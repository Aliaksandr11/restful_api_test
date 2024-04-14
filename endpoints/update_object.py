import allure
import requests
from endpoints.base_endpoints import BaseEndpoints

PAYLOAD = {
    "name": "Apple MacBook Pro 17",
    "data": {
        "year": 2020
    }
}


class UpdateObject(BaseEndpoints):
    @allure.step('Send PATCH request')
    def update_object(self, obj_id, payload=None):
        payload = payload if payload else PAYLOAD
        self.response = requests.patch(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check the response name')
    def check_name(self, name):
        assert self.response_json['name'] == name

    @allure.step('Check the response year')
    def check_year(self, year):
        assert self.response_json['data']['year'] == year
