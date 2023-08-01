#we can access the list items using index
my_list=['tata', 'hyundai', 'maruti']
print(my_list[0])

#negative indexing : python supports negative indexing that means stats from the end
print(my_list[-1])

#range of index : you can specify the stating and ending of the string [:] and it also supporting negative indexing
my_list2=['hero', 'honda', 'tvs', 'yamaha', 'ktm', 'bajaj']
print(my_list2[2:5])
print(my_list2[:2])


#check if the item is exists  : by using # in # keyword
if "tvs" in my_list2:
    print("apache is my favorite")
else:
    print("tvs is not availabe in the list")
