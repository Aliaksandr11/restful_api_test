import allure
import requests
from endpoints.base_endpoints import BaseEndpoints
from endpoints.json_schemas import CheckSchemasDelete


class DeleteObject(BaseEndpoints):
    # message = {
    #     "message": "Object with id = 6, has been deleted."
    # }
    @allure.step('Send DELETE request')
    def delete_object(self, obj_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
        self.response_json = self.response.json()
        self.status_code = self.response.status_code

    @allure.step('Check JSON Schema')
    def check_json_schemas(self):
        CheckSchemasDelete(**self.response_json)

    def message_verification(self, obj_id):
        assert self.response_json['message'] == f"Object with id = {obj_id} has been deleted."
