import random
from tqdm import tqdm
import time
import os

def gameStart():
    os.system('cls')
    print("Welcome to the Number Guessing Game!\n")
    print("Here's how to play:\n")
    print("1. Set Your Challenge: You will be asked to enter the maximum number for the game. The secret number will be randomly chosen from 1 up to (and including) the number you select. Keep in mind that a larger range will make the game more challenging!\n")
    print("2. Guess Wisely: After the system prepares a secret number, you will start guessing.\n")
    print("3. Helpful Hints: Based on your guesses and the maximum number you chose, the system will provide hints to guide you:\n")
    print("   * Extremely High/Low: Your guess is significantly higher or lower than the secret number.")
    print("   * Too High/Low: Your guess is considerably higher or lower than the secret number.")
    print("   * High/Low: Your guess is higher or lower than the secret number.")
    print("   * Slightly High/Low: Your guess is just a bit higher or lower than the secret number.")
    print("   * Very Close: You are very near the secret number!\n")
    print("4. The Importance of Attempts: The game keeps track of how many guesses it takes you to find the correct number. Try to guess it in as few attempts as possible!\n")
    print("Good luck and have fun!\n")

    def get_difficulty():
        print("Choose difficulty level:")
        print("1. Easy (1-50)")
        print("2. Medium (1-250)")
        print("3. Hard (1-500)")
        while True:
            try:
                choice = int(input("> "))
                if choice == 1:
                    return 50
                elif choice == 2:
                    return 250
                elif choice == 3:
                    return 500
                else:
                    print("Invalid choice. Please enter 1, 2, or 3.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def get_max_number():
        while True:
            try:
                print("\nPlease enter the maximum number for the game (or choose difficulty above):")
                max_num_input = input("> ")
                if not max_num_input:  # Handle empty input in case difficulty was chosen
                    return None
                max_number = int(max_num_input)
                if max_number <= 0:
                    print("Please enter a positive number.")
                else:
                    return max_number
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    max_number = get_difficulty()
    if max_number is None:
        max_number = get_max_number()
        if max_number is None: # Handle if user still gives invalid input
            print("Invalid maximum number. Exiting game.")
            return

    max_attempts = int(max_number**0.5) + 5 # Adjusted attempts based on range
    extremely_range = max_number // 2
    too_range = max_number // 4
    normal_range = max_number // 8
    slightly_range = max_number // 16

    rangestring = f"""
    Hint Ranges (based on max number {max_number}):
    Extreme: Greater than or equal to {extremely_range} away
    Too: Between {too_range} and {extremely_range - 1} away
    Normal: Between {normal_range} and {too_range - 1} away
    Slightly: Between {slightly_range} and {normal_range - 1} away
    Very close: Less than {slightly_range} away
    """
    print(rangestring)
    print("Preparing a number -- \n")
    for i in tqdm(range(30)):  # Reduced progress bar duration
        time.sleep(0.02)
    realnumb = random.randint(1, max_number)
    # print(f"The real number is {realnumb}") # Removed revealing the number

    attempt = 0
    while attempt < max_attempts:
        try:
            userguess = int(input(f"\nEnter your guess (Attempt {attempt + 1}/{max_attempts})> "))
            attempt += 1

            if userguess < 1 or userguess > max_number:
                print(f"Your guess is out of the valid range (1 to {max_number}). Please try again.")
                continue

            if userguess == realnumb:
                print(f"That's it! You guessed the number {realnumb} correctly in {attempt} attempts!\n")
                break
            else:
                difference = abs(userguess - realnumb)
                if difference >= extremely_range:
                    print(f"{userguess} is extremely {'high' if userguess > realnumb else 'low'}.")
                elif difference >= too_range:
                    print(f"{userguess} is too {'high' if userguess > realnumb else 'low'}.")
                elif difference >= normal_range:
                    print(f"{userguess} is {'high' if userguess > realnumb else 'low'}.")
                elif difference >= slightly_range:
                    print(f"{userguess} is slightly {'high' if userguess > realnumb else 'low'}.")
                else:
                    print(f"{userguess} is very close!")

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if attempt == max_attempts and userguess != realnumb:
        print(f"\nYou ran out of attempts! The correct number was {realnumb}.\n")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        gameStart()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    gameStart()