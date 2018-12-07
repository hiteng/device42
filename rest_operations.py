

import csv
import os
import sys
import requests
import json
import urllib3
import glob
import shutil
import datetime
#import pandas as pd
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import ConfigParser


class DeviceRequests(object):


    def __init__(self, username, password, entity, field):

        self.username = username
        self.password = password
        self.entity = entity
        self.field = field

        config = ConfigParser.ConfigParser()
        config.readfp(open(r'config.ini'))
        self.base_url = config.get('Path', 'base_url')
        self.dir_loc = config.get('Path', 'dir_path')
        self.src_loc = config.get('Path', 'src_loc')
        self.dest_loc = config.get('Path', 'dest_loc')

    def controller(self, dir_name):
        """

        :param dir_name: Directory name
        :return: List of .csv files in the input Directory name.
        Iterate through each returned file and input the file name
        into update_post_check
        """
        file_names = self.get_csv_from_dir(dir_name)
        for each_file in file_names:
            self.update_post_check(each_file)




    def get_csv_from_dir(self, dir_name):
        '''
        :param dir_name: Directory Name
        :return: List of files with .csv format.
        Each file is opened to check if its empty.
        1. If empty return Empty msg else
        2. Extract the file names from the path and
        store as a list in list_filtered_filenames
        '''
        path = os.path.join(self.dir_loc, dir_name, "*.csv")
        list_filtered_filenames  = []
        for file_path in glob.glob(path):
            with open(file_path, 'rU') as csvDataFile:
                csvReader = csv.DictReader(csvDataFile)
                if len(list(csvReader)) == 0:
                    print {"msg": "Empty File"}
                else:
                    file_name = os.path.basename(file_path)
                    list_filtered_filenames.append(file_name)
        return list_filtered_filenames


    def update_post_check(self, csv_inp_file):
        """
        :param csv_inp_file: FileName.csv
        :return: Update device42 or Post to device42
        Read the csv file and compare the devices with a list
        of existing devices in device42.
        1. Compare the fields of the device if it already exists
         in device42- Update else
        2. Post the device
        """
        lst_devices = self.read_csv(csv_inp_file)
        response = self.get_all_device()
        res_list = []
        res = response['Devices']
        for devices in res:
            res_list.append(devices)
        device_names = []
        for x in res_list:
            device_names.append(x.get('name'))
        with open('data.json', 'w') as out_file:
            json.dump(res_list, out_file)
        with open('data.json', 'r') as json_read:
            data = json.load(json_read)


        for device in lst_devices:
            for dev in data:
                if device.get('name') == dev.get('name'):
                    if not self.compare_data(device, dev):
                        self.update_device(device)
                    else:
                        self.post_device(device)

            return True #self.processed_file(csv_inp_file)
        return True


    def processed_file(self, processed_file):
        if processed_file.endswith(".csv"):
            time_stamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
            source_loc = os.path.join(self.src_loc, processed_file)
            dest_loc = os.path.join(self.dest_loc, processed_file + time_stamp)
            shutil.move(source_loc, dest_loc)
            print {"msg": "File moved to Processed Files Directory"}
        else:
            print {"msg": "The file is processed already"}



    def compare_data(self, csv_data, get_data):
        for i in csv_data:
            if i and csv_data.get(i) != get_data.get(i):
                return False
        return True

    def get_all_device(self): #GET from device42 DB
        try:
            url = os.path.join(self.base_url, self.entity, self.field, "")
            response = requests.get(url, auth=(self.username, self.password), verify=False)
        except requests.exceptions.ConnectionError as e:
            print e
            return {"msg": "Failed to get entity"}
        return response.json()

    def read_csv(self, csv_inp_file):  #GET from CSV file
        lst_devices = []
        with open(csv_inp_file, 'rU') as csvDataFile:
            csvReader = csv.DictReader(csvDataFile)
            csv_file = list(csvReader)
            for row_data in csv_file:
                lst_devices.append(row_data)
            return lst_devices


    def post_device(self, payload):  #payload = Hard code
        try:
            url = os.path.join(self.base_url, self.entity, "")
            response = requests.post(url, auth=(self.username, self.password), data=payload, verify=False).content
            print response
        except requests.exceptions.ConnectionError as e:
            print e
            return {"msg": "Failed to create the entity"}
        return response

    def post_csv(self, csv_inp_file):  #POST from CSV file
        with open(csv_inp_file, 'rU') as csvDataFile:
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

    def update_device(self, payload):
        try:
            url = os.path.join(self.base_url, "device", "")
            response = requests.put(url, auth=(self.username, self.password), data=payload, verify=False).content
            print response
        except requests.exceptions.ConnectionError as e:
            print e
            return {"msg": "Failed to update the entity"}
        return response


if __name__ == '__main__':


    #paylaod = {"name=dev22&in_service=yes&service_level=Production"}

    # payload = {"name": "dev10", "type": "cluster", "in_service": "yes", "virtual_host": "yui",
    #            "service_level": "production"}
    #
    # payload1 = (name=dev22, type=physical, service_level=QA)
    #             #{"name": "dev22", "type": "physical", "service level": "QA"}


    # obj = DeviceRequests('admin', 'hiten3', 'devices', 'all')
    # a = obj.read_csv("dev10.csv")
    # for i in a:
    #     print i

    obj = DeviceRequests('admin', 'hiten3', 'devices', 'all')
    obj.update_post_check("dev22.csv")

    # obj7 = DeviceRequests('admin', 'hiten3', 'buildings', 'all')
    # print obj7.get_csv_from_dir("device42test")

    # obj = DeviceRequests('admin', 'hiten3', 'devices', 'all')
    # obj.read_csv("dev10.csv")

    # obj = DeviceRequests('admin', 'hiten3', 'devices', 'all')
    # obj.controller("device42test")

    # obj = DeviceRequests('admin', 'hiten3', 'device', 'all')
    # obj.update_device(payload)



    # obj = DeviceRequests('admin', 'hiten3', 'devices', 'all')
    # print obj.get_all_device()

    # obj = DeviceRequests('admin', 'hiten3', 'device', 'all')
    # obj.post_device(name='dev22', type='physical', service_level='QA')























