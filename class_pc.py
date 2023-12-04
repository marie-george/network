import uuid


class Pc:

    @staticmethod
    def create_id():
        id = str(uuid.uuid4())
        return id

    def __init__(self):
        self.id = Pc.create_id()
        self.included = False
        self.ports_list = []
        self.occupied_ports = {} # словарь, в какой порт подключен какой кабель

    def add_port(self, port):
        self.ports_list.append(port)
        self.occupied_ports[port] = None

    def get_free_port(self):
        for k, v in self.occupied_ports.items():
            if not v:
                return k

    def connect(self, cable):
        free_port = self.get_free_port() #получаем свободный порт
        cable.set_port(free_port)
        free_port.port_occupation(cable)
        cable.add_connected_pc(self)
        self.included = True
        self.occupied_ports[free_port] = cable

    def get_neigbours(self):
        for v in self.occupied_ports.values():
            if v:
                for a in v.pc_list:
                    print(a.id)
