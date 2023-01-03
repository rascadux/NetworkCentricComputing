'''
TODO:
Add private text messages (Pasar los nicknames a client.py)

Add admin privileges

Add game
'''

import threading
import socket
from colorama import Fore, Back, Style
import time
import random
import tkinter
from io import StringIO
import sys

host = 'localhost'
port = 58000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []
administrator = None


# Broadcast messages to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

######################################################## GAME CODE ########################################################


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

    #create new window
    window1 = tkinter.Tk()
    window1.title("Game player")
    window1.eval('tk::PlaceWindow . center')

    guessLabel = tkinter.Label(window1, text="Your guess:").place(x=10, y=328)
    txtGuess = tkinter.Entry(window1, width=50)
    txtGuess.grid(row=2, column=0, padx=10, pady=10)

    txtGame = tkinter.Text(window1, width=50)
    txtGame.grid(row=1, column=0, padx=10, pady=10)

    guessLabel = tkinter.Label(window1, text="Your message:").place(x=10, y=328)
    txtGuess = tkinter.Entry(window1, width=50)
    txtGuess.grid(row=2, column=0, padx=10, pady=10)

    btnSendMessage = tkinter.Button(window1, text="Send", width=20, command=guessSender)
    btnSendMessage.grid(row=3, column=0, padx=10, pady=10)

    def guessSender(event=None):
        guess1 = txtGuess.get()

    ### GAME CREATION ###
    global guesses, fails, firstLetter, end
    s = StringIO()


    if firstLetter == False:
        showLetter()
        firstLetter = True

    while end != True:

        if fails == 3:
            showLetter()
            fails = 0

        failed = 0

        for char in word:

            buffer = StringIO()
            sys.stdout = buffer

            if char in guesses:
                print(char, end=' ')
                string = buffer.getvalue()

                sys.stdout = sys.__stdout__

                broadcast(string.encode('utf-8'))

            else: 
                print('_', end=' ')
                string = buffer.getvalue()

                sys.stdout = sys.__stdout__

                broadcast(string.encode('utf-8'))
                failed += 1


        if failed == 0:
            broadcast('\nYou win!'.encode('utf-8'))
            broadcast('The word is: ' + word)
            break

        broadcast('\n'.encode('utf-8'))
        broadcast('Guess a character: \n'.encode('utf-8'))
        #INSTEAD OF INPUT, NEED TO RECEIVE FROM CLIENT
        guess = txtGuess.get()
        


        guesses += guess

        if guess not in word:
            fails += 1
            broadcast('Wrong')
            broadcast('You have failed ', + fails, ' times')

    window1.mainloop()

######################################################## GAME CODE ########################################################


# Handle messages from clients
def handle_client(client):
    while True:
        try:
            # Broadcast messages
            nickname = nicknames[clients.index(client)]
            message = client.recv(1024)
            message = message.decode('utf-8')
            if(client == clients[0] and message == f'{nickname} : #GAMESTART\n'):
                broadcast('Game starting...\n'.encode('utf-8')) 
                runGame()
            else:
                broadcast(message.encode('utf-8'))
        except:
            # Remove and close clients that disconnect
            adminChange = False
            if(administrator == client):
                adminChange = True
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat\n'.encode('utf-8'))
            if(adminChange):
                clients[0].send('You are the new administrator\n'.encode('utf-8'))
            nicknames.remove(nickname)
            break

# Receive / broadcast messages
def receive():
    print(Fore.MAGENTA + 'Server listening...' + Style.RESET_ALL)
    while True:
        if(len(clients) == 1):
            global administrator 
            administrator = clients[0]
            time.sleep(0.5)
            administrator.send('You are the administrator\n'.encode('utf-8'))

        # Accept connection
        client, address = server.accept()
        print(f'Connection established with {str(address)}')

        # Request and store nickname
        nickname = client.recv(1024).decode('utf-8')
        # Remove the ': \n' from the nickname
        nickname = nickname[:-4]

        nicknames.append(nickname)
        clients.append(client)

        # Print and broadcast nickname
        print(' The nickname of the client is ' + Fore.GREEN + f'{nickname}' + Style.RESET_ALL)
        client.send('Now connected to the server\n'.encode('utf-8'))
        broadcast(f'{nickname} has joined the chat \n'.encode('utf-8'))

        # Start handling thread for client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

if __name__ == '__main__':
    receive()


