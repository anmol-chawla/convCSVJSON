import jstyleson
import csv

def jsonToCSV(obj_json):
    obj_csv = open("users.csv", 'w')
    file_json = jstyleson.load(obj_json, )
    headers = []
    item = file_json[0]
    for keys in item.keys():
        headers.append(keys)
    writer_csv = csv.DictWriter(obj_csv, headers)
    writer_csv.writeheader()
    for item in file_json:
        writer_csv.writerow(item)
    obj_csv.close()


def CSVToJSON(obj_csv):
    obj_json = open("users1.json", 'w')
    csv_reader = csv.DictReader(obj_csv)
    fields = csv_reader.fieldnames
    items = []
    item = {}
    for row in csv_reader:
        for field in fields:
            item[field] = row[field]
        items.append(dict(item))
    jstyleson.dump(items, obj_json, indent=4)
    obj_json.close()



obj_json = open("users.json")
jsonToCSV(obj_json)
obj_json.close()
obj_csv = open("users.csv", 'r')
CSVToJSON(obj_csv)
obj_csv.close()
