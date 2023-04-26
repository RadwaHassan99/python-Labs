import random

def guessing_game():
    number = random.randint(1, 100)
    
    tries = 10
    guessed_numbers = set()
    
    while tries > 0:
        guess = input(f"Guess a number between 1 and 100 (you have {tries} tries left): ")
        
        if not guess.isdigit() or int(guess) < 1 or int(guess) > 100:
            print("Invalid input. Please enter a number between 1 and 100.")
            continue
        
        if int(guess) in guessed_numbers:
            print("You have already guessed this number. Please try a different one.")
            continue
        
        guessed_numbers.add(int(guess))
        
        if int(guess) == number:
            print("Congratulations! You guessed the number!")
            play_again = input("Do you want to play again? (y/n): ")
            
            if play_again.lower() == "y":
                guessing_game()
            
            break
        
        if int(guess) < number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        
        tries -= 1
        
    else:
        play_again = input("You ran out of tries. Do you want to play again? (y/n): ")
        
        if play_again.lower() == "y":
            guessing_game()

guessing_game()
