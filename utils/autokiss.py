import random
import threading
import time

# Import config.py
import config

# Import utils
from utils.utils import send_message


def checkIfKiss(message):
    # Check if the message is a kiss

    # Check if message contains :kiss:
    if ":kiss:" in message:
        # Check if you get pinged
        if "@" + config.config["username"] in message:
            return True
    return False


def Main(ws, msg, author):
    # check if kiss
    if checkIfKiss(msg):
        # Run code in a thread
        threading.Thread(target=ReturnKiss, args=(ws, author)).start()
       

        return True

    else:
       return False


def ReturnKiss(ws, author):
    print("Got a kiss!")

    # wait btw x and y seconds from config
    time.sleep(random.randint(config.config["auto_kiss"]["delay_from"], config.config["auto_kiss"]["delay_to"]))

    send_message(ws, "@" + author + " :kiss:")
