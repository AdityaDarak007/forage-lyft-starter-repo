from car import CAR, abstractmethod

class serviceable(CAR):
    @abstractmethod
    def needs_service(self):
        pass