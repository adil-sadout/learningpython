tictactoe = [[1,2,3],[4,5,6],[7,8,9]]
			



def print_game():
	print("   0  1  2")
	for count, row in enumerate(tictactoe):
		print(count,row)



def winner(lst,x,y):
	for row in tictactoe:
		print(row[y] ,tictactoe[x][y])

	if tictactoe[x][y] != tictactoe[x]:
		return False

	for row in tictactoe:
		if row[y] != tictactoe[x][y]:
			return False
	
	
def play_round(x,y):
	try:
		print("   0  1  2")
		tictactoe[x][y]=1
		for count, row in enumerate(tictactoe):

			print(count,row)

		if winner(tictactoe,x,y)== True:
				print("You have won")
		
	except:
		print("something went wrong!!!")



play_round(0,2)


play_round(2,2)