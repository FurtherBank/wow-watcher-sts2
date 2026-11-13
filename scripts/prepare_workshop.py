"""Stage the tested build and validate Workshop materials without contacting Steam."""
from pathlib import Path
import hashlib
import json
import shutil

root = Path(__file__).resolve().parent.parent
workspace = root / 'workshop'
source = root / 'dist' / 'WowWatcher'
files = ('WowWatcher.dll', 'WowWatcher.pck', 'WowWatcher.json')
for name in files:
    if not (source / name).is_file():
        raise SystemExit('Build the mod first with scripts/build.sh; missing ' + name)
manifest = json.loads((source / 'WowWatcher.json').read_text())
config = json.loads((workspace / 'workshop.json').read_text())
if manifest['version'] != json.loads((root / 'WowWatcher.json').read_text())['version']:
    raise SystemExit('Build version differs from source manifest; rebuild first.')
if set(config['dependencies']) != {3747492505, 3737335127}:
    raise SystemExit('Workshop must require the specified Watcher and BaseLib items.')
if config['description'] != (workspace / 'description.zh-CN.bbcode.txt').read_text().strip():
    raise SystemExit('Description text differs from workshop.json; synchronize both files.')
for image in [workspace / 'image.png', *sorted((workspace / 'previews').glob('*'))]:
    if not image.is_file() or not 0 < image.stat().st_size < 1_000_000:
        raise SystemExit('Preview must exist and be less than 1 MB: ' + str(image))
content = workspace / 'content'
content.mkdir(exist_ok=True)
if any(p.name not in files for p in content.iterdir()):
    raise SystemExit('Unexpected upload content; inspect workshop/content before proceeding.')
checksums = ['WowWatcher v' + manifest['version']]
for name in files:
    shutil.copy2(source / name, content / name)
    checksum = hashlib.sha256((content / name).read_bytes()).hexdigest()
    checksums.append(checksum + '  content/' + name)
(workspace / 'package-checksums.txt').write_text('\n'.join(checksums) + '\n')
print('Prepared ' + config['title'] + ', v' + manifest['version'])
print('Visibility: ' + str(config.get('visibility', 'unchanged')))
print('Payload contains only the DLL, PCK, and manifest. No Steam request was made.')
