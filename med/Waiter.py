from Mediator import Component , Mediator
from Elements import Order
import State




class Waiter(Component):
    GID = 1

    def __init__(self, container: Mediator ):
        super().__init__(container)
        self.free = True
        self.order: Order
        self.id = Waiter.GID
        Waiter.GID += 1
    
    def takeOrder(self , order:Order):
        print("taking order from client")
        self.order = order
        self.callConrainer("OrderDelivered")

    def giverOrder(self) -> Order :
        res = self.order
        self.order = None
        return res
    
    def takeMeal(self , order:Order):
        self.order = order
        print("deliveringMealToCLient")
        self.callConrainer("MealDelivered")

