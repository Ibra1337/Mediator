from Mediator import Component , Mediator
from Elements import Order
from Waiter import Waiter


class Client(Component):
    GID = 1

    def __init__(self, container: Mediator):
        super().__init__(container)
        self.id = Client.GID
        Client.GID += 1

    def callWaiter(self):
        self.callConrainer("CallWaiter")

    def makeOrder(self):
        self.callConrainer("MakeOrder")
        print(f"client: {self.id} is making order")

    def leave(self , order:Order) :
        print("client receved meal and is leaving")
        self.callConrainer("Leaving")
    
    def order(self, order: Order, waiter: Waiter):
        waiter.order = order
        waiter.start()
