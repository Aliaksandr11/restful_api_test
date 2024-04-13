import allure
import requests
from endpoints.base_endpoints import BaseEndpoints


class GetObject(BaseEndpoints):
    obj_id = None

    @allure.step('Send GET request')
    def get_obj(self, obj_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
        self.status_code = self.response.status_code

    @allure.step('Check the response object id')
    def check_object_id(self, obj_id):
        assert self.response.json()['id'] == obj_id
        self.obj_id = obj_id
