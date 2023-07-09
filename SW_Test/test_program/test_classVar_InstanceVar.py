class Car :
    accel=3.0
    def incaccel(self):
        self.accel +=1 

car1=Car() 
car2=Car()
car3=Car()
print(car1.accel,car2.accel,car3.accel,Car.accel)
car1.accel=4.0
print(car1.accel,car2.accel,car3.accel,Car.accel)
car3.accel=10.0
print(car1.accel,car2.accel,car3.accel,Car.accel)
car2.incaccel()
print(car1.accel,car2.accel,car3.accel,Car.accel)
