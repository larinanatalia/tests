import requests
import json
from ad_py.Test.new_folder import new_folder

class Test_command:
    def setup(self):
        pass
    def test_status_201(self):
        assert new_folder('test_folder').status_code == 201

    def test_name_of_folder_on_disk(self):
        new_folder('test_folder')
        headers = {'Authorization': '+++++++++++++++++++++++'}
        params_folder = {'path': 'test_folder'}
        requests.put('https://cloud-api.yandex.net/v1/disk/resources/publish', headers=headers, params=params_folder)
        resp =requests.get('https://cloud-api.yandex.net/v1/disk/resources/public',
                     headers=headers)
        response = resp.json()
        name_list = []
        for i in response['items']:
            name_list.append(i['name'])
        assert 'test_folder' in name_list

    def teardown(self):
        headers = {'Authorization': '++++++++++++++++++++++++++++++++'}
        params_folder = {'path': 'test_folder'}
        requests.delete('https://cloud-api.yandex.net/v1/disk/resources',
                     headers=headers, params=params_folder)

