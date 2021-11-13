# Here i willreview the list comprehension in python\



# ******************** This is the list comprehension in python *****************
mine = [1,2,3,4,5,6,7,8]

even = [x for x in mine if x%2!=0 and x!=1]
odd = [x for x in mine if x%3!=0 and x!=1]


print(even)
print(odd)