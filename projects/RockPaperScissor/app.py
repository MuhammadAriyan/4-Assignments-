import random as rd

choices = ['r','p', 's']
compChoice = rd.choice(choices)

print('Welcome to the Rock, Paper, Scissors game!')
print('You will play against the computer.')
print('Select one of the following options:')
print('Rock (r)\n Paper (p)\n Scissor(s)')
user_input = input('Enter your choice: ').lower()

if user_input not in choices:
    print('Invalid input. Please try again.')
elif user_input == compChoice:
    print(f'You both chose {user_input}. It\'s a tie!')
elif (user_input == 'r' and compChoice == 's') or (user_input == 'p' and compChoice == 'r') or (user_input == 's' and compChoice == 'p'):
    print(f'You chose {user_input} and the computer chose {compChoice}. You win!')
else:
    print(f'You chose {user_input} and the computer chose {compChoice}. You lose!')
    