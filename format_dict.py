from get_data_from_file import *


def check_clone(dict_input, key_word, insert_result):
    if dict_input.get(key_word) is None:
        dict_input[key_word] = insert_result
    pass


def create_dict_elem(raw, result_dict):
    job = get_job_position(raw)
    lastname, firstname, surname = get_full_name(raw)
    organization = get_organization(raw)
    reformat_ph_nb = get_phone_number(raw)
    email = get_email(raw)
    name_surname = f'{lastname}, {firstname}'
    if result_dict.get(name_surname) is None:
        result_string = {
            'lastname': lastname,
            'surname': surname,
            'firstname': firstname,
            'phone': reformat_ph_nb,
            'organization': organization,
            'email': email,
            'position': job
        }
        result_dict[name_surname] = result_string
    else:
        insert_dict = result_dict[name_surname]
        check_clone(insert_dict, 'phone', reformat_ph_nb)
        check_clone(insert_dict, 'organization', organization)
        check_clone(insert_dict, 'email', email)
        check_clone(insert_dict, 'position', job)
    return result_dict


def create_dict(list_input):
    format_dict = dict()
    for elem in list_input:
        create_dict_elem(elem, format_dict)
    return format_dict


def format_dict_to_export(dict_for_format, template_head):
    format_list = list()
    for key in dict_for_format.keys():
        format_string = ''
        dict_output = dict_for_format[key]
        for i in range(0, len(template_head) - 1):
            format_string += f"{dict_output[f'{template_head[i]}']}, "
        format_string += f"{dict_output[f'{template_head[-1]}']};"
        format_list.append([format_string])
    return format_list



