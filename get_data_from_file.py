import re


def get_job_position(string):
    return string[4] if string[4] != '' else None


def get_full_name(string):
    return re.findall(r"\w+", str(string))[0:3]


def get_organization(string):
    return re.findall(r"\w+", str(string))[3]


def get_phone_number(string):
    phone_template = r'(\+7|8)\s*?[\(\s]?(\d{3})[\)\s]?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})(\s+?\(?доб\.\s+?\)?)?(\d*)?\s?\)?(\d+)?\)?'
    find_phone = re.findall(phone_template, str(string))
    if not find_phone:
        return None
    else:
        ph_nb = list(find_phone[0])
        if ph_nb[-2] == '':
            return f'+7({ph_nb[1]}){ph_nb[2]}-{ph_nb[3]}-{ph_nb[4]}'
        else:
            return f'+7({ph_nb[1]}){ph_nb[2]}-{ph_nb[3]}-{ph_nb[4]} доб.{ph_nb[6]}'


def get_email(string):
    template_email = r"\w+\@\w+\.\w+"
    find_email = re.findall(template_email, str(string))
    return find_email[0] if find_email else None



