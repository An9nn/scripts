import random, string, os

os.system('clear')
pass_amount = int(input('Enter many passwords you want to generate: '))
pass_length = int(input('Enter password length: '))

chars = string.ascii_letters + string.digits + string.punctuation
os.system('clear')
for im in range(pass_amount): # index amount
    password = ''

    for il in range(pass_length): # index length
        password = password + random.choice(chars)

    print('Password {} > {}'.format(im, password)) # result