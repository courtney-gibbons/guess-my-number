from random import seed
from random import randint

#user guesses
def guess_my_number():
    seed(1)
    number = randint(1, 100)
    #print(number)
    guesses = 8
    while guesses > 1:
        print('You have', guesses, 'guesses left')
        guess = input('Guess my number! ')
        if int(guess) > int(number):
            print('Too high')
            print(' ')
        if int(guess) < int(number):
            print('Too low')
            print(' ')
        if int(guess) == int(number):
            print('You got it!')
            return None
        guesses = guesses - 1
    if guesses == 1:
        print('You have', guesses, 'guess left')
        guess = input('Guess my number! ')
        if int(guess) == int(number):
            print('You got it!')
            return None
        else: 
            print('Sorry, you have run out of guesses')
            return None
 
guess_my_number()

#computer guesses
def computer_guess_my_number():
    number = input('Input a number in between 1 and 100 ')
    guesses = input('How many guesses should the computer have? ')
    print(' ')
    min = 1
    max = 100
    while int(guesses) > 1:
        print('The computer has', guesses, 'guesses left')
        guess = min + int((max-min)/2)
        print('The computer guessed', guess)
        if int(guess) > int(number):
            print('Too high')
            print(' ')
            max = guess
        if int(guess) < int(number):
            print('Too low')
            print(' ')
            min = guess
        if int(guess) == int(number):
            print('The computer got it!')
            return None
        guesses = int(guesses) - 1
    if int(guesses) == 1:
        print('The computer has', guesses, 'guess left')
        guess = min + int((max-min)/2)
        print('The computer guessed', guess)
        if int(guess) == int(number):
            print('The computer got it!')
            return None
        else: 
            print('The computer could not guess your number')
            return None

#computer_guess_my_number()
