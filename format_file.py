import csv


def get_data():
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        return list(rows)


def put_data(list_for_input):
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(list_for_input)