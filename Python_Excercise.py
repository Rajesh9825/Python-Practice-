# 1. Program to add two numbers in python
# Solution 1- (with predefined variable)
'''
num1 = 30
num2 = 40
print("the sum of given numbers: ",num1+num2)
'''

# Solution 2 - (with user input)
'''
num1=float(input("enter number 1: "))
num2=float(input("enter number 2: "))
sum = num1 + num2
print("Sum of two numbers is: ",sum)
'''
###################################
# 2. FInd and calculate square root program in python
# solution 1: (Using Exponentiation)
'''
num = 64
sr = num**(1/2)  #using Exponential operator 
print("the square root of given number is: ",sr)
'''

# solution 2: (Using Math module)
'''
import math
num = int(input("Enter a number here: "))
sr = math.sqrt(num)
print("The square root of given number is:",sr)
'''
####################################################
# 3. Calculate the area of triangle
'''
height = float(input("Enter the height of the triangle: "))
base = float(input("ENter the base of the triangle: "))

Area = (1/2)*height*base
print("The Area of Triangle is: ",Area)
'''
######################################################
# 4. Swap two variables in python
# Solution 1: (Using 3rd Variable)
'''
x = 12
y = 15

temp = x
x = y
y= temp
print("The valua of x is: ",x)
print("The value of y is: ",y)
'''
# Solution 2: (Without using 3rd Variable)
'''
x = 15
y = 20
x, y = y, x
print("The value of x is: ",x)
print("THe value of y is: ",y)
'''
#################################################
# 5. Program to Convert kilometers to Miles
# (Kilometers to Miles)....1Km = 0.621371Mile
'''
km = float(input("Enter your value in KM: "))
miles = (0.621371)*km
print(km ,"kms in miles will be ", miles,"miles")
'''

####################################################
# 6. Python program to check if a number is positive, negative or 0.
# SOlution (using conditional statement)

'''
num = int(input("Enter the number: "))

if num > 0:
    print("number is positive")
elif num == 0:
    print("number is 0")
else: print("number is negative")
'''

################################################
# 7. Check number is even or odd
# solution :
'''
num = int(input("ENter the number: "))

if num % 2 == 0:
    print("Number is Even number")
else:
    print("Number is Odd number")
'''
###############################################

# 8. Program to check leap year
# Solution:
'''
year = int(input("enter a year: "))

if (year % 400 == 0) and (year % 100 == 0): # this conditions are use for century year like 2000, 3000,4000.
    print(year," is a leap year")
elif (year % 4 == 0) and (year % 100 != 0): #this conditions are used for non century years like 1996, 2004,2008.
    print(year, " is a leap year")
else: print(year," is not a leap year")
'''

# 9. Python program to find the largest among three numbers
# solution
'''
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))

if (num1 > num2) and (num1 > num3) :
    print(num1, " is a largest number")
elif (num2 > num1) and (num2 > num3):
    print(num2," is a largest number")
else:
    print(num3, " is a largest number")

'''

########################################################
# 10. Python Program to check Prime number
# Prime number are 3,5,7,11,13,17 etc. it is a number who only divisible by 1 or itself.
'''num = int(input("enter a number here: "))

if num == 1:
    print("It is not a Prime Number")
if num > 1:
    for i in range(2,num):
        if num % i == 0:
            print("It is not a Prime Number")
            break
    else: print("It is a Prime Number")'''

# homework: find first 10 prime numbers?
################################################
# 11. Python Program to Generate a random Number
'''
import random
num = random.randint(0,10)
print(num)
'''
#################################################

# 12. Program to print all prim numbers in an interval
# Solution:
'''
lower = int(input("Enter a lower limit here: "))
higher = int(input("Enter a higher limit here: "))

for num in range (lower,higher+1): # here we are taking lower and higher value to show prime values till higher value
    if num > 1:                 # if this condition satisfy it below for loop run one by one
        for i in range (2,num):
            if num%i == 0 :
                break
        else: print(num)
'''
##############################################################
# 13. Program to convert celcius to Fahrenheit
# Solution:  0 Celcius  = 32 Fahrenheit
# Formula: (C*9/5) + 32 = F

'''
celcius = int(input("Enter Temperature in celcius: "))

fahrenheit = celcius * (9/5) + 32
print("the converted value is ",fahrenheit, "Fahreneit")
'''
###########################################################

# 14.FInd the Factorial of a number
# Solution 1: (Using For Loop)
'''
num = int(input("Enter a number here: "))

fact =1

if num < 0:
    print("Factorial of less than 0 does not exist")
if num == 0:
    print("factorial of 0 is",1)
if num > 0:
    for i in range(1,num+1):
        fact=fact*i
print("The factorial of given number is",fact)
'''
# Solution using recursion
'''
execution of code: assume we factorial of 5
5! = 5*4!
4! = 4*3!
3! = 3*2!
2! = 2*1!
i mean how recursion works here print( (5 * (4*(3*(2*(1))))) )
'''
# Code:
'''def fact(a):
    if a == 0:
        return 1
    else:
        return (a * fact(a-1))

num= int(input("Enter the value: "))
result = fact(num)
print("The factorial of given number is ",result)
'''
########################################################

# 15. DIsplay the Multiplication Table
# Solution: using for loop
'''
num = int(input("Enter a number: "))

for i in  range(1,11):
    print(num,"X",i,"= ",num*i)
'''
# Solution: (Using While loop)
'''
num = int(input("enter a number : "))
i = 1
while i <= 10 :
    print(num," X ",i,"=",num*i )
    i += 1 

'''
#######################################
# 16. Print the Fibonacci Sequence
# Solution: fibonacci sequesnce means it is the addition of previous or preceding 2 values eg: 0,1,1,2,3,5,8...etc.
'''
a= 0
b= 1
num=int(input("Enetr a number to obtain fibonacci sequence: "))
if num==1:
    print(a)
else:
    print(a,end="\t")
    print(b,end="\t")
    for i in range(2,num):
        c = a+b
        a = b
        b = c
        print(c,end="\t")

'''
################################################################
# 17. Program to check Armstrong Number
# Solution: ARmstrong number means assume
# 153 is armstrong number how bcz: 153 = (1*1*1)+(5*5*5)+(3*3*3) = 153
# SOlution: (for 3 digit armstrong number only)
'''
num = int(input("ENeter a number here: "))
sum = 0
temp = num

while temp > 0:
    digit = temp % 10  # last digit of given number will generate as output
    cube = digit ** 3 # Taking qube of last digit of given number
    sum = sum + cube # adding last digit cube with other digits cubes
    temp //=10 # here by using float division removing last digit
if sum == num:
    print("given number is Armstrong number")
else:print("Given number is not an Armstrong number")
'''
# Solution 2: may be it will 4 or 5 digit number so we will use len function
'''
num = int(input("ENeter a number here: "))
sum = 0
temp = num
order = len(str(num))

while temp > 0:
    digit = temp % 10  # last digit of given number will generate as output
    cube = digit ** order # with respect length of number here we will take power of the last digit number
    sum = sum + cube # adding last digit cube with other digits cubes
    temp //=10 # here by using float division removing last digit
if sum == num:
    print("given number is Armstrong number")
else:print("Given number is not an Armstrong number")
'''

################################################################

# 18. Program to find armstrong number in an interval
# Solution:

'''
lower = int(input("Enter the lower limit here: "))
upper = int(input("Enter the upper limit here: "))


for num in range(lower,upper+1):
    temp=num
    sum = 0
    order = len(str(temp))
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //=10
    if sum == num:
        print(num)
'''

#######################################################
# 19.
