import csv
import json


def FirstCsvToJson(csvFilePath, jsonFilePath):
    data = {}
    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)

        for rows in csvReader:
            key = rows['id']
            data[key] = rows
        with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(data, indent=4))


csvFilePath = r'books.csv'
jsonFilePath = r'books.json'

FirstCsvToJson(csvFilePath, jsonFilePath)
