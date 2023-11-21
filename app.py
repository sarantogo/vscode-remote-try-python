#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random
choice = True
rounds = 1
victories = 0
while choice==True:
    
    def get_computer_choice():
        options = ['rock', 'paper', 'scissors']
        return random.choice(options)

    def get_user_choice():
        choice = input("Enter your choice (rock, paper, or scissors): ")
        while choice not in ['rock', 'paper', 'scissors']:
            choice = input("Invalid choice. Enter your choice (rock, paper, or scissors): ")
        return choice

    def determine_winner(user_choice, computer_choice):
        global victories
        if user_choice == computer_choice:
            return "It's a tie!"
        if (user_choice == 'rock' and computer_choice == 'scissors') or \
        (user_choice == 'scissors' and computer_choice == 'paper') or \
        (user_choice == 'paper' and computer_choice == 'rock'):
            victories += 1
            return "You win!"
        else:
            return "You lose!"
        
    def continue_playing():
        global rounds
        choice = input("Do you want to play again? (y/n): ")
        while choice not in ['y', 'n']:
            choice = input("Invalid choice. Do you want to play again? (y/n): ")
        if(choice=='n'):
            print("You won",victories,"out of",rounds,"rounds.")
        else:
            rounds += 1
        return choice == 'y'

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}, computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))
    choice=continue_playing()