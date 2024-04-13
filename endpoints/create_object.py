import requests
import allure
from endpoints.base_endpoints import BaseEndpoints
from endpoints.json_schemas import CheckSchemasPost

PAYLOAD = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.98,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}


class CreateObject(BaseEndpoints):

    @allure.step('Send POST request')
    def create_object(self, payload=None):
        payload = payload if payload else PAYLOAD
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check the response name')
    def resp_name_is_req_name(self, name):
        assert self.response.json()['name'] == name

    @allure.step('Check JSON Schema')
    def check_json_schema(self):
        CheckSchemasPost(**self.response_json)
