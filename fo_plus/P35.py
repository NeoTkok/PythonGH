class Car:
    def __init__(self, a, b, c):
        self.capacity, self.speed, self.number = a,b,c
    def __str__(self):
        return f"<Car capacity:{self.capacity} speed:{self.speed} number:{self.number}>"
    
    def __eq__(self, obj):
        if (type(obj.number) == 'str'):
            return self.number == obj.number
        return "false"

c = Car(1000, 100, "a720po")
a = Car(1123, 234, "abc")
b = Car(12, 5, "abc")

print(a == None)