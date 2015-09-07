import sys
import subprocess
import pathlib

FLAG = '-small'

for orig in pathlib.Path('.').glob(sys.argv[1]):
    if FLAG in orig.stem:
        continue
    print orig
    small = orig.parent / (orig.stem + FLAG + orig.suffix)
    subprocess.check_call(['convert', str(orig), '-quality', '20', str(small)])
