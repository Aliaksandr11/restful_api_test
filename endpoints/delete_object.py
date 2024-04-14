import allure
import requests
from endpoints.base_endpoints import BaseEndpoints
from endpoints.json_schemas import CheckSchemasDelete


class DeleteObject(BaseEndpoints):

    @allure.step('Send DELETE request')
    def delete_object(self, obj_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
        self.response_json = self.response.json()
        self.status_code = self.response.status_code

    @allure.step('Check the response message')
    def check_message(self, obj_id):
        assert self.response_json['message'] == f"Object with id = {obj_id} has been deleted."

    @allure.step('Check the response object id')
    def check_object_id(self, obj_id):
        assert self.response_json['id'] == obj_id

    def check_delete_schema(self):
        assert CheckSchemasDelete(**self.response_json)
