import time

remind = input('Hi Im RemindBot. What should I remind you about? ')

min = float(input('In how many minutes? '))

sec = min * 60

time.sleep(sec)

print(remind)

