from cryptography.fernet import Fernet

master_pwd = input('what is the master password? ')

def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print (f'User: {user} Password: {passw}')

def add():
    name  = input('Account name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        f.write(f'{name} | {pwd}')

while True:
    mode = input('would you like to add a new password or view existing ones (view, add)? to quit press q').lower()

    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('invalid mode')
        continue
