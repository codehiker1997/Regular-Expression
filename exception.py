# This is the how exceptions work in python we can say how we can treat exception handling in pythonn

# First of all we will talk about three type of errors
# >>>>>>>>>>>> Compile time error >>>>>> syntatically wrong code give the compile error
# >>>>>>>>>>>> Run time error >>>>>>>> If user is giving a wrong number >>>>>>>>>>> for example we cannot devide something by 0
# >>>>>>>>>>>> Logical  error >>>>>>>>>>>> The output of the code is not correct


# **************************** Lets check it by example ****************************

a = int(input("Enter First Number"))
b = int(input("Enter Second Number"))
try:
    print("Resource Open")
    print(a/b)
except Exception as e:
    print("Error: We cannot devide something with zero", e)
finally:
    print("Resource Closed")