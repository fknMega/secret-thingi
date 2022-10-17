import json
import random
import re
import threading
import requests

import websocket
import time
import config
import utils.autokiss
import utils.utils
import utils.autohello



def on_message(ws: websocket.WebSocket, message):
    # Check if room is main
    data = json.loads(message[2:])
    if data[1]['room'] != 'main':
        return


    msg = data[1]['message']['content']

    # get the user avatar
    user_avatar = data[1]['message']['avatar']



    # Get the message author
    author = re.sub('<[^<]+?>', '', data[1]['message']['username'])


    # parse out html elements from the msg and keep only the text
    msg = re.sub('<[^<]+?>', '', msg)

    # Check if line reader is enabled
    if config.config["line_reader"]["enabled"]:
         if author == config.config["username"]:
             if msg == config.config["line_reader"]["command"]:
                    #send every line from lines.txt
                    with open(config.config["line_reader"]["file"]) as f:
                      for line in f:
                          utils.utils.send_message(ws, line)
                          time.sleep(config.config["line_reader"]["delay"])

    
    if author == config.config['username']:
        return

    print(msg)




    # Message is 'msg'
    # Author is 'author'

    # Autokiss
    if config.config["auto_kiss"]["enabled"] and author != config.config["username"]:
        # Check if the message is a kiss
        if utils.autokiss.Main(ws, msg, author):
            return



    



    # Auto hello
    if config.config["auto_hello"]["enabled"] and author != config.config["username"]:
        # Check if the message is contains one of the hello words
        if utils.autohello.Main(ws, msg, author):
            return
        



def on_pong(wsapp, message):
    print("Got a pong! No need to respond")
    wsapp.send('2')


def onclose():
    print("Connection closed! ")


def autoMessage(ws):
    # Start a loop
    while True:
        # Send a random message from the list
        utils.utils.send_message(ws, random.choice(
            config.config["auto_message"]["messages"]))

        # Wait for the time
        time.sleep(config.config["auto_message"]["time"])


def onopen(ws):
    print("Connection opened! ")


    # Auto Message
    if config.config["auto_message"]["enabled"]:
      # Start a background thread for auto Message
       threading.Thread(target=autoMessage, args=(ws,)).start()

    # Auto Market
    if config.config["auto_market"]["enabled"]:
        # Start a background thread for auto Market
        import utils.market
        utils.market.Main(ws)


wsapp = websocket.WebSocketApp(
    f'wss://yelling.cc/socket.io/?token={config.config["ws_token"]}&EIO=3&transport=websocket',
    on_message=on_message,
    on_pong=on_pong,
    on_close=onclose,
    on_open=onopen
)
wsapp.run_forever(ping_timeout=20, ping_interval=25, ping_payload='2')
