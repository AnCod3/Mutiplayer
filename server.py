
import socket
from _thread import *
from game import Game
import pickle


#using your local host server
#add by finding your ipconfig
server = '192.168.0.27'
port = 5555
#types of connections
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#test connection by using try and except
try:
    s.bind((server, port))

except socket.error as e:
    str(e)
#opens the port adding a nargument will limit the amount of connections
#if left blank it will leave unlimited connections
s.listen(2)
print('waitinf for connection, Server started')

#instead of one game this will have a dictionary of games
#each game will have their own id

#stores id of connected clients
connected = set()
#store our game ids
games = {}
idCount = 0
def threaded_client(conn, p, gameId):
    #keeps track of our Id count
    #for instance if someone leaves the game
    #the gameID count will grop
    global idCount
    #notify the player which player they are 1 or 2
    conn.send(str.encode(str(p)))

    reply = ""
    while True:
        try:
            #send get reset or move
            #get =  get game (get from client)
            #reset = finish game start over (get from client)
            #player makes move and sends to server if valid data will be sent back
            #increase limit data in case it's too large
            data = conn.recv(4096).decode()
            #check  if game session is still valid incase player disconnects
            if gameId in games:
                game = games[gameId]

                if not data:
                    break
                else:
                    if data == "reset":
                        game.resetWent()
                    elif data != "get":
                        game.play(p, data)


                #sends game back to client
                #reply = game
                    conn.sendall(pickle.dumps(game))
            else:
                break

        except:
            break
    #if something happens then the game gets closed.
    print("lost Connection")


    try:
        del games[gameId]
        print("closing game ", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

while True:
    #if connection is made then the connection and the address will be stored
    conn, addr = s.accept()
    print('Connected to ', addr)
    #here we will create games

    idCount += 1
    p = 0
    #everytime two clients connect to server
    #the game id gets incremented by one
    gameId = (idCount - 1)//2
    #if there are an odd number of players a new games/session has to be created
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creatring a new Game")
    else:
        #another player has conenct to the game
        #a new session can start
        games[gameId].ready = True
        p = 1

    #this will start the thread but normally we would have to wait for the thread to excute
    #before a conenction is made
    #the while loop will continue to run without waiting for the thread to complete and runs in the backround
    start_new_thread(threaded_client, (conn, p, gameId))


