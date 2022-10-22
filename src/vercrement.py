import sys
from os.path import exists
import re

PART_PATCH = 'patch'
PART_MINOR = 'minor'
PART_MAJOR = 'major'

def incrementSemver(major, minor, patch, VersionPart):
  if VersionPart == PART_PATCH:
    patch += 1
  elif VersionPart == PART_MINOR:
    minor += 1
  elif VersionPart == PART_MAJOR:
    major += 1

  return '{}.{}.{}'.format(major, minor, patch)


fname = sys.argv[1]
VersionPart = PART_PATCH if len(sys.argv) < 3 else sys.argv[2].lower()
if not VersionPart == PART_MINOR and not VersionPart == PART_MAJOR:
  VersionPart = PART_PATCH 

if not exists(fname):
  sys.exit('File does not exist: {}'.format(fname))

output = ''
infile = open(fname, 'r')
for line in infile.readlines():
  matches = re.search(r'(.*version.*?=.*?)(\d+)\.(\d+)\.(\d+)(.*)', line)
  if matches:
    output += matches.group(1) + incrementSemver(int(matches.group(2)), int(matches.group(3)), int(matches.group(4)), VersionPart) + matches.group(5) + '\n'
  else:
    output += line

infile.close()

outfile = open(fname, 'w')
outfile.write(output)
outfile.close()

print ('{}: {}'.format(fname, VersionPart))