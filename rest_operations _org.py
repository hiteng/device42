

import csv
import os
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



class DeviceRequests(object):

    base_url = 'https://10.0.0.16/api/1.0/'

    def __init__(self, username, password, url, entity, field, inp_file):

        self.username = username
        self.password = password
        self.url = url
        self.entity = entity
        self.field = field
        self.inp_file = inp_file



        self.url = os.path.join(self.base_url, self.entity, "")

    def controller(self):
        lst_devices = self.read_csv()
        for device in lst_devices:
            response = self.get_device(device.get('name'))
            print response.json()
            if response.status_code == 200:
                if not self.compare_data(device, response.json()):
                    self.update_device(device.get('name'), device)
            else:
                self.post_device(device)
        return True


    def compare_data(self, csv_data, get_data):

        for i in csv_data:
            if i and csv_data.get(i) != get_data.get(i):
                return False
        return True


    def update_device_exist(self, device_name):
        """Check if the input device exists
           if it does not exist, post the device
           else return exists msg
           """
        try:
            self.url = os.path.join(self.base_url, self.entity, self.field, device_name)
            response = requests.get(self.url, auth=(self.username, self.password), verify=False).content
        except requests.exceptions.ConnectionError as e:
            print e
            return False

        y = json.loads(response)
        if y.get('code') == 1:
            post_device = self.post_req({"name": device_name})
            return post_device
        else:
            device_exist = self.get_req(device_name)
            print device_exist


    def get_device(self, device_name): #GET from device42 DB
        try:
            self.url = os.path.join(self.base_url, self.entity, self.field, str(device_name))
            response = requests.get(self.url, auth=(self.username, self.password), verify=False)
        except requests.exceptions.ConnectionError as e:
            print e
            return {"msg": "Failed to get entity"}
        return response

    def read_csv(self):  #GET from CSV file
        with open(self.inp_file, 'rU') as csvDataFile:
            csvReader = csv.DictReader(csvDataFile)
            return list(csvReader)

    def post_device(self, payload):  #payload = Hard code
        try:
            self.url = os.path.join(self.base_url, self.entity, "")
            response = requests.post(self.url, auth=(self.username, self.password), data=payload, verify=False).content
        except requests.exceptions.ConnectionError as e:
            print e
            return {"msg": "Failed to create the entity"}
        return response

    def post_csv(self):  #POST from CSV file
        with open(self.inp_file, 'rU') as csvDataFile:
            csvReader = csv.DictReader(csvDataFile)
            for row in csvReader:
                data = row
                try:
                    url = os.path.join(self.base_url, self.entity, "")
                    response = requests.post(url, auth=(self.username, self.password), data=data, verify=False)
                    if response.status_code != 200:
                        raise Exception("wrong status code")
                except requests.exceptions.ConnectionError as e:
                    return {"msg": "Failed to create the entity", "exception": e}
            return True

    def update_device(self, device_name, payload):
        try:
            self.url = self.base_url + self.entity +'/'
            print self.url
            response = requests.put(self.url, auth=(self.username, self.password), data=payload, verify=False).content
        except requests.exceptions.ConnectionError as e:
            print e
            return {"msg": "Failed to update the entity"}
        return response




if __name__ == '__main__':


    payload = {"name": "db-095-westport",
               "type": "cluster",
               "in_service": "yes",
               "virtual_host": "yui",
               "service_level": "QA",
               "macaddress": "aabbccedffff"}

    obj = DeviceRequests('admin', 'hiten3', 'url', 'devices', 'name', 'device 2.csv')
    print obj.controller()










