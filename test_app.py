from ad_py.Test.application import person, shelf_num, list_documents, add_doc, delete_doc, add_shelf
from ad_py.Test.data import documents, directories


class Test_comand:
    def setup(self):
        pass
    def test_person(self):
        assert person('10006') == "Аристарх Павлов"
    def test_shelf_num(self):
        assert  shelf_num('2207 876234') == '1'
    def test_list_documents(self):
        assert list_documents() and "Геннадий Покемонов",'2207 876234'
    def test_add_doc(self):
        add_doc('passport', '1212121', 'Test name', '1')
        assert '1212121' in documents[-1]["number"]
    def test_delete_doc(self):
        assert delete_doc('11-2') not in documents
    def test_add_shelf(self):
        assert add_shelf('5') is directories
    def teardown(self):
        pass
