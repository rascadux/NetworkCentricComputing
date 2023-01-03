import random

words = ['apple', 'banana', 'orange', 'strawberry', 'grape', 'blueberry', 'melon', 'lemon', 'lime', 'coconut', 'apricot', 'watermelon', 'peach', 'cherry', 'pineapple', 'kiwi', 'mango', 'papaya', 'pear', 'peanut']

word = random.choice(words)

firstLetter = False
guesses = ''
fails = 0
end = False


def showLetter():
    for char in word[random.randint(0, len(word)-1)]:
        global guesses
        if(char not in guesses):
            guesses += char
            break
        else:
            showLetter()



def runGame():

    global guesses, fails, firstLetter, end


    if firstLetter == False:
        showLetter()
        firstLetter = True

    while end != True:

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
            print('\nYou win!')
            print('The word is: ', word)
            break

        print()
        print('Guess a character: ')
        guess = input("")


        guesses += guess

        if guess not in word:
            fails += 1
            print('Wrong')
            print('You have failed ', + fails, ' times')


