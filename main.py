import json
import re

import websocket

import config

tr = config.triger_and_respond


def on_message(ws: websocket.WebSocket, message):
    print(message.content)
    



def on_pong(wsapp, message):
    print("Got a pong! No need to respond")
    wsapp.send('2')


wsapp = websocket.WebSocketApp(
    f'wss://yelling.cc/socket.io/?token={config.config["ws_token"]}&EIO=3&transport=websocket',
    on_message=on_message,
    on_pong=on_pong)
wsapp.run_forever(ping_timeout=20, ping_interval=25, ping_payload='2')

def checkIfKiss(message):
    if message['type'] == 'kiss':
        return True
    else:
        return False
