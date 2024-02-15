print('Welcome to HistQuiz, A History Quiz Game!')

count = 0

playing = input('Would you like to play? ')

if playing != 'yes': 
    quit()

print('Lets begin!')

ans = input('In what year did the United States declare its independence from Great Britain? ')

if ans == '1776':
    print('correct!')
    count += 1
else:
    print('incorrect')

ans = input('When did the Treaty of Versailles officially end World War I? ')

if ans == '1919':
    print('correct!')
    count += 1
else:
    print('incorrect')

ans = input('When did the Berlin Wall fall, leading to the reunification of East and West Germany? ')

if ans == '1989':
    print('correct!')
    count += 1
else:
    print('incorrect')

print()




