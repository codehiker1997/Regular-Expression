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

# Lets take another example 
my_other_phone_numbers = "This is my one phone number 333-444-555 and i can make it +1-23-345-122"
y = re.findall(pattern, my_other_phone_numbers)
print(y)


# But the given example does not give the idea about which is our exact phone numbers or which is not
to_the_number = "lets make a call at 8:30 on my number +1-111-222-333"
my_patter1 = "\d+"
s = re.findall(my_patter1, to_the_number)
print(s)

my_patter2 = r"\+\d{1}\-\d{3}-\d{3}-\d{3}"
# THis is good practice to compile the regular expression
regex = re.compile(my_patter2)
d= re.findall(regex, to_the_number)


print(d)
# There are differen modues used in regular expression
import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())