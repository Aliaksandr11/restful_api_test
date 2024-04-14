import pytest
from endpoints.create_object import CreateObject
from endpoints.delete_object import DeleteObject


@pytest.fixture(scope='function')
def obj_id():
    create_object = CreateObject()
    create_object.create_object()
    obj_id = create_object.response_json['id']
    yield obj_id
    DeleteObject().delete_object(obj_id)
