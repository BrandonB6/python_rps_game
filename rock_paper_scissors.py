import random



def game():
    x = random.randint(0 , 2)
    response = input("Rock, Paper, or Scissors?")
    response = response.lower()
    li = ["rock", "paper", "scissors"]
    comp = print(f'The computers choice was {li[x]}')

    if li[x] == response:
        comp
        print("Game Draw")
    elif li[x] == "rock":
        comp
        if response == "scissors":
            print("You Lose")
        elif response == "paper":
            print("You Win!")
    elif li[x] == "paper":
        comp
        if response == "rock":
            print("You Lose")
        elif response == "scissors":
            print("You Win!")
    elif li[x] == "scissors":
        comp
        if response == "rock":
            print("You Win!")
        elif response == "paper":
            print("Your Lose")


def run():
    while True:
        invite = input("Would you like to play Rock, Paper, Scissors? if not say, 'quit'. ")
        if invite.lower() == "yes":
            game()
        elif invite.lower() == "quit":
            print("Thank you for playing")
            break
        else:
            print("Pleae try another response")

run()
        
    
