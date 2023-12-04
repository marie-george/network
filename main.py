from class_cable import Cable
from class_pc import Pc
from class_port import Port

pc1 = Pc()
port1 = Port()
port2 = Port()
pc1.add_port(port1)
pc1.add_port(port2)
cable1 = Cable()
pc1.connect(cable1)
pc2 = Pc()
port3 = Port()
pc2.add_port(port3)
pc2.connect(cable1)
pc1.get_neigbours()




