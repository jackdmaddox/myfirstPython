#Print a NxN square of * characters. Prompt the user for N. Example output:
"""
singlesquare = "*"
user_input = int(input("How big is the square?"))
squarelength = singlesquare * user_input
for x in squarelength:
    print(x * (user_input))
"""
square_rows = 0
user_input = int(input("How big is the square?"))

while square_rows < user_input:
    square_rows += 1
    print(" *" * user_input)