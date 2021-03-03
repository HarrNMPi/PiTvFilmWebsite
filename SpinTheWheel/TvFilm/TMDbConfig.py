import requests
import constants

get_config_uri = f"/configuration?api_key={constants.api_key}"


def get_config():
    full_url = constants.base_url + get_config_uri
    request = requests.get(full_url)
    content = request.json()["images"]
    base_url = content["base_url"]
    poster_sizes = content["poster_sizes"]
    return [base_url, poster_sizes]


# print(get_config())

# poster_sizes = ['http://image.tmdb.org/t/p/', ['w92', 'w154', 'w185', 'w342', 'w500', 'w780', 'original']]
