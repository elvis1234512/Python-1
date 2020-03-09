
class Temperature:
    def __init__(self, value):
        self.temperature = value

    def Celsius_to_Farenheit(self):
        print((self.temperature-32)*5/9)


        
        
    def Farenheit_to_Celsius(self):
        print((self.temperature*9/5)+32)

        
        
c= Temperature(100)
print(c.Celsius_to_Farenheit())
print(c.Farenheit_to_Celsius())



