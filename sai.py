'''
student_name = 'Alice'
student_age  = 20
student_grade = 'A'
print(student_name)
print(student_age)
print(student_grade)

temperature =72
print(temperature)
temperature=68
print(temperature)
temperature=75
print(temperature)

game_score = 0
print(game_score)
Level_1 = game_score + 100
print(Level_1)
Level_2 = Level_1 +150
print(Level_2)
penalty = Level_2 -50
print(penalty)

a = 10
b = 20
temp=a
a=b
b=temp
print("a:", a)
print("b:", b)

print("abc" > "abd")
print(ord('c'))
print(ord('d'))



gender = input("Enter gender character")
 # "M" -> Male, "F" -> Female, "O" -> Other

if gender == "M": 
    print("Male")
elif gender == "F":
     print("Female")
elif gender == "O":
    print("Others")
else:
    print("Invalid gender")

    

X = int(input("Enter a number"))
 

if X > 0:
    print("Positive number")
elif X < 0:
     print("Negative number")
else:
    print("Zero")

    

Z = int(input("Enter your Age"))

if Z >= 18:
    print("You can vote")
if Z >= 21:
    print("You can drink alcohol (in US)")

print("Thank you") 



score = int(input("Enter your score"))

if score >= 90:
    print("Grade: A")
    print("Excellent work!")

if score >= 80 and score < 90:
    print("Grade: B")
    print("Good job!") 

if score >= 70 and score < 80:
    print("Grade: C")
    print("Satisfactory")

if score >= 60 and score < 70:
    print("Grade: D")
    print("Needs improvement")

if score < 60:
    print("Grade: F")
    print("Failed")    

if score == 100:
    print("Perfect score")

if score < 50:
    print("Please see instructor")

    

age = 15
is_student = True

if age < 18 and is_student:
    price = 5
elif age < 18 and not is_student:
    price = 7
elif age >= 18 and is_student:
    price = 8
else:
    price = 10

print("Ticket Price: $", price)

username = "admin"
password = "secret123"

if not username:
    print("Error: Username is required.")
elif not password:
    print("Error: Password is required.")
elif username != "admin":
    print("Error: Invalid username.")
elif password != "secret123":
    print("Error: Incorrect password.")
else:
    print("Login successful")

bill_amount = 85.00
tip_rate = 0.18*85.00
print(tip_rate)
rounded_tip = round(tip_rate,2)
print(rounded_tip)
total_amount = bill_amount + rounded_tip
print(total_amount)
split_four = total_amount / 4
print(split_four)


a = (2 * 3600) + (30 * 60) + 45
print(a)



number = int(input("Enter a 3-digit number: "))

ones = number % 10
tens = (number // 10) % 10
hundreds = number // 100

print("Hundreds:", hundreds, "Tens:",tens, "Ones:", ones)


scores = [85, 92, 78, 95, 88]

average = sum(scores) / len(scores)

print("average:", average)



numbers = [45, 23, 67, 89, 12, 56]

max_index, max_value = max(enumerate(numbers), key=lambda x: x[1])

print("Max value:", max_value)
print("Index:", max_index)



a = (7,)
print(type(a))



red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

print("Red:", red)
print("Green:", green)
print("Blue:", blue)



numbers = [5, 2, 8, 2, 9, 2, 1, 2]
target = 2

positions = []

for index, value in enumerate(numbers):
    if value == target:
        positions.append(index)

print("Value found at positions:", positions)



names = ["Alice", "Bob", "Emily", "David", "Oliver", "Sarah"]
count =0
for name in names:
    if name.startswith(("A", "E", "I", "O", "U")):
        count +=1
        print(name)
        print("count:", count)

        

def greet():
    print("Hello, World!")
    
greet()   



def print_separator():
    print('-' * 30)

print_separator()



def circle_area(radius):
    pi = 3.14159
    area= pi*radius*radius
    print("area:", area)
circle_area(5)

def welcome(name):
    print("Welcome", name, "to Python Programming!")
    print("Let's learn functions together!")

welcome("sai")    


def countdown():
    for a in range(10, 0, -1):
        print (a)

countdown()       



def celsius_to_fahrenheit(C):
    F = (C*9/5) + 32
    print(F)

celsius_to_fahrenheit(25)

'''

x = 100
y = 100
print(id(x))
print(id(y))      