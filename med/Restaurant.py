
from Mediator import Mediator , Component
from Cook import Cook
from Waiter import Waiter
from Client import Client
import queue
from Elements import Order


class Restaurant(Mediator):
    
    def __init__(self  ):
        super().__init__()
        self.cook = Cook(self)
        self.waiter = Waiter(self)
        self.client :Client
        
    
    
    def makeOrder(self , caller:Client ):
        order = Order()
        order.generate_random_meals()
        self.waiter.takeOrder(order)

    def orderDeliverted(self , caller:Waiter):
        self.cook.preapareOrder(caller.giverOrder())
    
    def addClient(self , client :Client):
        if client is None:
            exit()
        
        client.makeOrder()
        self.client = client
        
    def mealDone(self , caller:Cook):
        self.waiter.takeMeal(caller.giveMeal())
    
    def mealDelivered(self , waiter:Waiter):
        self.waiter.giverOrder()
        
    def communicate(self, caller: Component, method: str):
        if method == "MakeOrder":
            self.makeOrder(caller)
        elif method=="OrderDelivered":
            self.orderDeliverted(caller)
        elif method =="MealDone":
            self.mealDone(caller)
        elif method =="MealDelivered":
            self.mealDelivered(caller)
        elif method =="Leaving":
            self.client = None
            print("clientLeft")
        else:
            print(f"Unhandled method: {method}")
