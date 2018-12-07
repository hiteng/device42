


import csv
import requests
import os


def insert_update_devices(inp_csv_file_name):
    with open(inp_csv_file_name, 'rU') as csvDataFile:
        csvReader = csv.DictReader(csvDataFile)
        #next(csvReader)
        for column in csvReader:
            print column
            result = column
            base_url = 'https://10.0.0.125/api/1.0/'
            username = 'admin'
            password ='hiten3'
            payload = result
            try:
                url = os.path.join(base_url, entity, "")
                response = requests.post(url, auth=(username, password), data=payload, verify=False).content

            except requests.exceptions.ConnectionError as e:
                print e
                return {"msg": "Failed to create the entity"}
                return response









if __name__ == '__main__':

    entity = 'devices'
    print insert_update_devices("device_csv.csv")


