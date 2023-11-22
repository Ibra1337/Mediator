from Restaurant import Restaurant
from Client import Client


restauant = Restaurant()




for i in range(8):
    restauant.addClient(Client(restauant))


