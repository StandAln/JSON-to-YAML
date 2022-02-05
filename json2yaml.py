import yaml
import json

with open('.\json-yaml\input.json') as json_in:
    with open ('.\json-yaml\output.yaml', 'w') as yaml_out:
        yaml.dump(json.load(json_in),yaml_out)