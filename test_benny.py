from abc import ABC, abstractmethod
from benny import Benny, Actor, SingleKeyActor

class Calculator(ABC):
    @abstractmethod
    def calculate(x, y):
        pass

class Adder(Calculator, SingleKeyActor):
    def register_key(self):
        return "ADD"
    
    def calculate(self, x, y):
        return x + y

class Multiplier(Calculator, Actor):
    def register_keys(self):
        return ["MUL", "TIMES"]
    
    def calculate(self, x, y):
        return x * y

dispatcher = Benny(Calculator)
dispatcher.register(Adder())
dispatcher.register(Multiplier())

z = dispatcher.calculate("ADD", 4, 5)
assert(z == 9)
w = dispatcher.calculate("MUL", 2, 3)
assert(w == 6)
v = dispatcher.calculate("TIMES", 0, 2)
assert(v == 0)
