import requests

from SpinTheWheel.TvFilm import constants
from SpinTheWheel.TvFilm.constants import grey_path


# https://developers.themoviedb.org/3/getting-started/introduction


def search_movie_title(search_uri):
    full_url = constants.base_url + search_uri
    request = requests.get(full_url)
    try:
        content = request.json()["results"][0]
    except IndexError:
        return "Search not found"
    else:
        title_id = content["id"]
        poster_path = constants.poster_url + "original/" + content["poster_path"]
        return [title_id, poster_path]


def check_providers(content, provider_name, path_id):
    for provider in content:
        if provider["provider_name"] == provider_name:
            return f"static/images/TvFilmLogos/{path_id}_Logo.png"
        else:
            return grey_path(path_id)


def check_netflix(content):
    return check_providers(content, "Netflix", "Netflix")


def check_amazon(content):
    return check_providers(content, "Amazon Prime Video", "Prime")


def check_disney(content):
    return check_providers(content, "Disney Plus", "Disney")


def check_apple(content):
    return check_providers(content, "Apple TV Plus", "Apple")


def get_providers(providers_uri):
    full_url = constants.base_url + providers_uri
    request = requests.get(full_url)
    try:
        content = request.json()["results"]["GB"]["flatrate"]
    except KeyError:
        return "No providers"
    else:
        return content


# x = search_movie_title("Iron Man")[0]
# print(x)
# print(get_providers(x))

# 138832
# greyhound 516486
# iron man 1726
