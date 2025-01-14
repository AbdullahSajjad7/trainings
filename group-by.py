import json

def file_reader(path):
    """
    This function will read the data from json file
    """
    try:
        with open(path, 'r') as file_obj:
            return json.load(file_obj)
    except:
        print(FileNotFoundError)

def group_by(data_list, filter):
    """
    This function will filter the data based on the key/filter passed
    """
    try:
        grouped_data = {}
        for d in data_list:
            if d[filter] not in grouped_data:
                temp_list = []
                temp_list.append(d)
                grouped_data[d[filter]] = temp_list
            else:
                grouped_data[d[filter]].append(d)

        return grouped_data
    except:
        raise ValueError("Correct filter is not passed")


def show_grouped_data(grouped_data): 
    """
    This function shows the grouped data in readable form
    """
    for item in grouped_data:
        print("Key:", item)
        print("Data: ", grouped_data.get(item))
        print()

data = file_reader(r"C:\Users\abdul\OneDrive\Desktop\trainings\python-programming\prime-number\places.json")

grouped_data = group_by(data, "country")

show_grouped_data(grouped_data)

