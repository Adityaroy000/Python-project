import random

def play_game():
    number = random.randint(0, 100)
    count = 0
    NoOfGuesses = 0
    a = -1

    print("🎲 Welcome to the Perfect Guess Game!")
    print("🔹 Try to guess the number between 0 and 100.")

    while a != number:
        try:
            a = int(input("🔢 Enter your guess (or type -1 to exit): "))
            if a == -1:
                print("Thanks for playing!")
                return
            
            if a < 0 or a > 100:
                print("Please enter a number between 0 and 100.")
                continue
            
            NoOfGuesses += 1  # Increment guess count
            
            if a > number:
                print("📉 Too high! Try a lower number.")
            elif a < number:
                print("📈 Too low! Try a higher number.")
            else:
                print(f"🎉 Perfect Guess! You guessed it in {NoOfGuesses} attempts.")
                break  # Exit loop when guessed correctly
            
            if NoOfGuesses == 4:
                print("⚠️ You're taking more guesses than your friend. Try to guess quickly!")

        except ValueError:
            print("❌ Invalid input! Please enter a valid number.")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
