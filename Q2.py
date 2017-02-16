global returnNumber

def factorial( n ):
   if n <1:   # base case
       return 1
   else:
       returnNumber = n * factorial( n - 1 )  # recursive call
       return returnNumber

# Change this value for a different result
with open('factorial-in.txt', 'r') as f:
		for line in f:
			num= int(line)

fo = open("factorial-out.txt", "rw+")
if num < 0:
	fo.write("Sorry, factorial does not exist for negative numbers")
elif num == 0:
	fo.write("Factorial for 0 is 1")
else:
	x=str(factorial(num))

	fo.write(x)