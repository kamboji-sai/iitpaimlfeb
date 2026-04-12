'''
a=10
print(id(a))
b=10
print(id(b))

a=input("Enter first number: ")
b=int(a)
c=input("Enter first number: ")
d=int(c)
print(b+d)


marks = [85, 92, 78, 95, 88]
max_value = 85
for i in marks:
    if i > max_value:
         max_value = i

    print("max_value is ", max_value)     

    

orders = [150, 20, -20, 40, 200]

for order in orders :
      if order < 0 :
        continue
      print(order)

      

students = ["Amit", "Priya", "Rahul", "Sneha", "vikram"]

for i in students:
    print("before :", i)
    if i == "Rahul":
        continue
    print("Rahul found")
    print(i)

    

def greet_new_version():
    print("Hello")
    print("Welcome to the class")

greet_new_version()   


def greet(name):
    print(f"Hello, {name}")
          
greet("Sai")
greet("Venkatesh")
greet("Kamboji") 

'''

name = "Sai"
age = 25
height = 5.11
is_student = True

print(f"Name: {name} | Age: {age} | Height: {height} | Student: {is_student}")

age_in_months = age*12
age_in_days = age*365
age_remainder = age %7
age_sauare = age **2

print("Age in months:", age_in_months)
print("Age in days:", age_in_days)
print("Remainder when age is divided by 7:", age_remainder)
print("Age squared:", age_sauare)
