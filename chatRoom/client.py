import threading
import socket
import tkinter
import time

# TKINTER INTERFACE 

amIAdmin = False


# Create Nickname window
window_login = tkinter.Tk()
window_login.title("Introduce your nickname")
window_login.eval('tk::PlaceWindow . center')

nickname_var = tkinter.StringVar()

# Enter your nickname
nickInput = tkinter.Entry(window_login, textvariable=nickname_var, width=50)
nickInput.grid(row=0, column=0, padx=10, pady= 10)

# Button for send nickname
btnSendMessage = tkinter.Button(window_login, text="Enter", width=20, command=window_login.destroy)
btnSendMessage.grid(row=1, column=0, padx=10, pady=10)

window_login.mainloop()

nickname = nickname_var.get()

# Create room window
window = tkinter.Tk()
window.title("Connected to localhost:58000")
window.eval('tk::PlaceWindow . center')

# Text box
txtMessages = tkinter.Text(window, width=50)
txtMessages.grid(row=1, column=0, padx=10, pady=10)

# Your message box
yourMessageLabl = tkinter.Label(window, text="Your message:").place(x=10, y=328)
txtYourMessage = tkinter.Entry(window, text="hola", width=50)
txtYourMessage.grid(row=2, column=0, padx=10, pady=10)

# See all nicknames on server



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 58000))

# Send messages to server
# I pass event as parameter to use the return key as sender 
def client_send(event=None):
    message = f'{nickname} : {txtYourMessage.get()}\n'
    client.send(message.encode('utf-8'))
    ########################################################## GAME ##########################################################
    if(message == f'{nickname} : #GAMESTART\n' and amIAdmin):
            client.send('Starting game...\n'.encode('utf-8'))

    else:
        if(amIAdmin and message == f'{nickname} : #GAMEEND\n'):
            client.send('Ending game...\n'.encode('utf-8'))
            
            



# Button for send message
btnSendMessage = tkinter.Button(window, text="Send", width=20, command=client_send)
btnSendMessage.grid(row=3, column=0, padx=10, pady=10)
window.bind('<Return>', client_send)


# Receive messages from server
def client_receive():
    while True:
        try:
            # Receive message from server
            message = client.recv(1024).decode('utf-8')
            #Check if I am the administrator
            if message == 'You are the administrator\n':
                global amIAdmin
                amIAdmin = True

            # Print message    
            print(message)
            txtMessages.insert(tkinter.END, message)
            txtYourMessage.delete(0, tkinter.END)

        except:
            # Close connection when error
            print('ERROR :(')
            client.close()
            break





# Start receiving and sending threads
receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()

window.mainloop()