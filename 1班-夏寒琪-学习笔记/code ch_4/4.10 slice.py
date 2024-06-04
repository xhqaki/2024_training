animals_list=["dog","cat","bird","fish","monkey"]
print("The first three items in the list are:")
for animal in animals_list[:3]:
    print(animal)
print("The items from the middle of the list are:")
for animal in animals_list[1:4]:
    print(animal)
print("The last three items in the list are:")
for animal in animals_list[2:]:
    print(animal)