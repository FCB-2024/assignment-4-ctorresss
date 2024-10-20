import sys

# Comprovar que hi ha almenys un argument i que és un número enter
if len(sys.argv) > 1 and sys.argv[1].isdigit():
    x = int(sys.argv[1])

def main(x):
	i = 1
	sx = 0
	s = 0
	j = 1
	# Comptem els divisors del número donat
	while (i <= x):
		if (x % i == 0):
			sx = sx + 1
		i = i + 1	

	# Comprovem els divisors dels números més petits
	while (x - 1 > 0):
		x = x - 1
		s = 0
		j = 1 
		while (j <= x):
			if (x % j == 0):
				s = s + 1
			j = j + 1

		if (s >= sx):
			return("not anti-prime")
	return("anti-prime")

	## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :
		## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
		## TO RUN THIS PROGRAM AS, FOR INSTANCE:
		## $ python antiprime.py 6
		## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
		## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
	print(main(x))
else:
    print("Error: Please provide a valid integer.")