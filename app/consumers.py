from channels.generic.websocket import WebsocketConsumer
import json

class EchoConsumer(WebsocketConsumer):
    
    def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        obj = json.loads(text_data)
        print('received :', obj)

        json_string = json.dumps({
            "content": obj["content"],
            "user": obj["user"],
        })

        self.send(json_string)