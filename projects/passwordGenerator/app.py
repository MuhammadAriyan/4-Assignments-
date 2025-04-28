import random as rd

def genPass():
    password = ''
    for i in range(12):
        password += rd.choice(chars)
    return password


print('Password Generator')

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+'
numberOfPasswords = int(input('How many passwords do you want to generate? '))

for i in range(numberOfPasswords):
    print('Password', i + 1, ':', genPass())