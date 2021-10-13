import random

number = random.randint(1, 10)
print(f'Random: {number}')
guess_list = []

while True:
    # print('Enter a number:')
    guess = input('Enter a number: ')
    if guess.isnumeric():
        if guess not in guess_list:
            guess_list.append(guess)
        if int(guess) == number:
            break
        else:
            print('Wrong guess, try again')
            print(f'Wrong guesses: {guess_list}')
    else:
        print('Only numbers, try again')
        print(f'Wrong guesses: {", ".join(x for x in guess_list)}')

print('You guessed it')
