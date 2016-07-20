from gsfileman import included_files
import json
import ntpath


fpaths = included_files('.', ['*.json'])

js = dict()
for fpath in fpaths:
    f = open(fpath, 'r')
    fname = ntpath.basename(fpath)[:-5]
    js[fname] = json.loads(f.read())

print("{0} files loaded".format(len(js)))

