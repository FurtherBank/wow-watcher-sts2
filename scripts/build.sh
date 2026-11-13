#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
"${DOTNET_BIN:-dotnet}" build WowWatcher.csproj -c Release --nologo "$@"
mkdir -p dist/WowWatcher
cp .godot/mono/temp/bin/Release/WowWatcher.dll WowWatcher.json dist/WowWatcher/
python3 scripts/pack.py
python3 - <<'PY'
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import json
root=Path('dist')
version=json.loads(Path('WowWatcher.json').read_text())['version']
with ZipFile(root/f'WowWatcher-{version}.zip','w',ZIP_DEFLATED) as archive:
    for path in sorted((root/'WowWatcher').iterdir()):
        archive.write(path,path.relative_to(root))
print(root/f'WowWatcher-{version}.zip')
PY
