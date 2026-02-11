"""
- print() => prints on to the console.
- input("Enter a number") -> Takes the input from the user during the execution of the program
"""

"""
Arithmatic operators in python: 
+ => addition => 2 + 3 = 5
- => subtraction => 2 - 3 = -1
* => multiplication => 2 * 3 = 6
/ => division => 5 / 2 = 2.5
(q: 2.5, r: 0), (q: 2, r: 1)

% => calculates the reminder of a division 
5 % 2 = 1
(q: 2, r: 1)

// => Floor division 
5 // 2 = 2

** => Exponentiation operator 
2^3 => 2**3 = 8
4 ** 2 = 16
"""

# all the arithmatic operators are binary operators 
# ? can i use ariothmatic operators between two boolean data type ?
# Arithmatic operatos can only be operated between two numbers 
# boolean type is a subset of integer data type : True -> 1, False -> 0
# int + int => Possible 
# float + int => Possible 
# boolean * int => False * 10 = 0
# string - string => "abc" - "xyz" =? 
# print("abc" + "xyz") # abcxyz "+" => Concatenation operator and not arithmatic operator.
# print("abc" / 10)  # "abc" + "abc"

# Find the last digit in a given number : 
# num = 437 # 435 / 10 => reminder is always the last digit. 
# print(num % 10)

# Home work: find the sum of digits in a given integer. 437 = 4 + 3 + 7 = 14

first_name = "aravind" #  "aravind" + " " = "aravind "
last_name = "samudrala"

# Full name: with space separation "aravind samudrala"
print(first_name + " " + last_name)