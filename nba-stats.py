from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()


def get_links():
	data = get(BASE_URL + ALL_JSON).json()
	links = data['links']
	return links

def get_scoreboard():
	scoreboard = get_links()['currentScoreboard']
	games = get(BASE_URL + scoreboard).json()['games']

	for game in games:
		home_team = game['hTeam']
		away_team = game['vTeam']
		clock = game['clock']
		period = game['period']
		print("================================")
		print(f"{home_team['triCode']} vs {away_team['triCode']}")
		print(f"{home_team['score']} - {away_team['score']}")
		print(f"Quarter: {period['current']}")
		print(f"Clock: {clock}")

def get_stats():
	stats = get_links()['leagueTeamStatsLeaders']
	teams = get(BASE_URL + stats).json()['league']['standard']['regularSeason']['teams'] # notice how you can chain down the json
	teams = list(filter(lambda x: x['name'] != "Team", teams)) # if function returns true keep it if not remove it
	teams.sort(key=lambda x: int(x['ppg']['rank']))

	for team in teams:
		name = team['name']
		nickname = team['nickname']
		ppg = team['ppg']['avg']
		print("================================")
		print(f"{nickname} - {ppg}")
	


get_stats()