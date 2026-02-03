#Write a python program to perform the following operations on Dictionary

#Create and access dictionary elements

dict_1={'name':'Peter','age':25,'city':'New York'}

print('DICTIONARY :',dict_1)

print('Accessing element :',dict_1['name'])

#Update Dictionary

dict_1['age']=26
dict_1['profession']='Superhero'

print('Updated Dictionary :',dict_1)

#Remove elements from Dictionary

del dict_1['city']
print('After removing city :',dict_1)

#Merging dictionaries

dict_2={'hobby':'swinging','strength':'super strength'}

dict_1.update(dict_2)
print('Merged Dictionary :',dict_1)