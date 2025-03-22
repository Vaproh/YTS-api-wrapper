import requests


class YTSAPI:
    BASE_URL = "https://yts.mx/api/v2/"

    def __init__(self):
        self.session = requests.Session()

    def _make_request(self, endpoint, params=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def list_movies(
        self, limit=20, page=1, quality=None, genre=None, sort_by=None, order_by=None
    ):
        params = {
            "limit": limit,
            "page": page,
            "quality": quality,
            "genre": genre,
            "sort_by": sort_by,
            "order_by": order_by,
        }
        return self._make_request("list_movies.json", params=params)

    def movie_details(self, movie_id, with_images=False, with_cast=False):
        params = {
            "movie_id": movie_id,
            "with_images": with_images,
            "with_cast": with_cast,
        }
        return self._make_request("movie_details.json", params=params)

    def movie_suggestions(self, movie_id):
        params = {"movie_id": movie_id}
        return self._make_request("movie_suggestions.json", params=params)

    def movie_comments(self, movie_id):
        params = {"movie_id": movie_id}
        return self._make_request("movie_comments.json", params=params)

    def movie_reviews(self, movie_id):
        params = {"movie_id": movie_id}
        return self._make_request("movie_reviews.json", params=params)

    def movie_parental_guides(self, movie_id):
        params = {"movie_id": movie_id}
        return self._make_request("movie_parental_guides.json", params=params)

    def movie_upcoming(self):
        return self._make_request("movie_upcoming.json")

    def user_details(self, user_id):
        params = {"user_id": user_id}
        return self._make_request("user_details.json", params=params)

    def user_key(self, user_key):
        params = {"user_key": user_key}
        return self._make_request("user_key.json", params=params)

    def like_movie(self, movie_id, user_key):
        params = {"movie_id": movie_id, "user_key": user_key}
        return self._make_request("like_movie.json", params=params)

    def get_magnet_url(self, hash, trackers=None):
        if trackers is None:
            trackers = [
                "udp://open.demonii.com:1337/announce",
                "udp://tracker.openbittorrent.com:80",
                "udp://tracker.coppersurfer.tk:6969",
                "udp://glotorrents.pw:6969/announce",
                "udp://tracker.opentrackr.org:1337/announce",
                "udp://torrent.gresille.org:80/announce",
                "udp://p4p.arenabg.com:1337",
                "udp://tracker.leechers-paradise.org:6969",
            ]
        magnet_url = f"magnet:?xt=urn:btih:{hash}"
        for tracker in trackers:
            magnet_url += f"&tr={tracker}"
        return magnet_url


# Example usage
if __name__ == "__main__":
    yts = YTSAPI()

    # List movies
    movies = yts.list_movies(limit=5, quality="1080p", genre="action")
    print(movies)

    # Get movie details
    movie_id = movies["data"]["movies"][0]["id"]
    details = yts.movie_details(movie_id)
    print(details)

    # Generate magnet URL
    torrent_hash = details["data"]["movie"]["torrents"][0]["hash"]
    magnet_url = yts.get_magnet_url(torrent_hash)
    print(magnet_url)
