import yaml
from typing import Dict, Any

def load_config(config_path: str = 'config.yaml') -> Dict[str, Any]:
    try:
        with open(config_path, 'r') as config_file:
            config = yaml.safe_load(config_file)
        return config
    except FileNotFoundError:
        raise FileNotFoundError(f"Config file not found: {config_path}")
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file: {e}")

"""
Usage example
if __name__ == "__main__":
    try:
        config = load_config()
        print("Miners:")
        for miner in config['miners']:
            print(f"  - {miner['name']}: {miner['ip_start']} to {miner['ip_end']}")
        print(f"Username: {config['credentials']['username']}")
        print(f"Password: {config['credentials']['password']}")
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f"Error loading config: {e}")
"""