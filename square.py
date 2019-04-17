#Print a 5x5 square of * characters. 
"""
stars = "*****"
for x in stars:
    print(x * 5)
"""

star_rows = 0
while star_rows < 5:
    star_rows += 1
    print(" *" * 5)