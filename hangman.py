import random

def hangman():
    words = ["python", "coding", "hangman", "game", "random"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        display_word = "".join([letter if letter in guessed_letters else "_" for letter in word])
        print("\nWord:", display_word)

        if display_word == word:
            print("🎉 Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single alphabet letter.")
            continue
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            attempts -= 1
            print(f"❌ Wrong! Attempts left: {attempts}")

    if attempts == 0:
        print("\n💀 Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
