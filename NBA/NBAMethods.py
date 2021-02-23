from nba_api.stats.endpoints import leaguegamefinder
from NBA import Teams2021 as Teams
import random


def get_opponent(matchup):
    if "vs" in matchup:
        opponent = matchup.split(" vs. ")
        return opponent[1]
    else:
        opponent = matchup.split(" @ ")
        return opponent[1]


def get_games():
    random_team = random.choice(Teams.teamList)
    game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable=random_team.ID)
    games = game_finder.get_data_frames()[0]
    last_game = games.sort_values('GAME_DATE').iloc[-1]
    opponent = get_opponent(last_game['MATCHUP'])
    return [random_team.abbr, opponent, last_game['GAME_DATE']]

