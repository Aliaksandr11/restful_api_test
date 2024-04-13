import allure
import requests
from endpoints.base_endpoints import BaseEndpoints


class ChangeObject(BaseEndpoints):
    @allure.step('Send PUT request')
    def change_object(self, obj_id, name, year, price):
        payload = {
            "name": name,
            "data": {
                "year": year,
                "price": price,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        self.response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check the response name')
    def resp_name_is_req_name(self, name):
        assert self.response_json['name'] == name

    @allure.step('Check the response year')
    def resp_year_is_req_year(self, year):
        assert self.response_json['data']['year'] == year
