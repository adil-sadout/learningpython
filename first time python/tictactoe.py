tictactoe = [[0,0,0],[0,0,0],[0,0,0]]


class game_board(object):
	tictactoe = [[0,0,0],[0,0,0],[0,0,0]]
	def print_game():
		print("   a  b  c")
		for count, row in enumerate(tictactoe):
			print(count,row)
	def play_round(x,y):
		print("   a  b  c")
		tictactoe[x][y]=1
		for count, row in enumerate(tictactoe):
			print(count,row)

game_board.print_game()

game_board.play_round(1,1)

game_board.print_game()

