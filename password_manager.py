master_pwd = input('what is the master password? ')

def view():
    pass

def add():
    name  = input('Account name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(f'{name} | {pwd}')

while True:
    mode = input('would you like to add a new password or view existing ones (view, add)? to quit press q ').lower()

    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('invalid mode')
        continue
