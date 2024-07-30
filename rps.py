import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'win'
    else:
        return 'lose'

def display_result(user_choice, computer_choice, result):
    print(f"\nYour choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")
    if result == 'tie':
        print("It's a tie!")
    elif result == 'win':
        print("You win!")
    else:
        print("You lose!")

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock, Paper, Scissors!")
    
    while True:
        while True:
            user_choice = input("\nEnter your choice (rock, paper, or scissors): ").strip().lower()
            if user_choice in ['rock', 'paper', 'scissors']:
                break
            else:
                print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

        computer_choice = get_computer_choice()
    
        result = determine_winner(user_choice, computer_choice)
    
        display_result(user_choice, computer_choice, result)
        
        if result == 'win':
            user_score += 1
        elif result == 'lose':
            computer_score += 1

        print(f"\nScores: You - {user_score} | Computer - {computer_score}")
        play_again = input("\nDo you want to play another round? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
