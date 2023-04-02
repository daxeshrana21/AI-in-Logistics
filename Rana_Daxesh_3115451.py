# used to generate random number
import random
# used to measured time
import time
# used to plays sound when user lose or win the game
import winsound

def play_game():
# displaying game instructions
    print("Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the number.")
    print("Type 'quit' to exit the game.")
    print("Let's begin!")
    time.sleep(2)

    # generating random number between 1 and 100
    num_to_guess = random.randint(1, 100)
    attempts = 0
    high_score = {'score': 0, 'name': None}

    # measuring the start time
    start_time = time.time()

    # while loop for getting user input and comparing it with the random number
    while attempts < 10:
        attempts += 1
        guess = input("Guess #{}: ".format(attempts))

        # checking if the user wants to quit the game
        if guess.lower() == 'quit':
            print("Thanks for playing! Goodbye.")
            return

        # converting user input to integer
        guess = int(guess)

        # Comparing user input with the random number
        if guess == num_to_guess:

        # measuring the end time and calculating total time taken to guess the number    
            end_time = time.time()
            total_time = round(end_time - start_time, 2)
            print("Wow Congratulations! You guessed the number in {} attempts and {} seconds.".format(attempts, total_time))
            if high_score['score'] == 0 or attempts < high_score['score']:
                high_score['score'] = attempts
                high_score['name'] = input("Enter your name: ")
                print("You Achive a New high score: {} attempts by {}!".format(high_score['score'], high_score['name']))
            # playing win sound
            winsound.PlaySound("win.wav", winsound.SND_ASYNC)
            break
        elif guess < num_to_guess:
            print("Ohh no Too low!Guess again")
            # playing wrong guess sound
            winsound.PlaySound("wrong.wav", winsound.SND_ASYNC)
        else:
            print("Ohh no Too high!Guess agin")
            # playing wrong guess sound
            winsound.PlaySound("wrong.wav", winsound.SND_ASYNC)
    
    # checking if the user has run out of attempts
    if attempts == 10:
        print("Sorry, you've run out of attempts. The number was {}.".format(num_to_guess))
        winsound.PlaySound("lose.wav", winsound.SND_ASYNC)

    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() == "y":
        # calling the play_game function again to start a new game
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

play_game()
