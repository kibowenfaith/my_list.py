my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print("List of Lists: ", my_list)

my_list.insert(1, 15)
print("Updated my_list:", my_list)

my_list.extend([50, 60, 70])
print("After extending with my_list1:",my_list)

my_list.pop(7)
print("Updated my_list after removing the last element:", my_list)

my_list.sort(reverse=True)
print("Sorted my_list in descending order:", my_list)

index_of_30 = my_list.index(30)
print("Index of 30 in my_list:", index_of_30)

print("Updated my_list:", my_list)

