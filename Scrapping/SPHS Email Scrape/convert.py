import csv
import json
import re

path = 'output_type_2.json'
csvName = 'idk'

with open(path) as f:
    data = json.load(f)
    headers = data[0].keys()

    staffList = []
    for item in data:
        emailStart = item['email'].split('@')[0]
        if re.search('[0-9]', emailStart) == None: #student match
            continue
            print('student: ', emailStart)
        else: #Staff Match
            staffList.append(item)
            # print('staff: ', emailStart)
    
    data = staffList

    with open(csvName + '.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(data)
