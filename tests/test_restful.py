import pytest
import allure
from BaseTests import BaseTest


class TestRestful(BaseTest):
    @allure.title('Create object test')
    @allure.story('Create object')
    @allure.feature('CRUD operations')
    @pytest.mark.critical
    def test_create_object(self, obj_id):
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        self.create_endpoint.create_object(payload)
        self.create_endpoint.check_status_code_is_200()
        self.create_endpoint.check_name(payload['name'])
        self.create_endpoint.check_price(payload['data']['price'])
        self.create_endpoint.check_year(payload['data']['year'])

    @allure.title('Get object by id test')
    @allure.story('Get object by id')
    @allure.feature('CRUD operations')
    def test_get_object_by_id(self, obj_id):
        self.get_endpoint.get_obj(obj_id)
        self.get_endpoint.check_status_code_is_200()
        self.get_endpoint.check_object_id(obj_id)

    @allure.title('Change object test')
    @allure.story('Change object')
    @allure.feature('CRUD operations')
    @pytest.mark.parametrize('name, year, price', [
        ('Apple MacBook Pro 16', 2020, 2000.00),
        ('Apple MacBook Pro 16', 2021, 2500.99),
        ('Apple MacBook Pro 16', 2022, 3000)])
    @pytest.mark.critical
    def test_put_object(self, obj_id, name, year, price):
        payload = {
            "name": name,
            "data": {
                "year": year,
                "price": price,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        self.change_endpoint.change_object(obj_id, payload)
        self.change_endpoint.check_status_code_is_200()
        self.change_endpoint.check_name(name)
        self.change_endpoint.check_year(year)
        self.change_endpoint.check_price(price)

    @allure.title('Update object test')
    @allure.story('Update object')
    @allure.feature('CRUD operations')
    def test_patch_object(self, obj_id):
        payload = {
            "name": "Apple MacBook Pro 17",
            "data": {
                "year": 2020
            }
        }
        self.update_endpoint.update_object(obj_id, payload)
        self.update_endpoint.check_status_code_is_200()
        self.update_endpoint.check_name(payload['name'])
        self.update_endpoint.check_year(payload['data']['year'])

    @allure.title('Delete object test')
    @allure.story('Delete object')
    @allure.feature('CRUD operations')
    def test_delete_object(self, obj_id):
        self.delete_endpoint.delete_object(obj_id)
        self.delete_endpoint.check_status_code_is_200()
        self.delete_endpoint.check_delete_schema()
        self.delete_endpoint.check_message(obj_id)
        self.get_endpoint.get_obj(obj_id)
        self.get_endpoint.check_status_code_is_404()

    @allure.title('End-to-end test')
    def test_end_to_end(self, obj_id):

        self.create_endpoint.create_object()
        self.create_endpoint.check_status_code_is_200()
        self.create_endpoint.check_name('Apple MacBook Pro 16')

        self.get_endpoint.get_obj(obj_id)
        self.get_endpoint.check_status_code_is_200()
        self.get_endpoint.check_object_id(obj_id)

        self.update_endpoint.update_object(obj_id)
        self.update_endpoint.check_year(2020)

        self.delete_endpoint.delete_object(obj_id)
        self.delete_endpoint.check_status_code_is_200()
        self.delete_endpoint.check_delete_schema()
        self.delete_endpoint.check_message(obj_id)
        self.get_endpoint.get_obj(obj_id)
        self.get_endpoint.check_status_code_is_404()
