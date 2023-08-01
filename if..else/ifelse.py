''' #1.Check if the number is positive or negaitve:

num=int(input("Enter one Number:"))
if(num>0):
    print("The Entered Number is positive")
else:
    print("The Entered Number is negative")

#2.Checking a person is eligible for vote:
vote=int(input("Enter Your Age:"))
if(vote>18):
    print("Eliginle For Vote")
else:
    print("Your Not eligible for vote")

#3.Check the number is odd or even:
num=int(input("Enter one Number"))
if(num %2==0):
    print("The Numebe in even")
else:
    print("The Number is odd ") 



#Question 2: Write a Python program that takes three integer inputs from the user and finds the largest number among them using if-else statements. After taking the inputs, please print the largest number. Give it a try!

num1=int(input("Enter Numner1:"))
num2=int(input("Enter Number2:"))
num3=int(input("Enter Number3:"))
if(num1>num2 and num1>num3):
    print("Number 1 is greatest")
elif(num2>num1 and num2>num3):
    print("Number 2 is greatest") 
else:
    print("Number 3 is greatest") 

#Question 3: Write a Python program that takes a character (a-z or A-Z) as input from the user and checks if it is a vowel or a consonant using an if-else statement. After taking the input, please print "Vowel" if the character is a vowel and "Consonant" if it is a consonant. If the input is not a valid character (neither a-z nor A-Z), print "Invalid input

vowel = input("Enter a Character: ").lower()

if vowel in ('a', 'e', 'i', 'o', 'u'):
    print("The character is a vowel.")
else:
    print("The character is a consonant.")

#Question 4: Write a Python program that takes a year as input from the user and checks if it is a leap year or not using if-else statements. After taking the input, please print "Leap year" if the year is a leap year, and "Not a leap year" if it is not a leap year.
year = int(input("Enter a Year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("This is a leap year.")
else:
    print("Not a leap year.")

#Question 5: Write a Python program that takes three integer inputs from the user and finds the smallest number among them using if-else statements. After taking the inputs, please print the smallest number.

num1 = int(input("Enter Number 1: "))
num2 = int(input("Enter Number 2: "))
num3 = int(input("Enter Number 3: "))

if num1 <= num2 and num1 <= num3:
    smallest = num1
elif num2 <= num1 and num2 <= num3:
    smallest = num2
else:
    smallest = num3

print("The smallest number is:", smallest) '''


# Question 6: Write a Python program that takes an integer input from the user and checks if it is a prime number or not using an if-else statement. A prime number is a positive integer greater than 1 that has no positive divisors other than 1 and itself. After taking the input, please print "Prime" if the number is a prime number, and "Not Prime" if it is not a prime number.
num=int(input("Enter a Number:"))
if(num%2==0):
    print("This is not a prime number")

else:
    print("the Numer is prime")