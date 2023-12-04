import uuid


class Cable:

    @staticmethod
    def create_id():
        id = str(uuid.uuid4())
        return id

    def __init__(self):
        self.id = Cable.create_id()
        self.port_list = []
        self.pc_list = []
        self.fully_occupied = False

    def set_port(self, port):
        self.port_list.append(port)

    def add_connected_pc(self, pc):
        self.check_occupation()
        if not self.fully_occupied:
            self.pc_list.append(pc)

    def check_occupation(self):
        if len(self.pc_list) == 2:
            self.fully_occupied = True
