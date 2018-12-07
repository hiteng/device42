

import unittest
from unittest import TestCase
import rest_operations
from rest_operations import DeviceRequests
from mock import patch

class TestDevicePost(TestCase):


    @patch('rest_operations.DeviceRequests')
    def test_post_device(self, MockDeviceRequests):
        DeviceRequests = MockDeviceRequests()

        DeviceRequests.post_device.return_value = [{"code": 0}]
        response = DeviceRequests.post_device()
        self.assertIsNotNone(response)
        self.assertNotEqual(response, [{"code": 1}])

    @patch('rest_operations.DeviceRequests')
    def test_get_all_device(self, MockDeviceRequests):
        DeviceRequests = MockDeviceRequests
        DeviceRequests.get_all_device.return_value = [{"name": "abc", "type": "cluster", "service_level": "QA"}]
        response = DeviceRequests.get_all_device()
        self.assertEqual(response, [{"name": "abc", "type": "cluster", "service_level": "QA"}])

    @patch('rest_operations.DeviceRequests')
    def test_read_csv(self, MockDeviceRequests):
        DeviceRequests = MockDeviceRequests
        DeviceRequests.read_csv.return_value = DeviceRequests.read_csv()
        response = DeviceRequests.read_csv
        self.assertNotEqual(response, [{"name": "abc", "type": "cluster", "service_level": "QA"}])

    @patch('rest_operations.DeviceRequests.post_csv', return_value={"status_code": 200})
    def test_post_csv(self, MockDeviceRequests):
        DeviceRequests = MockDeviceRequests
        response = DeviceRequests.post_csv("dev10.csv")
        self.assertNotEqual(response, {"status_code": 200})






if __name__ == '__main__':


    unittest.main()

