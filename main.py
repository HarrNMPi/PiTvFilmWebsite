from flask import Flask, render_template, request

from SpinTheWheel.TvFilm.TMDbFilm import find_film_info
from SpinTheWheel.TvFilm.TMDbTv import find_tv_info

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


# Spin The Wheel
@app.route('/SpinTheWheel')
def spin_the_wheel():
    return render_template("SpinTheWheel/spinTheWheel.html")


@app.route('/tvSpin')
def tv_wheel():
    result = find_tv_info()
    return render_template("SpinTheWheel/tvSpin.html", result=result[0], film_logo=result[1], apple_logo=result[2],
                           disney_logo=result[3], netflix_logo=result[4], prime_logo=result[5])


@app.route('/filmSpin')
def film_wheel():
    result = find_film_info()
    return render_template("SpinTheWheel/filmSpin.html", result=result[0], film_logo=result[1], apple_logo=result[2],
                           disney_logo=result[3], netflix_logo=result[4], prime_logo=result[5])

if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')
