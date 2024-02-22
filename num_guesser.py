import random

print('welcome to NumGuess!')

upper_bound = input('Type a number: ')

if upper_bound.isdigit():
    upper_bound = int(upper_bound)

    if upper_bound <= 0:
        print('please type a number greater than 0')
        quit()
else:
    print('please type a number')
    quit()

random_num = random.randint(1, upper_bound)
guesses = 0

while True:
    user_guess = input("Make a guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number')
        continue

    guesses += 1

    if user_guess == random_num:
        print('You got it! The number was', user_guess)
        break
    elif user_guess > random_num:
        print('guess lower')
    else:
        print('guess higher')

print ('You got it in', guesses, 'guesses' )
