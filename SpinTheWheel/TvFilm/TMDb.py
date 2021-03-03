import requests
from SpinTheWheel.TvFilm import constants
from SpinTheWheel.TvFilm.constants import grey_path
from SpinTheWheel.Wheel import get_film


def search_movie_uri(title):
    return f"/search/movie?api_key={constants.api_key}&query={title}"


def providers_uri(title_id):
    return f"/movie/{title_id}/watch/providers?api_key={constants.api_key}"


def search_movie_title(title):
    full_url = constants.base_url + search_movie_uri(title)
    request = requests.get(full_url)
    try:
        content = request.json()["results"][0]
    except IndexError:
        return "Movie not found"
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


def get_providers(title_id):
    full_url = constants.base_url + providers_uri(title_id)
    request = requests.get(full_url)
    try:
        content = request.json()["results"]["GB"]["flatrate"]
    except KeyError:
        return "No providers"
    else:
        return content


def find_film_info():
    result = get_film()
    search_result = search_movie_title(result)
    if search_result == "Movie not found":
        return [result, "static/images/TvFilmLogos/plain-white-background.jpg", grey_path("Apple"), grey_path("Disney"), grey_path("Netflix"), grey_path("Prime")]
    else:
        film_logo = search_result[1]
        providers = get_providers(search_result[0])
        if providers == "No providers":
            return [result, film_logo, grey_path("Apple"), grey_path("Disney"), grey_path("Netflix"), grey_path("Prime")]
        else:
            netflix_logo = check_netflix(providers)
            apple_logo = check_apple(providers)
            disney_logo = check_disney(providers)
            prime_logo = check_amazon(providers)
            return [result, film_logo, apple_logo, disney_logo, netflix_logo, prime_logo]

# x = search_movie_title("Iron Man")[0]
# print(x)
# print(get_providers(x))

# 138832
# greyhound 516486
# iron man 1726
