import random 


def guessing_game():

    """
    Generate a random number between 1 and 100.
    Give the user 7 attempts to guess it.
    After each guess, tell them "Too high!" or "Too low!".
    Track the number of attempts used.
    If they guess correctly: print a congratulations message with attempts used.
    If they use all 7 attempts: reveal the answer.
    Use the while loop with else clause.
    """

    answer = random.randint(1, 100)
    attempts = 0

    while attempts < 7:
        
        guess = int(input("Guess the number (1-100): "))
    
        attempts += 1

        if guess == answer:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess > answer:
            print("Too high!")
        else:
            print("Too low!")
    else:
        print(f"Out of attempts. The correct number was {answer}.")

    
        
guessing_game()




