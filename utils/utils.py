import json


def send_message(ws, msg, room='main'):
    ws.send('42' + json.dumps([2, {'message': msg, 'room': room}]))

