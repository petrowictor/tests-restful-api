import requests
from endpoints.base_endpoint import EndPoint

class DeleteObject(EndPoint):
    
    def delete_by_id(self, object_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{object_id}')
        self.response_json = self.response.json()
