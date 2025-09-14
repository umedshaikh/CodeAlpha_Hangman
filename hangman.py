import random
from colorama import Fore, Style

def save_score(name, attempts):
    with open("scores.txt", "a") as file:
        file.write(f"{name}:{attempts}\n")

def show_scores():
    try:
        with open("scores.txt", "r") as file:
            lines = file.readlines()
            scores = []
            for line in lines:
                name, attempt = line.strip().split(":")
                scores.append((name, int(attempt)))

            # Sort by attempts left in descending order
            scores = sorted(scores, key=lambda x: x[1], reverse=True)

            print(Fore.MAGENTA + "\n--- High Scores ---" + Style.RESET_ALL)
            for idx, (name, attempt) in enumerate(scores[:3], 1):
                print(f"{idx}. {name} - Attempts left: {attempt}")

    except FileNotFoundError:
        print(Fore.MAGENTA + "No scores yet. Play a game to create high scores!" + Style.RESET_ALL)

def hangman():
    print(Fore.CYAN + "Welcome to the Advanced Hangman Game!" + Style.RESET_ALL)
    
    show_scores()
    # Word categories
    categories = {
        "fruits": ["apple", "banana", "cherry", "orange", "grape"],
        "animals": ["tiger", "elephant", "giraffe", "monkey", "panda"],
        "countries": ["india", "brazil", "canada", "france", "japan"]
    }

    print("Choose a category:")
    for index, cat in enumerate(categories.keys(), 1):
        print(f"{index}. {cat.capitalize()}")

    choice = input("Enter the category number: ")
    try:
        choice = int(choice)
        selected_category = list(categories.keys())[choice - 1]
    except:
        print("Invalid choice! Defaulting to fruits.")
        selected_category = "fruits"

    word_list = categories[selected_category]
    word = random.choice(word_list)

    guessed = ["_"] * len(word)
    attempts = 6
    guessed_letters = set()

    print(f"\nCategory selected: {selected_category.capitalize()}")
    print("Word to guess:", " ".join(guessed))

    # ASCII hangman stages
    hangman_stages = [
        """
           -----
           |   |
               |
               |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
               |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========""",
        """
           -----
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        ========="""
    ]

    while attempts > 0 and "_" in guessed:
        print(hangman_stages[6 - attempts])
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print(Fore.YELLOW + "Please enter a single letter." + Style.RESET_ALL)
            continue

        if guess in guessed_letters:
            print(Fore.YELLOW + "You already guessed that letter." + Style.RESET_ALL)
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(Fore.GREEN + "Good guess!" + Style.RESET_ALL)
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
        else:
            print(Fore.RED + "Wrong guess!" + Style.RESET_ALL)
            attempts -= 1

        print("Word:", " ".join(guessed))
        print(f"Attempts left: {attempts}\n")

    if "_" not in guessed:
        print(Fore.GREEN + "Congratulations! You guessed the word:" + word + Style.RESET_ALL)
    else:
        print(Fore.RED + "Game over! The word was:" + word + Style.RESET_ALL)
    
    name = input("Enter your name to save your score: ")
    save_score(name, attempts)


    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again.startswith('y'):
        hangman()

if __name__ == "__main__":
    hangman()
    

