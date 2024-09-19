person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)

# print out the name of the second child
list_of_children = person['children']
print(list_of_children[1])

# professor prefers it the second way opposed to the first
print(person['children'][1])

# print out the name of the cat
# can't give the index value to a dictionary, so use the key
dict_of_pets = person['pets']
print(dict_of_pets['cat'])

# use this one because it uses less processing power and don't have to take an extra step
print(person['pets']['cat'])

# use a loop to print out the names of each child
# child in this loop is an iterator, children is the list while child is a string
# list and dictionary are iterable
for child in person['children']:
    print(child)

# use a loop to print out the pets in the following format:
# The type of pet is: dog and th ename of the pet is: Fido

for pet,name in person['pets'].items():
    print(f"The type of pet is: {pet} and the name of the pet is: {name}")