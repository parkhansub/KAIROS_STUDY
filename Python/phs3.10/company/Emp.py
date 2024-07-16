class Employee:
    def __init__(self, name, age, pay):
        self.name = name
        self.age = age
        self.pay = pay

    
    def get_details(self):
        print(f"Name is {self.name}. Age is {self.age}. Pay is {self.pay}.")
        
    def raise_pay(self, num1):
        self.pay = self.pay * num1
        return(self.pay)
    

# emp1 = Employee("심슨", 30, 50000)
# emp1.get_details()
# emp1.raise_pay(1.3)
# emp1.get_details()