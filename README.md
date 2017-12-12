# IPVanish Command Line Tool

[![asciicast](https://asciinema.org/a/152203.png)](https://asciinema.org/a/152203)

## What It Does
It calls **IPVanish API** for a list of current server statuses.
```
r = requests.get('https://www.ipvanish.com/api/servers.geojson')
```
It wraps it in a bunch of `argparse` command line *"helpies"*.
It also caches the response and reloads it only if **120** seconds have passed since the last API call.
The source file is about ~200 lines of `Python 3` code in a single script.
Tee project uses `requests` and `appdirs` packages
(for cross-platform implementation of user-app cache folder)

To be honest, this script is dumb as 2 cents,
but it solves a problem of quickly listing IPVanish servers.

## Use Cases (when to use it)
* Get the whole list of servers: `ipvanish`
* Filter by country code: `ipvanish CH` or `ipvanish US` or whatever
* Filter by country name: `ipvanish States`
* Filter by town name: `ipvanish Seattle`
* Filter by region code: `ipvanish WA`
* Filter by continent code: `ipvanish EU`
* Sort by latency (capacity), fastest first: `ipvanish -l`
* Show first 10 servers from search results: `ipvanish States -n 10`
* Show only the servers that are online: `ipvanish -o`
* Show this help message: `ipvanish -h`

## User Stories (how do you actually use it)
__Quickly, show me top 10 least loaded online VPN servers in Frankfurt:__
```
ipvanish Frankfurt -lo -n 10
# after 2-3 seconds of wait...
Requesting servers status from IPVanish.
API response is cached.
Frankfurt, Germany fra-a27.ipvanish.com 5% capacity
Frankfurt, Germany fra-a33.ipvanish.com 5% capacity
Frankfurt, Germany fra-a34.ipvanish.com 5% capacity
Frankfurt, Germany fra-a38.ipvanish.com 5% capacity
Frankfurt, Germany fra-a43.ipvanish.com 5% capacity
Frankfurt, Germany fra-a47.ipvanish.com 5% capacity
Frankfurt, Germany fra-a52.ipvanish.com 5% capacity
Frankfurt, Germany fra-a56.ipvanish.com 5% capacity
Frankfurt, Germany fra-a02.ipvanish.com 6% capacity
Frankfurt, Germany fra-a04.ipvanish.com 6% capacity
```

__Okay, great. Now show me first 30 VPN servers from USA. But do it faster,
dammit, are you mining Bitcoin there?__
```
ipvanish States -n 30
# after 0 seconds of wait (because API response is cached)...
Cache is still fresh. Reusing downloaded API response.
Seattle, United States sea-a01.ipvanish.com 42% capacity
Miami, United States mia-a02.ipvanish.com 37% capacity
Los Angeles, United States lax-a02.ipvanish.com 34% capacity
Chicago, United States chi-a04.ipvanish.com 54% capacity
San Jose, United States sjc-a01.ipvanish.com 33% capacity
Ashburn, United States iad-a02.ipvanish.com 52% capacity
Phoenix, United States phx-a01.ipvanish.com 47% capacity
Atlanta, United States atl-a03.ipvanish.com 48% capacity
New York, United States nyc-a03.ipvanish.com 46% capacity
Dallas, United States dal-a02.ipvanish.com 51% capacity
San Jose, United States sjc-a03.ipvanish.com 35% capacity
Seattle, United States sea-a02.ipvanish.com 37% capacity
Atlanta, United States atl-a02.ipvanish.com 56% capacity
Phoenix, United States phx-a02.ipvanish.com 34% capacity
San Jose, United States sjc-a02.ipvanish.com 34% capacity
Los Angeles, United States lax-a03.ipvanish.com 39% capacity
Miami, United States mia-a04.ipvanish.com 28% capacity
Chicago, United States chi-a02.ipvanish.com 59% capacity
Seattle, United States sea-a03.ipvanish.com 31% capacity
Miami, United States mia-a03.ipvanish.com 36% capacity
New York, United States nyc-a04.ipvanish.com 46% capacity
Chicago, United States chi-a01.ipvanish.com 62% capacity
New York, United States nyc-a01.ipvanish.com 80% capacity
San Jose, United States sjc-a04.ipvanish.com 43% capacity
Chicago, United States chi-a03.ipvanish.com 56% capacity
Ashburn, United States iad-a01.ipvanish.com 62% capacity
Los Angeles, United States lax-a01.ipvanish.com 61% capacity
New York, United States nyc-a02.ipvanish.com 47% capacity
Miami, United States mia-a01.ipvanish.com 36% capacity
Atlanta, United States atl-a01.ipvanish.com 65% capacity
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
