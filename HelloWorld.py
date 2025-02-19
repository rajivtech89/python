"""
print("Hello World")
print("-"*10)
price=10;
print(price)
rating=9.5
name="hello"
print(rating)
print(name)
is_published=False;
print(is_published)

employee_name="Virat";
employee_age=20;
is_new_employee=True;
#your_name = input('enter your name')
#favourite_color=input('enter your favourite color')
#print(your_name +' likes '+favourite_color +' color')

#birth_year = input('Birth Year :')
#age = 2025 - int(birth_year)
#print(age)
#print(type(age))
course= "Python course for beginners"
print(course)
print(course[0])
print(course[-1])
print(course[0:5])
print(course[0:])
print(course[1:])

#copy of string
another=course[:] 
print(another)
print(course[1:-1])
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)

#string methods
course = "Python course for beginners"
print(len(course))
print(course.upper()) # this does not modify the original string
print(course)
print(course.find('P')) # returns the index of the first occurrence of the character
print(course.replace('beginners', 'absolute beginners'))
print('Python' in course)   # returns a boolean value 
a=10;
a+=5;
print(a)

#operator precedence
x=10+3*2
print(x)

x=2.9
print(round(x))

"""
import math
print(math.ceil(2.9))
print(math.floor(2.9))  

is_hot=True
is_cold=False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water") 
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print ("It's a lovely day")
print("Enjoy your day")

price=1000000
has_good_credit=True
if has_good_credit:
    down_payment=0.1*price
else:
    down_payment=0.2*price
print(f"Down payment: ${down_payment}")



#logical operators
if has_good_credit and price>100000:
    print("Eligible for loan")
has_good_credit=False
has_high_income=True
if has_high_income and has_good_credit:
    print("Eligible for loan")

if has_high_income and not has_good_credit:
    print("Eligible for loan")

#comparison operators
temperature=35
if  temperature>30:
    print("It's a hot day")
else:
    print("It's not a hot day") 

name="Alice"
if len(name)<3:
    print("Name must be at least 3 characters")
elif len(name)>50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")


#weight converter
weight=int(input('Weight: '))
unit=input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted=weight*0.45
    print(f"You are {converted} kilos") 
else:
    converted=weight/0.45   
    print(f"You are {converted} pounds")   

#while loops
i=1
while i<=5:
    print('*'*i)
    i+=1
print("Done")


#guessing game
secret_number=9
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input('Guess: '))
    guess_count+=1 
    if guess==secret_number:
        print("You won!")
        break
    else:
        print("Sorry, you failed!")