import pytest
import allure
from endpoints.change_object import ChangeObject
from endpoints.create_object import CreateObject
from endpoints.get_object_by_id import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject


@allure.title('Create object test')
@allure.story('Create object')
@allure.feature('CRUD operations')
@pytest.mark.critical
def test_create_object():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }

    create_object = CreateObject()
    create_object.create_object(payload)
    create_object.check_status_code_is_200()
    create_object.resp_name_is_req_name(payload['name'])
    create_object.check_json_schema()


@allure.title('Get object by id test')
@allure.story('Get object by id')
@allure.feature('CRUD operations')
def test_get_object_by_id(obj_id):
    get_object = GetObject()
    get_object.get_obj(obj_id)
    get_object.check_status_code_is_200()
    get_object.check_object_id(obj_id)


@allure.title('Change object test')
@allure.story('Change object')
@allure.feature('CRUD operations')
@pytest.mark.parametrize('name, year, price', [
    ('Apple MacBook Pro 16', 2020, 2000.00),
    ('Apple MacBook Pro 16', 2021, 2500.99),
    ('Apple MacBook Pro 16', 2022, 3000)])
@pytest.mark.critical
def test_put_object(obj_id, name, year, price):
    change_object = ChangeObject()
    change_object.change_object(obj_id, name, year, price)
    change_object.check_status_code_is_200()
    change_object.resp_name_is_req_name(name)
    change_object.resp_year_is_req_year(year)


@allure.title('Update object test')
@allure.story('Update object')
@allure.feature('CRUD operations')
def test_patch_object(obj_id):
    payload = {
        "name": "Apple MacBook Pro 17",
        "data": {
            "year": 2020
        }
    }
    update_object = UpdateObject()
    update_object.update_object(obj_id, payload)
    update_object.check_status_code_is_200()
    update_object.check_resp_name_is_req_name(payload['name'])


@allure.title('Delete object test')
@allure.story('Delete object')
@allure.feature('CRUD operations')
def test_delete_object(obj_id):
    delete_object = DeleteObject()
    delete_object.delete_object(obj_id)
    delete_object.check_status_code_is_200()
    get_object = GetObject()
    get_object.get_obj(obj_id)
    get_object.check_status_code_is_404()
    delete_object.check_json_schemas()
    delete_object.message_verification(obj_id)
