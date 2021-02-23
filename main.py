from flask import Flask, render_template, request

from AdventureChallenge.adventureChallenge import get_adventure, format_input
from NBA import NBAMethods
from NBA.NBAMethods import get_games
from SpinTheWheel.PaintNumbers.PaintNumbers import get_paint_number
from SpinTheWheel.Wheel import get_book, get_film, get_tv

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
    result = get_tv()
    return render_template("SpinTheWheel/tvSpin.html", result=result)


@app.route('/filmSpin')
def film_wheel():
    result = get_film()
    return render_template("SpinTheWheel/filmSpin.html", result=result)


@app.route('/bookSpin')
def book_wheel():
    result = get_book()
    return render_template("SpinTheWheel/bookSpin.html", result=result)


@app.route('/paintSpin')
def paint_wheel():
    result = get_paint_number()
    return render_template("SpinTheWheel/paintSpin.html", result=result)


@app.route('/NBA')
def nba():
    answer_list = get_games()
    team = answer_list[0]
    opp = answer_list[1]
    date = answer_list[2]
    return render_template('NBA.html', team=team, opp=opp, date=date)


# Adventure Challenge
@app.route('/AdventureChallenge')
def adventure_challenge():
    location = request.args.get("location")
    when = request.args.get("when")
    supplies = request.args.get("supplies")
    if not location and not when and not supplies:
        challenge_number = ""
    elif location == "blank" and when == "blank" and supplies == "blank":
        challenge_number = ""
    elif location and when and supplies:
        challenge_number = get_adventure(location, when, supplies)
    else:
        challenge_number = ""
    return render_template('adventureChallenge.html', challenge_number=challenge_number)


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0')