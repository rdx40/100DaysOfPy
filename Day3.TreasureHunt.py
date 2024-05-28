print("Welcome to Treaure Island.\n")   
print("Your mission is to find the treasure.\n")    
direction=input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n")        
if(direction=="left"):
    print("You've come to a lake. There is an island in the middle of the lake.\n") 
    choice=input("Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")  
    if(choice=="wait"):
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.\n")
        door=input("Which color do you choose?\n")
        if(door=="red"):
            print("It's a room full of fire. Game Over.\n")
        elif(door=="yellow"):
            print("You found the treasure! You Win!\n")
        elif(door=="blue"):
            print("You enter a room of beasts. Game Over.\n")
        else:
            print("You chose a door that doesn't exist. Game Over.\n")
    else:
        print("You got attacked by an angry trout. Game Over.\n")
else:
    print("You fell into a hole. Game Over.\n")
    



###basic algo 
##if player choses right he dies
##if player choses left he comes to a lake
##in lake if player choses swim he dies
##if player choses wait he reaches an island with 3 doors
##on island there are 3 doors red, yellow, blue
##if player choses red he dies
##if player choses yellow he wins   
##if player choses blue he dies
##if player choses any other color he dies
##if player choses any other direction he dies
##game over