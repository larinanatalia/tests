import  requests

def new_folder(folder_name):
    headers = {'Authorization': '++++++++++++++++++++++++++++++++'}
    params_folder = {'path': folder_name}
    resp_folder = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                               headers=headers, params=params_folder)
    return resp_folder

def new_folder_negative():
    headers = {'Authorization': '++++++++++++++++++++++++++++'}
    params_folder = {'path': folder_name}
    resp_folder = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                               headers=headers, params=params_folder)
    return resp_folder
