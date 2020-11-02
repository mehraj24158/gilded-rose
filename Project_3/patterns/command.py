import abc

class Shelf():
    def __init__(self):
        self.shelf = []

class Invoker_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, item):
        raise NotImplementedError

    @abc.abstractmethod
    def undo(self, item):
        raise NotImplementedError

class Robot(Invoker_interface):
    def __init__(self, name, command):
        self.name = name
        self.command = command

    def execute(self):
        self.command.execute()

    def undo(self):
        self.command.undo()

class Command_interface(metaclass = abc.ABCMeta):

    @abc.abstractmethod
    def execute(self, item):
        raise NotImplementedError

    @abc.abstractmethod
    def undo(self, item):
        raise NotImplementedError

class Clean_sell_in(Command_interface):
    def __init__(self, inventory):
        self.cleaned_items = []
        self.inventory = inventory

    def execute(self):
        for i, item in enumerate(self.inventory.items):
            if item.get_sell_in() <= 0:
                self.cleaned_items.append(self.inventory.items.pop(i))

    def undo(self):
        self.inventory.items[:0] = self.cleaned_items

class Clean_quality(Command_interface):
    def __init__(self, inventory):
        self.cleaned_items = []
        self.inventory = inventory

    def execute(self):
        for i, item in enumerate(self.inventory.items):
            if item.get_quality() <= 0:
                self.cleaned_items.append(self.inventory.items.pop(i))

    def undo(self):
        self.inventory.items[:0] = self.cleaned_items

class Macro_command(Command_interface):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        for command in self.commands:
            command.execute()

    def undo(self):
        for command in self.commands:
            command.undo()