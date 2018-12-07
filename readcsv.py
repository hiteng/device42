
import csv
# from rest_operations import *
# import requests
#
#
#
# class CsvFile(DeviceRequests):
#
#     def __init__(self, payload):
#         self.payload = payload
#         super(CsvFile, self).__init__()

def insert_update_devices(inp_csv_file_name):

    with open(inp_csv_file_name, 'rU') as csvDataFile:
        csvReader = csv.DictReader(csvDataFile)
        #next(csvReader)
        return csvReader


if __name__ == '__main__':

    print insert_update_devices("device10.csv")

    #
    # def post_req(self, payload):
    #     try:
    #         self.url = os.path.join(self.base_url, self.entity, "")
    #         self.payload = "post_csv.csv"
    #         response = requests.post(self.url, auth=(self.username, self.password), data=self.payload, verify=False).content
    #     except requests.exceptions.ConnectionError as e:
    #         print e
    #         return {"msg": "Failed to create the entity"}
    #     return response




