#Print odd numbers between 1 and 10

number_count = 0

while number_count < 9:
    should_run = True
    number_count = number_count + 1
    if number_count%2 == 1:
        print(number_count)

