# Import config.py
import random
import threading
import time
import config
from utils.utils import send_message



def returnHello(ws, author):
    

    # wait delay from config
    time.sleep(config.config["auto_hello"]["delay"])

    # Pick a random response from the list and replace {ping} with the author
    send_message(ws, random.choice(
        config.config["auto_hello"]["responses"]).replace("{ping}", "@" + author))

    return

def Main(ws, msg, author):
    # Check if the message is contains one of the hello words
        if any(' ' + word + ' ' in ' ' + msg.lower() + ' ' for word in config.config["auto_hello"]["hellos"]):
            # Run code in a thread
            threading.Thread(target=returnHello, args=(ws, author)).start()
            return True
        else:
            return False

            

