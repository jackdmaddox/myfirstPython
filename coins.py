#Initially you have no coins. It will ask you if you want a coin? 
# If you type "yes", it will give you one coin, and print out the current tally. 
# If you type no, it will stop the program

coins = 0
should_run = True
while should_run:
    print("You have %s coins" % (coins,))
    coin_question = input("Do you want another? ")
    if coin_question == "yes":
        coins = coins + 1
        
    elif coin_question == "no":
        should_run = False
        print("Bye")
    
    
            
