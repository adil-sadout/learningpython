#Collatz conjecture

def collarcong(k):
	while k != 1 :
		if (k%2) == 0:
			k=k/2
		elif (k%2) == 1:
			k=(k*3)+1

	print(k)




collarcong(999999999999999999999999999999999999999999999999999999999999999999999999999)

#whatever value you give it, it will always end up being 1