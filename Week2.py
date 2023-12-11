def start_game():
  """Starts the game."""
  print("You wake up in a dark forest.")
  print("You hear a rustling in the bushes.")
  print("What do you do?")
  choice = input("> ").lower()
  if choice == "look around":
    print("You see a path leading deeper into the forest.")
  elif choice == "investigate the noise":
    print("You find a small, scared animal.")
    print("It scampers away into the darkness.")
  else:
    print("I don't understand what you mean.")
  play_again()

def play_again():
  """Asks the player if they want to play again."""
  choice = input("Do you want to play again? (y/n) ").lower()
  if choice == "y":
    start_game()
  else:
    print("Thanks for playing!")

start_game()