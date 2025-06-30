"""
Minigame:
1. 2 nguoi choi
2. 3 options: rock, paper, scissors
3. rule: paper > rock, rock > scissors, scissors > paper
4. nhap lua chon cua nguoi
5. random lua chon cua may
6. dua ra ket qua
"""

import random


choices = ["rock", "paper", "scissors"]
choices_dict = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
print("Player's choice:", player_choice)
random_choice = random.choice(choices)
print("Computer's choice:", random_choice)

if player_choice == random_choice:
    print("It's a tie!")
elif choices_dict[player_choice] == random_choice:
    print("Player wins!")
else:
    print("Computer wins!")

