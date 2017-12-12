# IPVanish Command Line Tool

`Live Demo or GIF here`

## What It Does
It calls IPVanish API for a current JSON of server statuses.
```
r = requests.get('https://www.ipvanish.com/api/servers.geojson')
```
Then it wraps it in a bunch of `argparse` command line helpies.
It also caches the response and reloads it only if **120** seconds have passed since last API call.
The source file is about ~200 lines of Python 3 code in a single script.
Uses `requests` and `appdirs` packages (for cross-platform user-app
cache folder access)

## Use Cases
* Get the whole list of servers `ipvanish`
* Filter by country code `ipvanish CH` or `ipvanish US` or whatever
* Filter by country name `ipvanish States`
* Sort by latency (capacity) `ipvanish -l`
* Show first 10 servers `ipvanish States -n 10`
* Show only visible and online servers `ipvanish -o`
* Show all countries
* Show help message `ipvanish -h`

## User Stories
__Quickly, show me top 10 least loaded online VPN servers in Frankfurt:__
```
ipvanish Frankfurt -lo -n 10
# after 3 seconds of wait...

```

__Okay, great. Now show me first 30 VPN servers from USA. But do it faster,
dammit, are you mining Bitcoin there?__
```
ipvanish States -n 30
# after 0 seconds of wait (because API response is cached)...

```

## Installation

### Dependencies
* `python 3`
* `requests`
* `appdirs`

### MacOS X
If you don't have Python 3, then you need to install it using Homebrew.
```
brew install python3
```
If you don't have Homebrew, please install it. It's really a must have.
```
cd ipvanish_installation_location
git clone git@github.com:vduseev/ipvanish.git
cd ipvanish
./ipvanish
```
