from SpinTheWheel.TvFilm import constants
from SpinTheWheel.TvFilm.TMDb import search_movie_title, get_providers, check_netflix, check_apple, check_disney, \
    check_amazon
from SpinTheWheel.TvFilm.constants import grey_path
from SpinTheWheel.Wheel import get_film


def search_movie_uri(title):
    return f"/search/movie?api_key={constants.api_key}&query={title}"


def providers_uri(title_id):
    return f"/movie/{title_id}/watch/providers?api_key={constants.api_key}"


def find_film_info():
    result = get_film()
    search_result = search_movie_title(search_movie_uri(result))
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

# x = search_movie_title("Iron Man")[0]
# print(x)
# print(get_providers(x))

# 138832
# greyhound 516486
# iron man 1726
