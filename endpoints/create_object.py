import requests
from endpoints.base_endpoint import EndPoint

class CreateObject(EndPoint):

    def new_object(self, payload):
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.response_json = self.response.json()
    
    def check_name(self, name):
        assert self.response_json['name'] == name
