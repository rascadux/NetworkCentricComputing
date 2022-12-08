import random

words = ['apple', 'banana', 'orange', 'strawberry', 'grape', 'blueberry', 'melon', 'lemon', 'lime', 'coconut', 'apricot', 'watermelon', 'peach', 'cherry', 'pineapple', 'kiwi', 'mango', 'papaya', 'pear', 'peanut']


word = random.choice(words)

firstLetter = False
guesses = ''
fails = 0

def showLetter():
    for char in word[random.randint(0, len(word)-1)]:
        global guesses
        if(char not in guesses):
            guesses += char
            break
        else:
            showLetter()

if firstLetter == False:
    showLetter()
    firstLetter = True

turns = 20

while turns > 0:

    if fails == 3:
        showLetter()
        fails = 0

    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=' ')

        else:
            print('_', end=' ')
            failed += 1

    if failed == 0:
        print('You win!')
        print('The word is: ', word)
        break

    print()
    guess = input("Guess a character: ")

    guesses += guess

    if guess not in word:
        turns -= 1
        fails += 1
        print('Wrong')
        print('You have', + turns, 'more guesses')
        print('You have failed ', + fails, ' times')

        if turns == 0:
            print('You lose')

