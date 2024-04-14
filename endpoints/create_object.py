import requests
import allure
import logging
from endpoints.base_endpoints import BaseEndpoints
from endpoints.json_schemas import CheckSchemasPost

logging.getLogger(__name__)


PAYLOAD = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}

HEADERS = {'Content-Type': 'application/json'}


# сделать проверку на статус код 400

class CreateObject(BaseEndpoints):

    @allure.step('Send POST request')
    def create_object(self, payload=None, headers=None):
        payload = payload if payload else PAYLOAD
        headers = headers if headers else HEADERS
        logging.info(f'Object creation payload: {payload}')
        self.response = requests.post('https://api.restful-api.dev/objects', json=payload, headers=headers)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()
        self.schema_post = CheckSchemasPost(**self.response_json)

    @allure.step('Check the response name')
    def check_name(self, name):
        assert self.schema_post.name == name

    @allure.step('Check the response year')
    def check_year(self, year):
        assert self.schema_post.data.year == year

    def check_price(self, price):
        assert self.schema_post.data.price == price
