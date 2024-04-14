import allure


class BaseEndpoints:
    status_code = None
    response = None
    response_json = None
    object_id = None
    schema_post = None
    schema_delete = None

    @allure.step('Check status code is 200')
    def check_status_code_is_200(self):
        assert self.status_code == 200

    @allure.step('Check status code is 404')
    def check_status_code_is_404(self):
        assert self.status_code == 404
