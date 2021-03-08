from SpinTheWheel.TvFilm import constants
from SpinTheWheel.TvFilm.TMDb import search_movie_title, get_providers, check_netflix, check_apple, check_disney, \
    check_amazon
from SpinTheWheel.TvFilm.constants import grey_path
from SpinTheWheel.Wheel import get_tv


def search_tv_uri(title):
    return f"/search/tv?api_key={constants.api_key}&query={title}"


def providers_uri(title_id):
    return f"/tv/{title_id}/watch/providers?api_key={constants.api_key}"


def find_tv_info():
    result = get_tv()
    search_result = search_movie_title(search_tv_uri(result))
    if search_result == "Search not found":
        return [result, "static/images/TvFilmLogos/plain-white-background.jpg", grey_path("Apple"), grey_path("Disney"),
                grey_path("Netflix"), grey_path("Prime")]
    else:
        logo = search_result[1]
        providers = get_providers(providers_uri(search_result[0]))
        if providers == "No providers":
            return [result, logo, grey_path("Apple"), grey_path("Disney"), grey_path("Netflix"), grey_path("Prime")]
        else:
            netflix_logo = check_netflix(providers)
            apple_logo = check_apple(providers)
            disney_logo = check_disney(providers)
            prime_logo = check_amazon(providers)
            return [result, logo, apple_logo, disney_logo, netflix_logo, prime_logo]
