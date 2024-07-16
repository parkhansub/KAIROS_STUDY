from .Emp import Employee

class Developer(Employee):
    def __init__(self, name, age, pay, strength):
        super().__init__(name, age, pay)
        self.strength = strength
    
    def get_details(self):
        super().get_details()
        print(f"Stength is {self.strength}")        


# dev1 = Developer("대주주", 25, 60000, ["Python", "JavaScript"])
# dev1.get_details()
# dev1.raise_pay(2)
# dev1.get_details()