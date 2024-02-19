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