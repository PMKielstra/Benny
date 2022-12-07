from abc import ABC, abstractmethod
import inspect

class Actor(ABC):
    def __set_current_key__(self, key):
        self.__current_key__ = key
    
    def get_current_key(self):
        return self.__current_key__

    @abstractmethod
    def register_keys(self) -> list:
        pass

class SingleKeyActor(Actor, ABC):
    @abstractmethod
    def register_key(self):
        pass

    def register_keys(self):
        return [self.register_key()]

class Benny:

    def __init__(self, APIClass: type):
        self.APIClass = APIClass
        self.keys = {}
        for func, _ in inspect.getmembers(APIClass, predicate=inspect.isfunction):
            if not hasattr(self, func):
                def dispatch(key, *args, **kwargs):
                    assert(key in self.keys)
                    self.keys[key].__set_current_key__(key)
                    return getattr(self.keys[key], func)(*args, **kwargs)
                setattr(self, func, dispatch)
    
    def register(self, newAPI):
        assert isinstance(newAPI, self.APIClass)
        assert isinstance(newAPI, Actor)
        for key in newAPI.register_keys():
            self.keys[key] = newAPI
    