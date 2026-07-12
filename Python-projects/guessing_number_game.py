import random

def get_user_guess() -> int:
    """Responsible only for getting and validating user input."""
    while True:
        try:
            return int(input("Enter your guess (between 1 and 100): "))
        except ValueError:
            print("⚠️ Invalid input! Please enter a valid integer.")

def check_guess(guess: int, secret_number: int) -> bool:
    """Responsible only for comparing the guess and providing feedback."""
    if guess < secret_number:
        print("❌ Too Low! Try a higher number ⬆️\n")
        return False
    elif guess > secret_number:
        print("❌ Too High! Try a lower number ⬇️\n")
        return False
    else:
        return True

def play_game():
    """Main function: Responsible only for managing the game flow and attempts."""
    print("=" * 50)
    print("🎯 Welcome to the Number Guessing Game (SRP) 🎯")
    print("=" * 50)
    print("The computer has chosen a number between 1 and 100.")
    print("Try to guess it in the fewest attempts possible.\n")
    
    secret_number = random.randint(1, 100)
    attempts = 0
    is_game_over = False
    
    while not is_game_over:
        guess = get_user_guess()
        attempts += 1
        is_game_over = check_guess(guess, secret_number)
    
    # Win message after breaking the loop
    print("=" * 50)
    print("🎉 Congratulations! You won! 🥳🥳")
    print(f"You guessed the secret number [{secret_number}] in {attempts} attempts!")
    print("=" * 50)

if __name__ == "__main__":
    play_game()