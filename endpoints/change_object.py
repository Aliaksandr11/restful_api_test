import allure
import requests
from endpoints.base_endpoints import BaseEndpoints


class ChangeObject(BaseEndpoints):
    @allure.step('Send PUT request')
    def change_object(self, obj_id, payload):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check the response name')
    def check_name(self, name):
        assert self.response_json['name'] == name

    @allure.step('Check the response year')
    def check_year(self, year):
        assert self.response_json['data']['year'] == year

    @allure.step('Check the response price')
    def check_price(self, price):
        assert self.response_json['data']['price'] == price
