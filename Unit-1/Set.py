#Write a python program to perform the follwing operations on set

#Create and access set elements 

set_1={'doremon','shinchan','perman','ben10'}
print('SET :',set_1)

print('Accessing element :','ben10' in set_1)

#Union and intersection of sets 

set_2={'mickeymouse','jake&the neverlands pirates','tom&jerry','ben10'}
print('NEW SET  :',set_2)

print('Union of sets :',set_1.union(set_2))

print('Intersection of sets :',set_1.intersection(set_2))

#Difference of the elements

print('Difference of sets :',set_1.difference(set_2))
print('Difference of sets :',set_2.difference(set_1))   