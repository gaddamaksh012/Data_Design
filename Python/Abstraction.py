from abc import ABC,abstractmethod


class computer(ABC):
    @abstractmethod
    def process(self):
        pass

class laptop(computer):
    def process(self):
        print("its running")

com1 = laptop()
# com = computer()
# com.process()
com1.process()


