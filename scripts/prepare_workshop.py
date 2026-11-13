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
published_record = workspace / 'published-item.json'
if published_record.exists():
    published = json.loads(published_record.read_text())
    if set(published['dependencies']) != set(config['dependencies']):
        raise SystemExit('Published item belongs to a different Watcher implementation.')
    item_id = str(published['workshop_id'])
    id_file = workspace / 'mod_id.txt'
    if id_file.exists() and id_file.read_text().strip() != item_id:
        raise SystemExit('mod_id.txt differs from the published item record; inspect before uploading.')
    id_file.write_text(item_id + '\n')
description = config.get('description')
local_descriptions = [(workspace / name).read_text().strip() for name in
                      ('description.zh-CN.bbcode.txt', 'description.en.bbcode.txt')]
if description is None:
    if not published_record.exists():
        raise SystemExit('A first upload needs a description; no published item record exists.')
else:
    if description not in local_descriptions:
        raise SystemExit('Description text differs from local listing copy; synchronize before uploading.')
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
print('Visibility: ' + str(config.get('visibility') or 'unchanged on Steam'))
print('Payload contains only the DLL, PCK, and manifest. No Steam request was made.')
