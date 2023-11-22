from abc import ABC , abstractmethod

class State(ABC) :

    @abstractmethod
    def doAction(self):
        pass
