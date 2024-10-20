## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW

import sys
x = int (sys.argv[1])

def main(x) :
	## YOU CODE SHOULD START HERE AST THE SAME
	## IDENTATION AS THIS COMMENT

	i = 1
	sx = 0
	s = 0
	j = 1

	# Comptem els divisors del número donat
	while (i <= x):
		if (x % i == 0):
			sx = sx + 1
		i = i + 1	

	print(sx)

	# Comprovem els divisors dels números més petits
	while (x - 1 > 0):
		x = x - 1
		s = 0
		j = 1 
		while (j <= x):
			if (x % j == 0):
				s = s + 1
			j = j + 1
		print(s)

		if (s >= sx):
			return("not anti-prime")
	else:
		return("anti-prime")

	## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"

## DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__" :

	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT

print(main(x))

