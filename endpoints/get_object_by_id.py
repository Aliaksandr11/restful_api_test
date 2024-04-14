import allure
import requests
import logging
from endpoints.base_endpoints import BaseEndpoints

logging.getLogger(__name__)


class GetObject(BaseEndpoints):

    @allure.step('Send GET request')
    def get_obj(self, obj_id):
        logging.info(f'Get object id: {obj_id}')
        self.response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
        self.status_code = self.response.status_code

    @allure.step('Check the response object id')
    def check_object_id(self, obj_id):
        logging.info(f'Response object id: {self.response.json()['id']}. Request object {obj_id}')
        assert self.response.json()['id'] == obj_id
