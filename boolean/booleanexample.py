#boolean program for raining or sunny today
'''1. Definig boolean variable'''
is_sunny=True
is_rainy=False

'''2.Perform action based on boolean opration'''

if(is_sunny):
    print("its sunny today")
else:
    print("its rainy today")

if(is_rainy):
    print("is rainy today")
else:
    print("its sunny today")

#boolean example for temperature:
temperature=25
is_hot=temperature>30
is_cold=temperature<10
print(f"it is hot{is_hot}")
print(f"it is cold{is_cold}")

#3.Using and , or , not

is_weekend=True
is_sunny=False

if(is_weekend and is_sunny):
    print("its sunny weekend")
elif(is_weekend and not is_sunny):
    print("its not sunny weekend")
else:
    print("rainy today")

