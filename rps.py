import random 

user_wins = 0
computer_wins = 0

options = ['rock','paper','scissors']

while True:
    user_input = input('Type Rock/Paper/Scissors or Q to quit: ').lower()
    if user_input == 'q':
        quit()

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    comp_pick = options[random_number]

    print("Bot picked {comp_pick}")

print('Goodbye!')