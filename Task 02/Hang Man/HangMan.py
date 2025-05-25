import random
import os
import time

class HangmanGame:
    def __init__(self, words=None):
        
        self.default_words = [
            "python", "hangman", "computer", "programming", "algorithm",
            "developer", "interface", "database", "network", "security",
            "machine", "learning", "artificial", "intelligence", "software",
            "engineering", "framework", "library", "variable", "function",
            "keyboard", "monitor", "website", "internet", "browser"
        ]

        
        self.word_hints = {
            "python": "A popular programming language named after a snake",
            "hangman": "The name of this game you're playing",
            "computer": "Electronic device for processing data",
            "programming": "The process of writing code",
            "algorithm": "Step-by-step procedure to solve problems",
            "developer": "Person who creates software",
            "interface": "Where humans meet computers",
            "database": "Organized data storage",
            "network": "Connected computers sharing resources",
            "security": "Protection from unauthorized access",
            "machine": "Mechanical or electronic device",
            "learning": "Getting knowledge or skills",
            "artificial": "Made by humans, not natural",
            "intelligence": "Ability to learn and apply knowledge",
            "software": "Programs for computers",
            "engineering": "Applying science to build things",
            "framework": "Structure for software development",
            "library": "Collection of code resources",
            "variable": "Value that can change in code",
            "function": "Block of code that does a task",
            "keyboard": "Device to type input",
            "monitor": "Screen display",
            "website": "Pages on the internet",
            "internet": "Global network",
            "browser": "Software to access the web"
        }

        
        self.words = words if words else list(self.word_hints.keys())

        
        self.hangman_pics = [
            '''
              +---+
              |   |
                  |
                  |
                  |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
             /|\\  |
                  |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
             /|\\  |
             /    |
                  |
            =======''',
            '''
              +---+
              |   |
              O   |
             /|\\  |
             / \\  |
                  |
            ======='''
        ]

        self.start_new_game()

    def start_new_game(self):
        self.word = random.choice(self.words).lower()
        self.hint = self.word_hints.get(self.word, "No hint available")
        self.guessed_letters = set()
        self.wrong_guesses = 0
        self.max_wrong = len(self.hangman_pics) - 1
        self.game_over = False
        self.hint_used = False

    def show_game(self):
        
        os.system('cls' if os.name == 'nt' else 'clear')

        print("\n===== HANGMAN =====\n")
        print(self.hangman_pics[self.wrong_guesses])

        
        display_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print("\nWord: ", display_word)

        
        guessed = sorted(self.guessed_letters)
        print("\nGuessed letters: ", ", ".join(guessed) if guessed else "None")

        
        tries_left = self.max_wrong - self.wrong_guesses
        print(f"Remaining tries: {tries_left}")

        
        if self.hint_used:
            print("\nHint:", self.hint)
        else:
            print("\nType 'hint' for a hint (costs 1 try)")

    def check_guess(self, guess):
        guess = guess.lower()

        if self.game_over:
            return "The game is finished. Please start a new game."

        if guess == "hint":
            if self.hint_used:
                return "You already used the hint."
            self.hint_used = True
            self.wrong_guesses += 1
            if self.wrong_guesses >= self.max_wrong:
                self.game_over = True
                return f"Hint: {self.hint}\nNo tries left! The word was: {self.word}"
            return f"Hint: {self.hint}\n(This costs you 1 try)"

        if len(guess) != 1 or not guess.isalpha():
            return "Please enter a single letter."

        if guess in self.guessed_letters:
            return f"You already guessed '{guess}'. Try another letter."

        self.guessed_letters.add(guess)

        if guess in self.word:
            
            if all(letter in self.guessed_letters for letter in self.word):
                self.game_over = True
                return f"Congrats! You guessed the word: {self.word}"
            return f"Good job! '{guess}' is in the word."
        else:
            self.wrong_guesses += 1
            if self.wrong_guesses >= self.max_wrong:
                self.game_over = True
                return f"Game over! The word was: {self.word}"
            return f"Sorry, '{guess}' is not in the word."

    def play(self):
        print("\nWelcome to Hangman!")
        print("Guess the word one letter at a time.")
        print("Type 'exit' to quit or 'hint' to get a hint (costs 1 try).")

        playing = True
        while playing:
            self.start_new_game()

            while not self.game_over:
                self.show_game()
                guess = input("\nEnter a letter: ").strip()

                if guess.lower() == "exit":
                    print("Thanks for playing!")
                    return

                message = self.check_guess(guess)
                print(message)
                time.sleep(1)

            self.show_game()

            while True:
                again = input("\nPlay again? (y/n): ").strip().lower()
                if again == 'y':
                    break
                elif again == 'n':
                    playing = False
                    print("Thanks for playing!")
                    break
                else:
                    print("Please enter 'y' or 'n'.")

if __name__ == "__main__":
    game = HangmanGame()
    game.play()
