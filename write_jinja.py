#!/usr/bin/env python
from gsfileman import included_files
import json
import ntpath
import os
from jinja2 import Template

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
    js[fname] = json.loads(str(f.read()))

# Process jinja template
f = open('../test.jj', 'r')
template = Template(f.read())
result   = template.render(js=js)
f.close()

# Write to file
f = open('../test.csv', 'w')
f.write(result)
f.close()
