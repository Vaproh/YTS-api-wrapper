# YTS API Wrapper

## Overview 🎬
This project is a Python wrapper for the [YTS API](https://yts.mx/api) that allows users to fetch movie details, list movies, get movie suggestions, reviews, parental guides, and generate magnet URLs for torrents.

## Features ⭐
- List movies with filters (quality, genre, sorting, etc.)
- Fetch detailed information about a specific movie
- Get movie suggestions based on a selected movie
- Retrieve movie comments, reviews, and parental guides
- Fetch upcoming movies
- Generate magnet URLs for torrents
- Configurable SSL verification and custom CA bundles
- Automatic retries for failed requests with exponential backoff

## Installation 🔧
### Requirements
- Python 3.x
- `requests`
- `urllib3`
- `certifi`

### Install Dependencies
```sh
pip install requests urllib3 certifi
```

## Basic Usage 🚀
### Initialize the API Wrapper
```python
from yts_api import YTSAPI

yts = YTSAPI(verify_ssl=True)
```

### List Movies
```python
movies = yts.list_movies(limit=5, quality="1080p", genre="action")
if movies:
    print(movies)
```

### Get Movie Details
```python
movie_id = 10  # Replace with a valid movie ID
details = yts.movie_details(movie_id)
if details:
    print(details)
```

For detailed usage and more examples, refer to the [documentation](./documentation.md) for more details.

## License 📜
This project is open-source and available under the MIT License.

## Disclaimer ⚠️
This project is for educational purposes only. Make sure to comply with copyright laws when using the YTS API.


