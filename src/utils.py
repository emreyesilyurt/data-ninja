import json
from configparser import ConfigParser

def load_proxies(file_path):
    with open(file_path, 'r') as f:
        proxies_config = json.load(f)
    return proxies_config['proxies']

def load_config(file_path):
    config = ConfigParser()
    config.read(file_path)
    return config

def load_item_urls(file_path):
    with open(file_path, 'r') as f:
        items_config = json.load(f)
    return items_config['item_urls']
