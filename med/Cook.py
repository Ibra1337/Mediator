from time import sleep
from Elements import Order
from Mediator import Mediator , Component


class Cook(Component ):
    GID =1

    def __init__(self , container:Mediator) :
        super().__init__(container)
        self.currentOrder:Order
        self.free = True
        Cook.GID +=1
        self.id = Cook.GID


    def preapareOrder(self, order: Order):
        self.currentOrder = order
        print(f"cook prepares order: {self.currentOrder.id}")
        sleep(2)
        self.callConrainer("MealDone")

    def giveMeal(self):
        print("meal ready")
        res = self.currentOrder
        self.currentOrder = None
        return res
