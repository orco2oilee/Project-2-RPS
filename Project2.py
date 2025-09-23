#Orcun's Part
p1_wins = 0
p2_wins = 0
draws = 0
round_number = 1

choices = ["rock", "paper", "scissors"]

while False:
    print(f" Round {round_number} ")
    
#Joshua's Part
# Define choices for player 1 and player 2
p1_choice = input("Player 1, enter your choice (1=Rock, 2=Paper, 3=Scissors): ")
p2_choice = input("Player 2, enter your choice (1=Rock, 2=Paper, 3=Scissors): ")

if p1_choice == p2_choice:
    print("It's a draw!\n")
    draws += 1
elif (
    (p1_choice == "1" and p2_choice == "3") or
    (p1_choice == "2" and p2_choice == "1") or
    (p1_choice == "3" and p2_choice == "2")
):
    print("Player 1 wins this round!\n")
    p1_wins += 1
else:
    print("Player 2 wins this round!\n")
    p2_wins += 1

round_number += 1
again = input("Do you want to play again? (y/n): ").lower()
if again != "y":
    print("\n--- Final Results ---")
    print(f"Player 1 Wins: {p1_wins}")
    print(f"Player 2 Wins: {p2_wins}")
    print(f"Draws: {draws}")

    if p1_wins > p2_wins:
        print("Overall Winner: Player 1!")
    elif p2_wins > p1_wins:
        print("Overall Winner: Player 2!")
    else:
        print("It's an overall tie!")

if p1_wins > p2_wins:
    print("Overall Winner: Player 1!")
elif p2_wins > p1_wins:
    print("Overall Winner: Player 2!")
else:
    print("It's an overall tie!")
    
    round_number += 1

