tictactoe = [[0,0,0],[0,0,0],[0,0,0]]


class Game_Board(object):
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

Game_Board.print_game()

Game_Board.play_round(1,1)

Game_Board.print_game()

