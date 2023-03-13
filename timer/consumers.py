import json
from time import sleep
from random import randint

from channels.generic.websocket import WebsocketConsumer

class TimerConsumer(WebsocketConsumer):
    
    def connect(self):
        self.accept()
        
        for i in range(1000):
            self.send(json.dumps({
                "message": randint(1, 100),
            }))
            sleep(1)