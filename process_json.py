from gsfileman import included_files
import json
import ntpath
import os

# Look for jsons here:
path   = './test_cases/'

# Find jsons
fpaths = included_files(path, ['*.json'])

# change to jsons directory
os.chdir(path)

# Load each one into a dict
js = dict()
for fpath in fpaths:
    f = open(fpath, 'r')
    fname = ntpath.basename(fpath)[:-5]
    js[fname] = json.loads(f.read())

print("{0} files loaded".format(len(js)))

