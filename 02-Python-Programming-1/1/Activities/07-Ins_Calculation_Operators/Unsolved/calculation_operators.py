# Create our x and y variables
x = 5
y = 8
# Addition problem
answer = x + y 
print ("x + y =" +str(answer))
# Subtraction problem
answer = x - y
print ("x - y =" +str(answer))
# Multiplication problem
answer = x * y
print ("x * y =" +str(answer))
# Division problem
answer = x / y 
print ("x/y =" +str(answer))
# Modulus problem
answer = x % y
print ("x % y = " +str(answer))

# Floor division problem
answer = x // y
print ("x // y =" +str(answer))
# Exponent problem
answer = x ** y
print ("x ** y (x is to the y power) =" +str(answer))
# Order of operations problem without parenthesis
answer = x * y - x + y
print ("x * y - x + y = " +str(answer))
# Order of operations problem with parenthesis
answer = (x * y) + (x + y) - y
print ("(x * y) + (x + y) - y =" +str(answer))