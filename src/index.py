import json
import sys
sys.path.append('../smartyaml')

import smartyaml.smartyaml as xx

config = xx.loadConfig('tests/config/child.yaml')
print (json.dumps(config, indent=2))