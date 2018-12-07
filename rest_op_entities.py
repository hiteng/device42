
def get_rack(self):
    try:
        self.url = os.path.join(self.base_url, self.entity, "")
        response = requests.get(self.url, auth=(self.username, self.password), verify=False)
    except requests.exceptions.ConnectionError as e:
        print e
        return {"msg": "Failed to get a Rack"}
    return response.json()

def post_rack(self, payload):
    try:
        url = os.path.join(self.base_url, self.entity, "")
        response = requests.post(url, auth=(self.username, self.password), data=payload, verify=False).content
    except requests.exceptions.ConnectionError as e:
        print e
        return {"msg": "Failed to get a Room"}
    return response

def get_room(self):
    try:
        self.url = os.path.join(self.base_url, self.entity, "")
        response = requests.get(self.url, auth=(self.username, self.password), verify=False)
    except requests.exceptions.ConnectionError as e:
        print e
        return {"msg": "Failed to get a Rack"}
    return response.json()

def post_room(self, payload):
    try:
        url = os.path.join(self.base_url, self.entity, "")
        response = requests.post(url, auth=(self.username, self.password), data=payload, verify=False).content
    except requests.exceptions.ConnectionError as e:
        print e
        return {"msg": "Failed to get a Room"}
    return response
def get_building(self):
    try:
        self.url = os.path.join(self.base_url, self.entity, "")
        response = requests.get(self.url, auth=(self.username, self.password), verify=False)
    except requests.exceptions.ConnectionError as e:
        print e
        return {"msg": "Failed to get a Rack"}
    return response.json()

def post_building(self, payload_building):
    try:
        url = os.path.join(self.base_url, self.entity, "")
        response = requests.post(url, auth=(self.username, self.password), data=payload_building, verify=False).content
    except requests.exceptions.ConnectionError as e:
        print e
        return {"msg": "Failed to get a Building"}
    return response



if __name__ == '__main__':
    payload_rack = {"name": 11, "size": 42, "room_id": 7, "numbering_start_from_bottom": "no", "first_number": 4,
                    "row": 12, "manufacturer": "apc", "notes": "ujwgyd"}

    payload_room = {"name": "room12", "building": "test building", "notes": "ejgf"}

    payload_building = {"name": "hit1", "address": "ljdhbfjd", "notes": "khkn"}

    # obj1 = DeviceRequests('admin', 'hiten3', 'racks', 'all')
    # print obj1.get_rack()

    # obj2 = DeviceRequests('admin', 'hiten3', 'racks', 'all')
    # print obj2.post_rack(payload_rack)

    # obj3 = DeviceRequests('admin', 'hiten3', 'rooms', 'all')
    # print obj3.get_room()
    #
    # obj4 = DeviceRequests('admin', 'hiten3', 'rooms', 'all')
    # print obj4.post_room(payload_room)

    # obj5 = DeviceRequests('admin', 'hiten3', 'buildings', 'all')
    # print obj5.get_building()

    # obj6 = DeviceRequests('admin', 'hiten3', 'buildings', 'all')
    # print obj6.post_building(payload_building)