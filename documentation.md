# YTS API Wrapper - Full Documentation

## Introduction
The **YTS API Wrapper** is a Python library that provides an easy way to interact with the [YTS API](https://yts.mx/api). It allows users to fetch movie details, list movies, get suggestions, retrieve reviews, parental guides, and generate magnet URLs for torrents.

## Installation
### Requirements
- Python 3.x
- `requests`
- `urllib3`
- `certifi`

### Install Dependencies
```sh
pip install requests urllib3 certifi
```

## Initialization
To use the API wrapper, you need to create an instance of the `YTSAPI` class:

```python
from yts_api import YTSAPI

yts = YTSAPI(verify_ssl=True)
```
- `verify_ssl`: Enables or disables SSL verification (default: `True`).
- `custom_ca_bundle`: Optional path to a custom CA bundle file.

## Available Methods & Examples

### 1. List Movies
Fetches a list of movies with optional filters.

```python
movies = yts.list_movies(limit=5, quality="1080p", genre="action")
if movies:
    print(movies)
```
#### Parameters:
- `limit` (int): Number of movies to return (default: 20).
- `page` (int): Page number (default: 1).
- `quality` (str): Filter by quality (e.g., "1080p").
- `genre` (str): Filter by genre (e.g., "action").
- `sort_by` (str): Sorting field (e.g., "title").
- `order_by` (str): Order by "asc" or "desc".

### 2. Get Movie Details
Fetches details of a specific movie by ID.

```python
movie_id = 10
details = yts.movie_details(movie_id, with_images=True, with_cast=True)
if details:
    print(details)
```
#### Parameters:
- `movie_id` (int): ID of the movie.
- `with_images` (bool): Include images in the response (default: `False`).
- `with_cast` (bool): Include cast details (default: `False`).

### 3. Get Movie Suggestions
Fetches movie recommendations based on a given movie ID.

```python
suggestions = yts.movie_suggestions(movie_id=10)
if suggestions:
    print(suggestions)
```
#### Parameters:
- `movie_id` (int): ID of the movie.

### 4. Get Movie Comments
Retrieves user comments for a specific movie.

```python
comments = yts.movie_comments(movie_id=10)
if comments:
    print(comments)
```
#### Parameters:
- `movie_id` (int): ID of the movie.

### 5. Get Movie Reviews
Retrieves reviews for a specific movie.

```python
reviews = yts.movie_reviews(movie_id=10)
if reviews:
    print(reviews)
```
#### Parameters:
- `movie_id` (int): ID of the movie.

### 6. Get Movie Parental Guides
Retrieves parental guidance information for a specific movie.

```python
parental_guides = yts.movie_parental_guides(movie_id=10)
if parental_guides:
    print(parental_guides)
```
#### Parameters:
- `movie_id` (int): ID of the movie.

### 7. Get Upcoming Movies
Retrieves a list of upcoming movies.

```python
upcoming_movies = yts.movie_upcoming()
if upcoming_movies:
    print(upcoming_movies)
```
#### Parameters:
- None

### 8. Generate Magnet URL
Generates a magnet link for a torrent based on its hash.

```python
torrent_hash = "YOUR_TORRENT_HASH"
magnet_url = yts.get_magnet_url(torrent_hash)
print(magnet_url)
```
#### Parameters:
- `hash` (str): The torrent hash.
- `trackers` (list, optional): List of trackers.

## Error Handling
This wrapper includes robust error handling for:
- SSL errors
- HTTP errors
- Connection errors
- Timeouts
- General request exceptions

## License
This project is open-source and available under the MIT License.

## Disclaimer
This project is for educational purposes only. Ensure compliance with copyright laws when using the YTS API.

