import uuid


class Port:

    @staticmethod
    def create_id():
        id = str(uuid.uuid4())
        return id

    def __init__(self):
        self.id = Port.create_id()
        self.occupied = False
        self.injected_cable = ''

    def port_occupation(self, cable):
        self.occupied = True
        self.injected_cable = cable
