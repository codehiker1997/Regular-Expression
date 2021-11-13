# This is all about the regular expression in python 
# I iwll guid each and everything about the regular expression and will try to make it easy


my_phone_number = "123-122-111"
numbers = []
for char in my_phone_number:
    number_value = None
    try:
        number_value = int(char)
    except:
        pass
    if number_value != None:
        numbers.append(number_value)
number_as_str = ''.join([f"{x}" for x in numbers])
print(number_as_str)
# This is the traditional way to represent the number in a string and write it in aany format


# Now we will move towards regular expression
import re

pattern = "\d+"

v = re.findall(pattern, my_phone_number)
print(v)

# There are unch of method used in regular expression

