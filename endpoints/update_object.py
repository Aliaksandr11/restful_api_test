import allure
import requests
from endpoints.base_endpoints import BaseEndpoints


class UpdateObject(BaseEndpoints):
    @allure.step('Send PATCH request')
    def update_object(self, obj_id, payload):
        self.response = requests.patch(f'https://api.restful-api.dev/objects/{obj_id}', json=payload)
        self.status_code = self.response.status_code
        self.response_json = self.response.json()

    @allure.step('Check the response name')
    def check_resp_name_is_req_name(self, name):
        assert self.response_json['name'] == name
