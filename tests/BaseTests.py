from endpoints.change_object import ChangeObject
from endpoints.create_object import CreateObject
from endpoints.get_object_by_id import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject


class BaseTest:
    create_endpoint = None
    get_endpoint = None
    change_endpoint = None
    update_endpoint = None
    delete_endpoint = None

    def setup_method(self):
        self.create_endpoint = CreateObject()
        self.get_endpoint = GetObject()
        self.change_endpoint = ChangeObject()
        self.update_endpoint = UpdateObject()
        self.delete_endpoint = DeleteObject()
