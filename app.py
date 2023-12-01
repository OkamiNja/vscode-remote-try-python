#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

def get_random_choice():
    options = ["rock", "paper", "scissors"]
    return random.choice(options)

def determine_winner(player, opponent):
    if player == opponent:
        return "Draw"
    elif (player == "rock" and opponent == "scissors") or (player == "scissors" and opponent == "paper") or (player == "paper" and opponent == "rock"):
        return "You Win"
    else:
        return "You Lose"

def play_game():
    score = {'You Win': 0, 'You Lose': 0, 'Draw': 0}

    while True:
        print("\nChoose: rock, paper, or scissors")
        player_choice = input().lower()

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please try again.")
            continue

        opponent_choice = get_random_choice()
        result = determine_winner(player_choice, opponent_choice)

        print(f"\nYou chose: {player_choice}, opponent chose: {opponent_choice}")
        print(f"Result: {result}")

        score[result] += 1

        while True:
            print("\nDo you want to play again? (yes/no)")
            option = input().lower()
            if option == "yes":
                break
            elif option == "no":
                print("\nFinal score:")
                print(f"You Win: {score['You Win']}, You Lose: {score['You Lose']}, Draw: {score['Draw']}")
                return
            else:
                print("Invalid response. Please respond with 'yes' or 'no'.")

if __name__ == "__main__":
    play_game()