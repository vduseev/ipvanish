import argparse
import requests
import appdirs
import time
import json
import os

API_URL = 'https://www.ipvanish.com/api/servers.geojson'
CACHE_TIMEOUT = 120  # seconds

def process_command():
    data = get_data()
    print(data[0]['type'])

def build_arg_parser():
    parser = argparse.ArgumentParser(description='IPVanish Command Line')
    parser.add_argument('--c', help='Filter by two-letter country code')
    parser.add_argument('--l')

def get_data():
    # 1. Check if fresh cached version is available
    if is_cache_fresh():
        print('Cache is still fresh. Reusing downloaded API response.')
        data = read_cache()
    # 2. Else retrieve from API and cache that
    else:
        print('Requesting servers status from IPVanish.')
        data = call_api()
        cache_data(data)
    return data

def is_cache_fresh():
    try:
        cached_at = int(os.path.getmtime(cache_file_path()))
        now = int(time.time())
        return True if now - cached_at < CACHE_TIMEOUT else False
    except OSError as e:
        # cache file does not exist or is inaccessible
        return False

def read_cache():
    with open(cache_file_path(), 'r') as f:
        data = f.read()
        json_string = json.loads(data)
    return json_string

def call_api():
    r = requests.get(API_URL)
    return r.json()

def cache_data(data):
    with open(cache_file_path(), 'w') as f:
        json_string = json.dumps(data)
        f.write(json_string)
        print('API response is cached.')

def cache_file_path():
    return './servers.geojson'
    # return os.path.join(
    #     cache_dir_path(),
    #     '.servers.geojson'
    # )

def cache_dir_path():
    return appdirs.user_cache_dir(
        appname='ipvanish',
        appauthor='vduseev'
    )

def unix_timestamp():
    return str(
        int(time.time())
    )

if __name__ == '__main__':
    process_command()
