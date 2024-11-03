#Hailey Clark and Lexi Nguyen Group 2
#Date: 02/27/2024
#Purpose: To create a game called Yahtzee

import check_input
import player


def take_turn(player):
  '''Roll the player’s dice, display the dice, check for and display any win types (pair, series, three-of-a-kind), and display the updated score'''

  #Initializing starting points and rolling dice
  prev_points = player._points
  player.roll_dice()

  #Printing dice roll
  print(player)

  #Checking for win types
  if player.has_three_of_a_kind():
    print("You got a three of a kind! +3 points")
  elif player.has_pair():
    print("You got a pair! +1 point")
  elif player.has_series():
    print("You got a series of 3! +2 points")
  elif player._points == prev_points:
    print("Aww. Too Bad. :( +0 points")

  #Printing total points
  print("Score = ", player.get_points())




def main():
  #Game begins
  print("-Yahtzee- \n")
  print("Game Start \n")
  play = True
  user = player.Player()
  
  #Game continues until user chooses to stop 
  while play:
    
    #For each game loop, takes a turn for player 
    take_turn(user)
    
    #Asks if user wants to continue 
    user_choice = check_input.get_yes_no("\nPlay again? (Y/N): ")
    
    #Checks for game stop condition 
    if not user_choice:
      play = False
      print("\nGame Over!")
      print("Your final score is: " + str(user.get_points()))

    print()
      

main()