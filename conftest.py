import pytest
from test_API_altsvetkov.endpoints.create_object import CreateObject
from test_API_altsvetkov.endpoints.delete_object import DeleteObject


@pytest.fixture()
def obj_id():
    create_object = CreateObject()
    create_object.create_object()
    obj_id = create_object.response_json['id']
    yield obj_id
    delete_object = DeleteObject()
    delete_object.delete_object(obj_id)
