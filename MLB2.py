import statsapi


def recent_game():
	team_name = 147
	game = statsapi.last_game(team_name)
	return game

def show_linescore():
	game = recent_game()
	line_score = statsapi.linescore(game, timecode=None)
	print(line_score)


show_linescore()



