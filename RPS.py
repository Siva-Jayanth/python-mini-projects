import random
def rps():
  user = input("Enter rock, paper, or scissors: ")
  computer = random.choice(["rock", "paper", "scissors"]) 
  if user == computer:
    print("It's a tie!")
  elif user == "rock":
    if computer == "paper":
      print("You lose! Paper covers rock.")
    else:
      print("You win! Rock smashes scissors.")
  elif user == "paper":
    if computer == "scissors":
      print("You lose! Scissors cuts paper.")
    else:
        print("You win! Paper covers rock.")