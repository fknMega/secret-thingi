# Import utils
from utils.utils import send_message


# Import config.py
import config

# Import time
import time

# Import random
import random

# Import threading
import threading


def Main(ws):
    # Run code in a thread
    threading.Thread(target=Loop, args=(ws)).start()


def Loop(ws):
    # Send a message every x seconds
    while True:
        # Wait x seconds
        time.sleep(config.config["auto_market"]["time"])

        # Send a random message
        send_message(ws, random.choice(
            config.config["auto_market"]["messages"], 'market'))
