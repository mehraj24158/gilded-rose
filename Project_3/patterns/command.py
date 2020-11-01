import abc
class Command_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, item):
        raise NotImplementedError

    @abc.abstractmethod
    def undo(self, item):
        raise NotImplementedError

    @abc.abstractmethod
    def log(self, item):
        raise NotImplementedError

class Invoker_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, item):
        raise NotImplementedError

    @abc.abstractmethod
    def undo(self, item):
        raise NotImplementedError

class get_item(Command_interface):
    def __init__(self, inventory = None):
        self.inventory = inventory

    def execute(self, item):
        if item in self.inventory:
            return self.inventory.pop(item)
        else:
            raise AssertionError(" Item not present in inventory")
        
    def undo(self, item)

class clean(Command_interface):
    def __init__(self, inventory = None):
        self.inventory = inventory
    
    def execute(self):
        for item in self.inventory:
            if item.sell_in <= 0:
                self.inventory.garbage.append(self.inventory.pop(item))

class Robot(Invoker_interface):

    def __init__(self):
        self.name
        self.command

    def execute(self):
        self.command.execute()

    def undo(self):
        self.command.undo()

    def log(self):
        self.command.log()