"""Pack Mod resources using Godot's unencrypted PCK v2 format."""
from pathlib import Path
import hashlib,struct
root=Path(__file__).resolve().parent.parent
files=[]
for path in sorted((root/'WowWatcher').rglob('*')):
    if not path.is_file() or path.suffix not in {'.json', '.png', '.res'}:
        continue
    name=('res://'+path.relative_to(root).as_posix()).encode()
    name+=b'\0'*((-len(name))%4)
    files.append((name,path.read_bytes()))
header=struct.pack('<6IQ',0x43504447,2,4,5,1,0,0)+bytes(64)+struct.pack('<I',len(files))
base=len(header)+sum(4+len(n)+8+8+16+4 for n,d in files)
base=(base+15)//16*16
entries=bytearray();payload=bytearray()
for name,data in files:
    entries+=struct.pack('<I',len(name))+name+struct.pack('<QQ',base+len(payload),len(data))+hashlib.md5(data).digest()+struct.pack('<I',0)
    payload+=data
    payload+=bytes((-len(payload))%16)
out=root/'dist/WowWatcher/WowWatcher.pck';out.parent.mkdir(parents=True,exist_ok=True)
out.write_bytes(header+entries+bytes(base-len(header)-len(entries))+payload)
print(out)
