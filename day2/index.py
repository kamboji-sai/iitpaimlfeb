
# numbers 2 > 5 , string > string
# The comparison between two strings is always based on ascii codes of each character. 
# ASCII => Every character in a string internally converted to a standard integer to be stored in the memory.
# 'a' => 97 , 'a' - 'z' (97, 122)
# 'A' - 'Z' (65, 90)
# '0' - '9' (48, 57) 
# print(ord('Z'))

# Comparison between strings: 
# print("aravind" != "aravInd") # 
# print("a" > "A") # 97 > 65
# print("abc" > "abd") # Sicne 'c' not greater than 'd' 
# # "abc", "abcd"
# print("abcd" > "abc") # True

# The result of any comparison operation is "boolean"

"""
 Logical Operators:
 and, or : (Binary operators)

 and: If both the operands are true then the result of the operation is true otherwise false.
 - If the first value is true then the result is equal to the second operand .
 - If the first value is false then the result is first operand. 
 A and B: 

 A      B        A and B
 True   True      True
 True   False     False
 False  True      False
 False  False     False

  or: If at least one operand is true then the result is true otherwise false.

 A or B:
 - If the first operand is a truthy then the result is first operand itself.
 - If the first operand is a falsy then the result is second operand.

 A      B       A or B
 True   True     True
 True   False    True
 False  True     True
 False  False    False

 not: Unary operator

In python we can use any data type as operand for logical operators.

Every value in python can be treated as a boolean value (False, True)
Truthy: All other than Falsy values are truthy : 1, 3, 14.4, "abc", " "
Falsy: None, "", 0, 0.0, False

print("aravind" and 13) # True and True => 13
print(13 and "aravind") # True and True => aravind
print("" and False)  # Falsy and ? => ""
print("aravind" and False) # True and x => x

print(None or "aravind") # Falsy or Truthy => "aravind"
print(None and "") # Falsy and ? => None


not => not True => false, not False => True
not operation always gives boolean result irrespective of the operand data type. 
# print(not True , not False)
print(not "aravind") # not Truthy => False
print(not "") # not Falsy => True
"""

# num = int(input("Enter a number"))
# # num % 2 => 0 (even) , 1 (odd)
# print(num % 2 == 0) # If num is even print True else print False

# If the number is Even print "Even" else print "Odd"
# Conditional statements : Execute a block of code conditionally .

"""
if, elif, else => keywords in python

if condition:
    #line1
    #line2
    #line3
    ...
elif condition: # elif should alway come right after another if or another elif statement only. 
    #lin1
    #line2
    ...
else: # else statement should always be right after another if or elif.
    #Lin1
    #line2
    #line3
    ...

if, elif1, elif2, elif3 ..... elifn, else
=> If the first statement is true none in the if..elif ladder gets a choice. 
=> In an if..elif..else ladder always one block gets executed.
"""

# num = int(input("Enter a number"))
# # num = 3
# if num % 2 == 0 : # 1 == 0 => False
#     print("Even")
# elif True:  # 1 != 0 => True
#     print("Odd")
# elif False:
#     print("second else if")
# elif False:
#     print("second else if")
# else:
#     print("Something")

# gender = input("Enter gender character") # "M" -> Male, "F" -> Female, "O" -> Other

# if gender == "M": 
#     print("Male")
# elif gender == "F":
#     print("Female")
# elif gender == "O":
#     print("Others")
# else:
#     print("Invalid gender")


"""
Loops: (Repetative)
Loops can be used to execute a block of code repetitively.

while loop:
while condition:
    #line1
    #line2
    #line3
    ....
for loop: 
"""

# while True:
#     print("Aravind")
#     print("Rajesh")

# i = 0 # 0 -> 1 -> 2 -> 3
# while i < 3: # 3 < 3 = False
#     print(i) # 0, 1, 2
#     i = i + 1 # i = 3 
# print(i) # 3

# i = 0 
# while i > 0 : # 0 > 0
#     print("i is positive")
#     i = i + 1


# for loop => range(start, end, step) => range(2, 7, 3) => {2, 5}
# range(2, 8, 3) => { 2, 5 } => [start, end)
# range(0, 4, 1) = {0, 1, 2, 3  }

# in -> operatoer is used to check if a value is present in a sequence or not .
# print(2 in range(0, 5, 1)) # { 0, 1, 2, 3 , 4 }

# for variable in sequence: 
# for x in range(0, 5, 2): # { 0, 2, 4 } => x = 0 -> 2 -> 4
#     print(x)

# print your name for 5 times. 
# range(0, 5, 1) = { 0, 1, 2, 3 , 4}

# for i in range(0, 5, 1):
#     print("Aravind")

# range(0, n, 1) => start = 0, end = ?, step = 1
# range(3, 5) => { 3, 4 }
# range(4) => { 0, 1, 2 ,3 }

# Homework => 
# 1. Take a string as an input and check if that's palindrome or not. "madam" 
# 2. Find sum of ascii codes in a given string . "aAX" => {97, 65, 88} = 250
# 3. Find the sum of digits in a given integer. 374833 => 28
