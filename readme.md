# YTS API Wrapper 🎬🔥🎥

## Overview 🎞️📽️🍿
This project is a Python wrapper for the [YTS API](https://yts.mx/api) that allows users to fetch movie details, list movies, get movie suggestions, reviews, parental guides, and generate magnet URLs for torrents. 🎥✨🎬

## Features 🚀🎭🎞️
- List movies with filters (quality, genre, sorting, etc.)
- Fetch detailed information about a specific movie
- Get movie suggestions based on a selected movie
- Retrieve movie comments, reviews, and parental guides
- Fetch upcoming movies
- Generate magnet URLs for torrents
- Configurable SSL verification and custom CA bundles
- Automatic retries for failed requests with exponential backoff

## Installation 🛠️💻⚙️
### Requirements 📌🔧📦
- Python 3.x
- `requests`
- `urllib3`
- `certifi`

### Install Dependencies 📥⚡📜
```sh
pip install requests urllib3 certifi
```

## Usage 🎯📜💡
### Initialize the API Wrapper 🏗️🖥️🔌
```python
from yts_api import YTSAPI

yts = YTSAPI(verify_ssl=True)
```

### List Movies 🎬🔍📽️
```python
movies = yts.list_movies(limit=5, quality="1080p", genre="action")
if movies:
    print(movies)
```

### Get Movie Details 📋🔎🎞️
```python
movie_id = 10  # Replace with a valid movie ID
details = yts.movie_details(movie_id)
if details:
    print(details)
```

### Generate Magnet URL 🧲📡⚡
```python
torrent_hash = "YOUR_TORRENT_HASH_HERE"
magnet_url = yts.get_magnet_url(torrent_hash)
print(magnet_url)
```

## Error Handling ⚠️🐞🚨
The API wrapper handles various exceptions such as: ❌⚡🔍
- SSL errors
- HTTP errors
- Connection errors
- Timeouts
- General request exceptions

## License 📜⚖️🔓
This project is open-source and available under the MIT License. 🏛️🔓📖

## Disclaimer ⚠️📢📝
This project is for educational purposes only. Make sure to comply with copyright laws when using the YTS API. 🚫📜⚖️


