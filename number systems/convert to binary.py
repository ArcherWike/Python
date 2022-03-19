#from decimal -> binary
your_num = int(input("give the number to the convenor: "))

def convertToBinary(a):
	n = ""
	
	while (a>0):
		n = str(a % 2) + n
		a = a // 2   	
	return n


print(convertToBinary(your_num))


