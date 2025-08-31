def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))

    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)
print()

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") #kw.["make"]
        self.model = kw.get("model") #kw.["model"]
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="Skyline")
print(my_car.make)
print(my_car.model)
print(my_car.color)