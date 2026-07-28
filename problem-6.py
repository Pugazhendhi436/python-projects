#oops

from abc import ABC, abstractmethod

#empty class
class vehicle(ABC):
    @abstractmethod
    def display_info(self):
        pass

#class with instance attributes
class car(vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year    

#class with methods
class bike:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print("The bike is starting.")

    def stop(self):
        print("The bike is stopping.")

#object creation
b1=bike("ducati", "monster", 2020)
print(b1.make)
print(b1.model)
print(b1.year)

#inheritance
class vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
#encapsulation - private attributes with getters and setters
    # Getter for make
    @property
    def make(self):
        return self.__make

    # Setter for make
    @make.setter
    def make(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Make must be a non-empty string.")
        self.__make = value

    # Getter for model
    @property
    def model(self):
        return self.__model

    # Setter for model
    @model.setter
    def model(self, value):
        if not value or not isinstance(value, str):
            raise ValueError("Model must be a non-empty string.")
        self.__model = value

    # Getter for year
    @property
    def year(self):
        return self.__year

    # Setter for year
    @year.setter
    def year(self, value):
        if not isinstance(value, int) or value < 1886:  # First car invented in 1886
            raise ValueError("Year must be an integer greater than or equal to 1886.")
        self.__year = value

#polymorphism - overriding method
    def display_info(self):
        print(f"Vehicle Make: {self.make}, Model: {self.model}")    

class car(vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")

class bike(vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model)
        self.year = year

    def display_info(self):
        print(f"Bike Make: {self.make}, Model: {self.model}, Year: {self.year}")
car1 = car("mercedes", "c-class", 2022)
car1.display_info()
bike1 = bike("ducati", "monster", 2020)
bike1.display_info()




