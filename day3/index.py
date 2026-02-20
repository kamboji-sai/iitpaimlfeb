"""
Zomato - Few thousands of restaurants 

All restaurants names : List => Array 

Data types: int, float, boolean, string 
In a list we can keep multple data types. 

variable_name = [val1, val2, val3 ... ]
- List is heterogenious.
- List is dynamic , we can grow/shrink the size of the list by adding/deleting elements to/from the list. 
- List is mutable in nature.
- For any data structure: 
    - Access
    - Update
    - adding / deleting
    - Iteration

print() => function
type() => 
len() => 
input() => 
range() => function 
"""
# names = ["Sanjana", 13, 76.8, True, [3, 4, 5]]
# Idexing:  0        1    2     3       4
#           -5       -4   -3    -2      -1
# -ve indexing:
# print(names[0], names[-5])
# print(names)
# names[1] = "Aravind"
# print(names)
# print(names[-6]) # index is out of range / bounds
# names[5] = "New value"
# print(len(names))
# print(names)
# names.append("Sridhar") # adds an element at the end of the list.

# print(names)
# Object: properties, methods 
# human -> name:"Surekha", age: "", address: "" , sleep, eat, walk, cry, code, drink ... 


# Add element into the list. 
# nums = [8, 4, 5, 19]  # add -1 at index 3: [8, 4, 5, -1, 19]
# print(nums)
# nums.insert(3, -1) # inserts -1 at index 3
# print(nums)
# Delete an element from the list.
# deleted_element = nums.pop() # pop deletes the last element from the list and returns it.
# print(deleted_element, nums) # 19, [8, 4, 5]

# Python sequence data types: string, list, range()

# for loop
# nums = [4, 5, 8, 10]
# deleted_value = nums.pop(0) 
# print(nums, deleted_value)
#.      0. 1. 2. 3.  4
# sum = 0
# index = 0
# while index < len(nums):
#     sum += nums[index]
#     index += 1
# print(sum)
# for index in range(0, len(nums), 1):
#     sum += nums[index]
# print(sum)

# for num in nums: # nums is a sequence: [4, 5, 8, 10]
#     print(num)
# for char in "aravind": #{ 'a', 'r', 'a', 'v', 'i', 'n' , 'd'}
#     print(char)
# name = "aravind"
# nums = [3, 4, 2]
# print(name[0], nums[0])

 # whenever we call a function : function_name(param1, param2)
 # nums.pop(29)

# nums = [2, 3, 4, 3, 5] # [2, 4, 3, 5]
# nums.remove(3)
# print(nums)

## Tuples -> Sequence data structures.
"""
Touples are similar to List data structre but the only diff is tuple is immutable.
name = (3, 4 ,5, "aravind")
indexing is again similar to list
len() function gives the length of the tuple.

can i Add/delete/update elements from tuple ? NO!
"""
# nums = 3, 4, 8
# print(type(nums))
# print(nums[2], nums[-2]) # 8, 4

# nums = 1, 9, 8
# nums_list = list(nums) # type casting from tuple to list
# print(nums, nums_list)
# nums_list.append(19)
# nums = tuple(nums_list) # type casting from list to tuple back. 
# print(nums)


# Slicing can be applied to sequence data types. (string -> immutable, lists -> Mutable, tuples -> Immutable)
# "abcd" => slice / subsequence 
# ab, ac, abd, ad => slices of "abcd"
# ba, cda => INvalid slices of "abcd"

# range(start, stop, step)

# variable_name[start:stop:step] => start is inclusive, end is exclusive
# start & end are indices of the sequence.

# nums = [4, 3, 5, 9, 18] 
#.      0. 1. 2. 3.  4
# nums[1:4:1] # indices: 1, 2, 3
# print(nums[1:4:1])
# print(nums[3:4:2]) # indices:3 , [9]

# print(nums[0:4:1])
# print(nums[0:10:2])
# print(nums[::2]) # start = 0, end = len(list)
# print(nums)

# nums = [4, 3, 5, 9, 18] 
# #.      0. 1. 2. 3.  4
# #      -5.-4 -3 -2  -1
# print(nums[-1:-4:-1]) # -1, -2, -3 => [18, 9, 5]
# print(nums[-5:-2:1]) # -5, -4, -3
# print(nums[-1:-4:1]) # -1, 0, 1, 2, 3, .... empty list
# print(nums[4:2:1]) # []


# Dictionaries : (key, value) pair
# {key: val1, key2: val2, key3: val3} => key can be string, int, bool
# value can be of any data type.
# user = {"name": "aravind", "age": 25, "friends": ["Rajesh", "Akhil"], True:False, 10:393.83}
# print(type(user))
# user = {
#     "name": "aravind",
#     "age": 25,
#     "friends": ["a", "b"],
#     "address": {
#         "state":"TG",
#         "district":"Warangal"
#     }
# }

# print(user["friends"][1])
# update age to 26
# print(user["age"])
# user["age"] = 26
# print(user)
# user["cgpa"] = 7.0
# print(user)
# deleted_value = user.pop("friends")
# print(deleted_value, user)
# On using for loop with a dictionary we get sequence of keys.

# user = {
#     "name": "aravind",
#     "age": 25,
#     "friends": ["a", "b"],
#     "address": {
#         "state":"TG",
#         "district":"Warangal"
#     }
# }
# for key in user:
#     print(key, user[key]) # key = "name", user["name"] => "aravind"


# Homework: 
# 1. 2 Sum
# 2. Merge sorted lists
# 3. https://leetcode.com/problemset/#:~:text=28.%20Find%20the,Easy
# 4. https://leetcode.com/problemset/#:~:text=35.%20Search%20Insert,Easy 