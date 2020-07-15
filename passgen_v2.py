import secrets
import string

lenght = int(input('Password lenght: '))
num = int(input('How many passwords you need?: '))

def pwd():
    alphabet = string.ascii_letters + string.digits 
    password = ''.join(secrets.choice(alphabet) for i in range(lenght))
    print(password)

while num > 0:
    pwd()
    num = num - 1
