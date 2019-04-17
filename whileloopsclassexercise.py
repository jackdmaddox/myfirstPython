#Prompt user over and over and over again

#Bye count set to zero, nothing said yet

bye_count = 0

while bye_count <3:
    #initial condition set to true
    should_run = True
    
    while should_run:
        user_input = input("What? ")
        print("%s" % (user_input,))
        
        if user_input == "bye":
            should_run = False
            bye_count = bye_count + 1
        print(bye_count)
