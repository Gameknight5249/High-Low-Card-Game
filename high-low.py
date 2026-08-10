import random
## The 4 Suit in a Deck of Card ( in order from Least to Greatest)
suit = ["Clubs", "Diamonds", "Hearts", "Spades"]

## Ordered from Least to Greatest
number = [ "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

## The suit of the first card
baselineSuit = random.choice(suit)

## The number of the first card
baselineNumber = random.choice(number)

## - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def main():

    print( "Welcome to Adi's High/Low Game\n")
    print( "Rules are: Clubs < Diamonds < Hearts < Spades\n")
    print( "And: Ace is lowest and King is highest\n")

    compPick()

    UserInput = str(input("High or Low? "))
    UserInput = UserInput.lower().strip()
    ## print(UserInput) - this can be used to check if the user's input is being recorded properly

    gameLogic(UserInput)
   
   

def compPick():
        
        message = f"The baseline card is \033[31m{baselineNumber}\033[0m of \033[31m{baselineSuit}\033[0m\n "

        print(message)

def gameLogic(choice):
        
    ## This is the second card's suite
    userSuit = random.choice(suit)
    ## This is the second card's number
    userNumber = random.choice(number)
        
    message2 = f"\nThe second card is \033[31m{userNumber}\033[0m of \033[31m{userSuit}\033[0m\n"


    ## This is the index of first card's suite: 
    ## Since the list is in order from least to greatest
    ## I am using the indexs to compare which card is higher or lower
       
    BaselineSuitPosition = suit.index(baselineSuit)

    BaselineNumberPosition = number.index(baselineNumber)
        
    UserSuitPosition = suit.index(userSuit)
        
    UserNumberPosition = number.index(userNumber)
        

    if choice == "high":
        if UserSuitPosition > BaselineSuitPosition:
            print(message2)
            print("Therefore you Won!!!")
        elif UserSuitPosition == BaselineSuitPosition:
            if UserNumberPosition > BaselineNumberPosition:
                print(message2)
                print("Therefore you Won!!!")
            elif UserNumberPosition == BaselineNumberPosition:
                print(message2)
                print("Wow!, your lucky that we tied")
            else:
                print(message2)
                print("Oof, sorry you lost :(")     
        else:
            print(message2)
            print("Oof, sorry you lost :(")


    if choice == "low":
        if UserSuitPosition < BaselineSuitPosition:
            print(message2)
            print("Therefore you Won!!!")
        elif UserSuitPosition == BaselineSuitPosition:
            if UserNumberPosition < BaselineNumberPosition:
                print(message2)
                print("Therefore you Won!!!")
            elif UserNumberPosition == BaselineNumberPosition:
                print(message2)
                print("Wow!, your lucky that we tied")
            else:
                print(message2)
                print("Oof, sorry you lost :(")
        else:
            print(message2)
            print("Oof, sorry you lost :(")

main()
