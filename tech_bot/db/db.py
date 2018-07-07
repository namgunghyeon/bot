import abc

class Singleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
      if cls not in cls._instances:
          cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)

      return cls._instances[cls]

class DB(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def get(self, site):
    pass

  @abc.abstractmethod
  def save(self, site, title, link):
    pass