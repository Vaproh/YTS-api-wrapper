import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import certifi

class YTSAPI:
    BASE_URL = "https://yts.mx/api/v2/"

    def __init__(self, verify_ssl=True, custom_ca_bundle=None):
        """
        Initialize the YTSAPI wrapper.

        :param verify_ssl: Whether to verify SSL certificates (default: True).
        :param custom_ca_bundle: Path to a custom CA bundle file (optional).
        """
        self.session = requests.Session()
        self.verify_ssl = verify_ssl
        self.custom_ca_bundle = custom_ca_bundle if custom_ca_bundle else certifi.where()

        # Configure retries with exponential backoff
        retries = Retry(
            total=5,  # Total number of retries
            backoff_factor=1,  # Exponential backoff factor
            status_forcelist=[500, 502, 503, 504],  # Retry on these status codes
            allowed_methods=["GET"]  # Only retry on GET requests
        )
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount("https://", adapter)

    def _make_request(self, endpoint, params=None):
        """
        Make a request to the YTS API.

        :param endpoint: The API endpoint to call.
        :param params: Query parameters for the request.
        :return: JSON response or None if the request fails.
        """
        url = f"{self.BASE_URL}{endpoint}"
        try:
            response = self.session.get(
                url,
                params=params,
                timeout=10,  # Add a timeout
                verify=self.verify_ssl
            )
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()
        except requests.exceptions.SSLError as e:
            print(f"SSL error occurred: {e}")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            return None
        except requests.exceptions.ConnectionError as e:
            print(f"Connection error occurred: {e}")
            return None
        except requests.exceptions.Timeout as e:
            print(f"Request timed out: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    def list_movies(self, limit=20, page=1, quality=None, genre=None, sort_by=None, order_by=None):
        """
        List movies from the YTS API.

        :param limit: Number of movies to return (default: 20).
        :param page: Page number (default: 1).
        :param quality: Filter by quality (e.g., "1080p").
        :param genre: Filter by genre (e.g., "action").
        :param sort_by: Sort by field (e.g., "title").
        :param order_by: Order by "asc" or "desc".
        :return: JSON response or None if the request fails.
        """
        params = {
            "limit": limit,
            "page": page,
            "quality": quality,
            "genre": genre,
            "sort_by": sort_by,
            "order_by": order_by
        }
        return self._make_request("list_movies.json", params=params)

    def movie_details(self, movie_id, with_images=False, with_cast=False):
        """
        Get details for a specific movie.

        :param movie_id: The ID of the movie.
        :param with_images: Include images in the response (default: False).
        :param with_cast: Include cast details in the response (default: False).
        :return: JSON response or None if the request fails.
        """
        params = {
            "movie_id": movie_id,
            "with_images": with_images,
            "with_cast": with_cast
        }
        return self._make_request("movie_details.json", params=params)

    def movie_suggestions(self, movie_id):
        """
        Get movie suggestions based on a movie ID.

        :param movie_id: The ID of the movie.
        :return: JSON response or None if the request fails.
        """
        params = {
            "movie_id": movie_id
        }
        return self._make_request("movie_suggestions.json", params=params)

    def movie_comments(self, movie_id):
        """
        Get comments for a specific movie.

        :param movie_id: The ID of the movie.
        :return: JSON response or None if the request fails.
        """
        params = {
            "movie_id": movie_id
        }
        return self._make_request("movie_comments.json", params=params)

    def movie_reviews(self, movie_id):
        """
        Get reviews for a specific movie.

        :param movie_id: The ID of the movie.
        :return: JSON response or None if the request fails.
        """
        params = {
            "movie_id": movie_id
        }
        return self._make_request("movie_reviews.json", params=params)

    def movie_parental_guides(self, movie_id):
        """
        Get parental guides for a specific movie.

        :param movie_id: The ID of the movie.
        :return: JSON response or None if the request fails.
        """
        params = {
            "movie_id": movie_id
        }
        return self._make_request("movie_parental_guides.json", params=params)

    def movie_upcoming(self):
        """
        Get a list of upcoming movies.

        :return: JSON response or None if the request fails.
        """
        return self._make_request("movie_upcoming.json")

    def get_magnet_url(self, hash, trackers=None):
        """
        Generate a magnet URL for a torrent hash.

        :param hash: The torrent hash.
        :param trackers: List of trackers (optional).
        :return: Magnet URL.
        """
        if trackers is None:
            trackers = [
                "udp://open.demonii.com:1337/announce",
                "udp://tracker.openbittorrent.com:80",
                "udp://tracker.coppersurfer.tk:6969",
                "udp://glotorrents.pw:6969/announce",
                "udp://tracker.opentrackr.org:1337/announce",
                "udp://torrent.gresille.org:80/announce",
                "udp://p4p.arenabg.com:1337",
                "udp://tracker.leechers-paradise.org:6969"
            ]
        magnet_url = f"magnet:?xt=urn:btih:{hash}"
        for tracker in trackers:
            magnet_url += f"&tr={tracker}"
        return magnet_url

