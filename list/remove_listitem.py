#the remove() method removes the specific item:

tree_list=['banyan', 'mangotree' , 'appletree' ]
tree_list.remove('appletree')
print(tree_list) 

#remove specified index
#by using pop() method:

laptop_list=['hp','dell','lg','sony','infinix']
laptop_list.pop(4)
print(laptop_list)

#the del() keyword is also used to delete the specified index:

laptop_list2=['wio','toshiba','victus','apple']
del laptop_list2[0]
print(laptop_list2)

#the clear() method is used to clear the list:

laptop_list2.clear()
print(laptop_list2)