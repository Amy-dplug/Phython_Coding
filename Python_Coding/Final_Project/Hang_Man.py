import random

# Step 1: Word list
words = ["python", "coding", "hangman", "developer", "keyboard"]
word = random.choice(words)
guessed = []
wrong_guesses = 0
max_wrong = 6

# Step 2: Game loop
while True:
    # Step 3: Display word
    display = [letter if letter in guessed else "_" for letter in word]
    print("\nWord:", " ".join(display))

    # Step 4: Check for win
    if "_" not in display:
        print("🎉 You won!")
        break

    # Step 5: Get user input
    guess = input("Guess a letter: ").lower()

    # Step 6: Validate input
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue
    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    # Step 7: Check guess
    if guess not in word:
        wrong_guesses += 1
        print(f"❌ Wrong guess! ({wrong_guesses}/{max_wrong})")
        if wrong_guesses == max_wrong:
            print(f"💀 Game over! The word was '{word}'")
            break
