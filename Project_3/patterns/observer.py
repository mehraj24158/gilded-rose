import abc
from datetime import datetime
class Observer_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def update_season(self, qm, sm):
        raise NotImplementedError

class Subject_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def register(self, observer):
        raise NotImplementedError

    @abc.abstractmethod
    def unregister(self, observer):
        raise NotImplementedError

    @abc.abstractmethod
    def notify(self):
        raise NotImplementedError

class Season(Subject_interface):
    def __init__(self):
        self.observers = []
    
    def register(self, observer):
        self.observers.append(observer)

    def unregister(self, observer):
        observer.update_season(0, 0)
        self.observers.remove(observer)

class Winter(Season):
    def __init__(self):
        super().__init__()
    
    def notify(self):
        today = datetime.today()
        if today.month in range(1, 4):
            for observer in self.observers:
                observer.update_season(10, 10)
        else:
            for observer in self.observers:
                observer.update_season(0, 0)

class Spring(Season):
    def __init__(self):
        super().__init__()
    
    def notify(self):
        today = datetime.today()
        if today.month in range(4, 7):
            for observer in self.observers:
                q = observer._quality
                s = observer._sell_in
                observer.update_season(observer._quality, observer._sell_in)
        else:
            for observer in self.observers:
                observer.update_season(0, 0)

class Summer(Season):
    def __init__(self):
        super().__init__()
    
    def notify(self):
        today = datetime.today()
        if today.month in range(7, 10):
            for observer in self.observers:
                observer.update_season(5, 5)
        else:
            for observer in self.observers:
                observer.update_season(0, 0)

class Fall(Season):
    def __init__(self):
        super().__init__()

    def notify(self):
        today = datetime.today()
        if today.month in range(10, 13):
            for observer in self.observers:
                observer.update_season(5, 3)
        else:
            for observer in self.observers:
                observer.update_season(0, 0)