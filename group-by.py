import json

def file_reader(path):
    with open(path, 'r') as file_obj:
        return json.load(file_obj)

def group_by(data_list, filter):
    grouped_data = {}
    filter_list = []
    for d in data_list:
        if d[filter] not in filter_list:
            filter_list.append(d[filter])
            temp_list = []
            temp_list.append(d)
            grouped_data[d[filter]] = temp_list
        else:
            grouped_data[d[filter]].append(d)

    return grouped_data

data = file_reader(r"C:\Users\abdul\OneDrive\Desktop\trainings\python-programming\prime-number\places.json")

grouped_data = group_by(data, "country")


def show_grouped_data(grouped_data):
    
    for gd in grouped_data:
        print("Key:", gd)
        print("Data: ", grouped_data.get(gd))
        print()

show_grouped_data(grouped_data)

