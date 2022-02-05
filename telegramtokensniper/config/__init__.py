import os
import yaml

file_dir = os.path.dirname(__file__)

with open(f'{file_dir}/general.yml', 'r') as f:
    general_params = yaml.safe_load(f)