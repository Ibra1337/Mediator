from abc import ABC , abstractmethod




class Mediator(ABC):

    @abstractmethod
    def communicate(self , caller , method:str):
        pass


class Component(ABC) :

    def __init__(self  , container:Mediator):
        self.free =True
        self.container = container

    def callConrainer(self , method:str):
        self.container.communicate(self , method)

#implement 