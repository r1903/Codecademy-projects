import random

money = 100

#Write your game of chance functions here
# function for coin flip game 
def coin_flip(guess,bet):
  print("coin flip game has started..")   

  if(bet > money or bet < 0):
      print("sorry you do not have enough money to bet!")
      return 0

  result = random.randint(1, 2)
  print("coin flip value: " + str(result)) 
  print("Guess value: " + str(guess)) 

  if result == 1:
      coin_toss="HEADS"
  else:
      coin_toss = "TAILS"
 
  if((guess.upper()).find(coin_toss) >= 0):
      endResult = "won"
      print("You won " + str(bet)+" bet!")
      return bet
  else:
       endResult = "lost"
       print("You lost " + str(bet)+" bet!")
       return -bet       

# function for Cho_han game    
def cho_han(guess,bet):
    print("cho_han game has began")
     
    if(bet > money or bet < 0):
      print("sorry you do not have enough money to bet!")
      return 0

    print("Guess value is : "+ str(guess))
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("First dice result: "+ str(dice1))
    print("Second dice result: "+ str(dice2))
    
    total = dice1 + dice2
    print("Total dice value: " + str(total))

    if(total % 2 == 0 and guess == "Even"):
        print("Your guess was right and you won " + str(bet)+" bet")
        return bet
    elif(total % 2 == 1 and guess == "Odd"):
        print("Your guess was right and you won " + str(bet)+" bet")
        return bet
    else:
         print("Your guess was wrong and you lost " + str(bet)+" bet")
         return -bet

# function for card game   
def card_game(bet):
    print("card game game has began")
    
    if(bet > money or bet < 0):
      print("sorry you do not have enough money to bet!")
      return 0

    card1 = random.randint(1, 10)
    card2 = random.randint(1, 10)
    print("player1 card is " + str(card1))
    print("player2 card is " + str(card2))

    if(card1 > card2):
        print("player1 won " + str(bet) + " bet")
        return bet
    elif(card2 > card1):
        print("player2 won " + str(bet) + " bet")
        return -bet
    else:
        print("There is tie")
        return 0   


# function for roulette game   

def roulette(guess, bet):
    print("Roulette game has began")

    if(bet > money or bet < 0):
      print("sorry you do not have enough money to bet!")
      return 0
    
    print("your guess is " + str(guess))

    result = random.randint(0, 37)
    print("Result value is " + str(result))

    if result == 37:
        print("The wheel landed on 00")
    else:
        print("The wheel landed on " + str(result))


    if result != 0 and result % 2 == 0 and guess=="Even":
        print(str(result) + " is an even number.")
        print("You won " + str(bet)+" bet")
        return bet
    elif result != 37 and result % 2 == 1 and guess=="Odd":
        print(str(result) + " is an odd number.")
        print("You won " + str(bet)+" bet")
        return bet
    elif guess == result:
        print("Result and guess are matching")
        print("You won " + str(bet)+" bet")
        return bet * 35  
    else:
        print("you lost " + str(bet))
        return -bet         


#Call your game of chance functions here
money += coin_flip("heads", 10)
money += cho_han("Even", 110)
money+=card_game(20)
money+=roulette("Even",10)
print("Total value of money left is: " + str(money))
