import json
import os

def get_config():
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    
    with open(config_path, 'r') as file:
        config = json.load(file)
    
    return config
