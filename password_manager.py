
## encryption to txt
from cryptography.fernet import Fernet


active = True

## Creating new key
def write_key():
    key = Fernet.generate_key()
    with open('key.key' , 'wb') as key_file:
        key_file.write(key)

## Loading key
def load_key():
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key

def view():
    ## shows user and password line by line
    with open('passwords.txt', 'r') as file:
        for line in file.readlines():
            data = line.rstrip()
            user , passww = data.split('|')
            print(f"User: {user} - Password: {fer.decrypt(passww.encode()).decode()}")

def add():
    name = input("Enter your name: ")
    password = input("Enter your password: ")
    ##place where file opens and users name , password writes
    with open('passwords.txt' , 'a') as file:
        encrypted_password = fer.encrypt(password.encode()).decode()
        file.write(name + '|' + encrypted_password + '\n')
    print(f"Password for {name} has been added.")


master_password = input("Enter master password: ")

## If there are already key it takes that else it creates a new one
try:
    key = load_key()
except FileNotFoundError:
    print("⚠ Key file not found! Generating new key...")
    write_key()
    key = load_key()

fer = Fernet(key)
## main loop
while active:
    print("===========================")
    print("1.View")
    print("2.Add")
    print("3.Exit")
    print("===========================")
    mode = int(input("Enter mode: "))

    if mode == 3:
        active = False
        print("Thank you for using")

    elif mode == 1:
        view()
    elif mode == 2:
        add()
    else:
        print("Invalid mode")
        continue
