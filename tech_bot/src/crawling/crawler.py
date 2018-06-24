import abc

class Crawler(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def crawling(self):
    pass