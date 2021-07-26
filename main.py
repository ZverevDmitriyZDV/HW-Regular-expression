from format_dict import *
from format_file import *

if __name__ == '__main__':

    try:
        contacts_list = get_data()
        head_file = contacts_list.pop(0)
        head_file[-1] = head_file[-1].replace(';', '')
        result_dict = create_dict(contacts_list)
        format_list = format_dict_to_export(result_dict, head_file)
        put_data(format_list)
        print('Создание файла завершено успешно')

    except:
        print('Ошибка записи')
