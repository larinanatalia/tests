from ad_py.Test.data import documents, directories

def person(num_doc):
    for data_doc in documents:
        if num_doc == data_doc['number']:
            return data_doc['name']


def shelf_num(num_shelf):
    count = 0
    for data_doc in documents:
        if num_shelf == data_doc['number']:
            count += 1
            for key, value in directories.items():
                for values in value:
                    if num_shelf == values:
                        answer = key
        if count == 0:
            answer = 'Такого документа нет'
    return answer


def list_documents():
    for data_doc in documents:
        return (f'''{data_doc['type']} "{data_doc['number']}" "{data_doc['name']}" ''')


def add_doc(new_type,new_number,new_name,shelf_num):
    new_dict = {"type": 0, "number": 0, "number": 0}
    new_dict["type"] = str(new_type)
    new_dict["number"] = str(new_number)
    new_dict["name"] = str(new_name)
    documents.append(new_dict)
    if shelf_num in directories:
        directories[shelf_num].append(new_number)
    else:
        directories[shelf_num] = directories.get(shelf_num, [str(new_number)])
    return documents, directories

def delete_doc(del_doc):
    count = 0
    for data_doc in documents:
        if del_doc in data_doc.values():
            count += 1
            data_doc.clear()
            print(documents)
    for key, value in directories.items():
        if del_doc in value:
            value.remove(del_doc)
            print(directories)
    if count == 0:
        print('Такого документа не существует')


def move_doc(num_doc,new_sh):
    count = 0
    for data_doc in documents:
        if num_doc in data_doc["number"]:
            count += 1
    if count == 1:
        for key, value in directories.items():
            if num_doc in value:
                value.remove(num_doc)
                new_directories = dict()
        if new_sh in directories:
            directories[new_sh].append(num_doc)
        else:
            directories[new_sh] = directories.get(new_sh, [str(num_doc)])
        print(directories)
    else:
        print('Такого документа не существует')
    return directories


def add_shelf(new_sh):
    if new_sh in directories:
        new_sh = 1
    else:
        directories[new_sh] = directories.get(new_sh, [])
    return directories

