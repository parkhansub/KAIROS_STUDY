# class MyClass:
#     def __init__(self, name, id_num, jen, hobby):
#         self.name = name
#         self.id_num = id_num
#         self.jen = jen
#         self.hobby = hobby

#     def print_name(self, nick_name):
#         print(f"우리반 {self.id_num}번째 학생은 {self.name}입니다.\n 그리고 별명은 {nick_name}입니다.")
        

#     def print_jen(self):
#         print(f"우리반 {self.name}는/은 {self.jen}자입니다.")

#     def print_hobby(self) :
#         print(f"{self.name}의 취미는 {self.hobby}")

# stu1 = MyClass("조권희", 1, "남","밴드")
# print(stu1.name)
# stu1.print_name("조조")
# stu1.print_jen()
# stu1.print_hobby()

############계산기 (calculator) 만들기################
# class Calculator :
#     def __init__(self):
#         self.result = 0
        

#     def add(self, num1, num2):
#         self.result = num1 + num2
#         return self.result

#     def sub(self, num1, num2):
#         self.result = num1 - num2
#         return self.result
    
#     def mul(self, num1, num2):
#         self.result = num1 * num2
#         return self.result
    
#     def div(self, num1, num2):
#         if num1 != 0 and num2 != 0:
#             self.result = num1 / num2
#             return self.result
#         else :
#             print("0이외의 값을 넣어 주세요")
#             pass
        




# cal = Calculator()
# print(cal.add(5,3))
# print(cal.sub(5,3))
# print(cal.mul(5,3))
# print(cal.div(5,3))


# class Robot:
#     def __init__(self, name, type):
#         self.name = name
#         self.type = type
#         self.dim = 0

#     def get_description(self):
#         print(f"{self.name} : {self.type}")

#     def increase(self, dim):
#         self.dim += dim
#         print(f"{self.name}의 이동거리 : {self.dim}km")


        


# my_robot = Robot("ROB", "agv")

# my_robot.get_description()
# #ROB : agv
# my_robot.increase(10)
# my_robot.increase(13)
# my_robot.increase(10)

#######CLASS 상속########


# class Father:
#     def __init__(self, surname, given_name) :
#         self.surname = surname
#         self.given_name = given_name
        

#     def get_marry(self, status):
#         if status:
#             print("현재 유부남")
#         else : 
#             print("미혼")
        


# class Sun(Father):
#     def __init__(self, surname, given_name, mother):
#         super().__init__(surname, given_name)
#         self.mother = mother






# father = Father("심", "승환")
# print(father.surname)
# father.get_marry(True)
# sun = Sun(father.surname, "슨", "수지")
# print(sun.surname, sun.given_name, father.surname, father.given_name, sun.mother)
# sun.get_marry(False)
# print(print("d"))

class Employee:
    def __init__(self, emp_name, emp_age, emp_pay) :
        self.emp_name = emp_name
        self.emp_age = emp_age
        self.emp_pay = emp_pay

    def increase(self, pay_mul) :
        self.pay_mul = pay_mul
        return(self.emp_pay * pay_mul)
    

class Developer(Employee):

    def __init__(self, emp_name, emp_age, emp_pay, emp_tech):
        self.emp_tech = emp_tech
        super().__init__(emp_name, emp_age, emp_pay)
    


emp1 = Employee("김민우", 24, 5000)
emp2 = Employee("김무현", 26, 8000)

print(emp1.increase(1.2))
print(emp2.increase(1.3))

dev1 = Developer("장용원", 30, 10000, ["기구설계", "python"])
print(dev1.increase(1.5))
print(dev1.emp_tech)