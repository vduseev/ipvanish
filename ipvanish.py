import argparse
import requests
import logging
import appdirs
import time
import json
import os

API_URL = 'https://www.ipvanish.com/api/servers.geojson'
CACHE_TIMEOUT = 120  # seconds

def process_command():
    data = get_data()
    args = arg_parser().parse_args()
    results = search(args.search_term, data)

    if args.latency_sorting:
        results = sorted(
            results, key=lambda server: server['properties']['capacity']
        )

    if args.online_filter:
        filtered = filter(
            lambda server: server['properties']['online'],
            results
        )

    if args.limit_filter is not None:
        results = results[:args.limit_filter]

    for server in results:
        print_server(server)

def get_data():
    if is_cache_fresh():
        # 1. Check if fresh cached version is available
        logging.info(
            ('Cache is still fresh. '
             'Reusing downloaded API response.')
        )
        data = read_cache()
    else:
        # 2. Else retrieve from API and cache that
        logging.info(
            'Requesting server status from IPVanish.'
        )
        data = call_api()
        cache_data(data)
    return data

def arg_parser():
    parser = argparse.ArgumentParser(
        description='IPVanish Command Line Tool'
    )

    parser.add_argument(
        'search_term',
        nargs='?',
        default=None,
        type=str,
        help='Search filter'
    )

    parser.add_argument(
        '-l', '--l',
        action='store_true',
        default=False,
        dest='latency_sorting',
        help='Sort by latency (capacity)'
    )
 
    parser.add_argument(
        '-o', '--o',
        action='store_true',
        default=False,
        dest='online_filter',
        help='Only show online visible servers'
    )

    parser.add_argument(
        '-n', '--n',
        default=None,
        type=int,
        dest='limit_filter',
        help='Show first N servers'
    )

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 0.1.0'
    )

    return parser

def search(search_term, data):
    if search_term is None:
        return data

    search_for_short_code = False
    if len(search_term) == 2 and search_term.upper() == search_term:
        search_for_short_code = True
    query = search_term.lower()
    results = []
    for server in data:
        # 1. Search by Title
        if query in server['properties']['title'].lower():
            results.append(server)
        # 2. Search by Country Code
        if query in server['properties']['countryCode'].lower():
            results.append(server)
        # 3. Search by Region Code
        if query in server['properties']['regionCode'].lower():
            results.append(server)
        # 4. Search by Continent
        if query in server['properties']['continent'].lower():
            results.append(server)
        # 5. Search by Continent Code
        if query in server['properties']['continentCode'].lower():
            results.append(server)
        # 6. Search if search term is 2 characters long
        if search_for_short_code:
            query = search_term.upper()
            if query in server['properties']['countryCode'].upper() or \
               query in server['properties']['continentCode'].upper() or \
               query in server['properties']['regionAbbr'].upper():
                results.append(server)

    return results

def print_server(server):
    logging.info('{:>30} {:>20} {:>4}% capacity'.format(
        server['properties']['title'],
        server['properties']['hostname'],
        server['properties']['capacity']
    ))

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
        logging.info('API response is cached.')

def cache_file_path():
    return './servers.geojson'

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
    logging.basicConfig(
        format='%(asctime)s %(levelname)s %(message)s',
        level=logging.DEBUG
    )
    process_command()
