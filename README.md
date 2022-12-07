# Benny: Quick-and-Dirty Python Function-Key Dispatch

Occasionally I have a couple of different classes that expose the same interface and I have to switch between them.  For instance, sometimes I want a user to be able to use multiple file formats to input the same data.  Benny is a general solution for this.

```
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
```

Create your `Benny` object (in this case, `dispatcher`) with a base class.  The object will take on all methods available in that base class.  You can then register instances of subclasses of that class.  Registered classes are expected to inherit from `Actor` or a subclass as well, which provides the `register_keys` function.  `SingleKeyActor` provides `register_key` instead.

`Actor` also provides the `self.get_current_key()` method, which returns the actual key used to dispatch the function call.  This is handy if, say, you have one parser that can handle two different file types and a second parser that handles a third type.

