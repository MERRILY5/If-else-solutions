'''----------------------1)----------------------'''

n=int(input("Enter value A: "))
m=int(input("Enter value B: "))

if n>m:
    print("Value A is greater")
else:
    print("Value B is greater")



'''----------------------2)----------------------'''
a=int(input("Enter value B: "))
b=int(input("Enter value B: "))
c=int(input("Enter value B: "))

if a>b and a>c:
    print("Value A is greater")
elif b>c and b>a:
    print("Value B is greater")
else:
    print("Value C is greater")



'''----------------------3)----------------------'''
n=int(input("Enter a number: "))
if n==0:
    print("Entered value is 0")
elif n>0:
    print("Entered value is positive")
else:
    print("Entered value is negative")



'''----------------------4)----------------------'''
n=int(input("Enter a value: "))
if n%5==0 and n%11==0:
    print("The number is divisible by 5 and 11")
else:
    print("The number is not divisible by 5 and 11")



'''----------------------5)----------------------'''
n=int(input("Enter a number: "))
if n%2==0:
    print("The number is even")
else:
    print("The number in odd")



'''----------------------6)----------------------'''
n=int(input("Enter the year: "))
if n%4==0:
    print("It is a leap year")
else:
    print("It is not a leap year")



'''----------------------7)----------------------'''
a=input("Enter the alphabet: ")
if (a >= 'a' and a <= 'z') or ( a >= 'A' and a<= 'Z'):
    print("Enter value is alphabet")
else:
    print("Entered value is not an alphabet")



'''----------------------8)----------------------'''
a=input("Enter the alphabet: ")
if a =='a' or a=='e' or a=='i' or a=='o' or a=='u':
    print("Entered value is vowel")
else:
    print("Entered value is consonant")



'''----------------------9)----------------------'''
n=input("Enter any character: ")
if (n >= 'a' and 'z'<= n) or (n >= 'A' and 'Z' <= n):
    print("Entered character is an alphabet")
elif n >='0' or n <= '9':
    print("Entered character is number")
else:
    print("Entered character is a spl character")



'''----------------------10)----------------------'''
a=input("Enter an alphabet: ")
if a >= 'A' and a <= 'Z':
    print("Entered chararcter is uppercase")
elif a >= 'a' and a <= 'z':
    print("Entered character is lowercase")
else:
    print("invalid")



'''----------------------11)----------------------'''
n=int(input("Enter a number: "))
if n==1:
    print("Monday")
elif n==2:
    print("Tuesday")
elif n==3:
    print("Wednesday")
elif n==4:
    print("Thursday")
elif n==5:
    print("Friday")
elif n==6:
    print("Saturday")
elif n==7:
    print("Sunday")
else:
    print("Invalid")


    
'''----------------------12)----------------------'''
n=int(input("Enter a number: "))
if n==1:
    print("Jan - 31 days")
elif n==2:
    print("Feb - 28 days")
elif n==3:
    print("Mar - 31 days")
elif n==4:
    print("Apr - 30 days")
elif n==5:
    print("May - 31 days")
elif n==6:
    print("June - 30 days")
elif n==7:
    print("July - 31 days")
elif n==8:
    print("Aug - 31 days")
elif n==9:
    print("Sept - 30 days")
elif n==10:
    print("Oct - 31 days")
elif n==11:
    print("Nov - 30 days")
elif n==12:
    print("Dec - 31 days")
else:
    print("Invalid")



'''import calendar

y=2024
m=6

p=calendar.calendar(y)
p=calendar.month(y,m)
print(p)'''



'''----------------------13)----------------------'''
n=int(input("Enter the amount: "))
fivehu=hun=fifty=twe=ten=five=two=one=0
if n >=500:
    fivehu = n//500
    n -= fivehu * 500
    
if n >= 100:
    hun = n//100
    n -= hun * 100
    
if n >= 50:
    fifty = n//50
    n -= fifty * 50
    
if n >= 20:
    twe = n//20
    n -= twe*20
    
if n>=10:
    ten=n//10
    n -= n*10
    
if n>=5:
    five = n//5
    n -= n*5
    
if n>= 2:
    two = n//2
    n -= n*2
    
if n>=1:
    one = n
    
    
print("500 = ",fivehu)
print("100 = ",hun)
print("50 = ",fifty)
print("20 = ",twe)
print("10 = ",ten)
print("5 = ",five)
print("2 = ",two)
print("1 = ",one)


  
'''----------------------14)----------------------'''
a=int(input("Enter triangle side 1: "))
b=int(input("Enter triangle side 2: "))
c=int(input("Enter triangle side 3: "))
if (a+b+c)==180:
    print("Triangle is valid")
else:
    print("Triangle is invalid")



'''----------------------15)----------------------'''
a=int(input("Enter triangle side 1: "))
b=int(input("Enter triangle side 2: "))
c=int(input("Enter triangle side 3: "))
if ((a+b)>c) or ((b+c)>a) or ((a+c)>b):
    print("Triangle is valid")
else:
    print("Triangle is invaild")



'''----------------------16)----------------------'''
a=int(input("Enter triangle side 1: "))
b=int(input("Enter triangle side 2: "))
c=int(input("Enter triangle side 3: "))
if a==b==c:
    print("It is a equilateral triangle")
elif a==b or b==c or c==a:
    print("It is a isosceles triangle")
else:
    print("It is a scalene triangle")



'''----------------------17)----------------------'''
import math
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
value=(b*b)-(4*a*c)

if value>0:
    root1 = (-b + sqrt(value))/(2*a)
    root2 = (-b + sqrt(value))/(2*a)
    print("Root1: ",root1)
    print("Root2: ",root2)
elif value == 0:
    root1 = root2 = -b/(2*a);
    print("Root1: ",root1)
    print("Root2: ",root2)
else:
    root1 = root2 = -b/(2*a)
    i = sqrt(-value)/(2*a)
    print("Root1: ",root1)
    print("Root2: ",root2)
    print("Imaginary: ",i)

    

'''----------------------18)----------------------'''
cost = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

if selling_price > cost:
    profit = selling_price - cost
    print(f"The profit is = {profit}")
elif cost > selling_price:
    loss = cost - selling_price
    print(f"The loss is = {loss}")
else:
    print("No loss no profit")



'''----------------------19)----------------------'''
phy=int(input("Enter the mark of Physics: "))
chem=int(input("Enter the mark of Chemistry: "))
bio=int(input("Enter the mark of Biology: "))
math=int(input("Enter the mark of Mathematics: "))
comp=int(input("Enter the mark of Computer: "))

total = phy+chem+bio+math+comp
avg = total/5
if avg >= 90:
    print("Grade A")
elif avg >= 80 and avg <= 89:
    print("Grade B")
elif avg >= 70 and avg <= 79:
    print("Grade C")
elif avg >= 60 and avg <= 69:
    print("Grade D")
elif avg >= 40 and avg <= 59:
    print("Grade E")
else:
    print("Fail")



'''----------------------20)----------------------'''
salary = int(input("Enter the basic salary: "))

if salary <= 10000:
    hra = salary * 0.2
    da = salary * 0.8
elif salary >= 10001 and salary <= 20000:
    hra = salary * 0.25
    da = salary * 0.9
else:
    hra = salary * 0.3
    da = salary * 0.95

gross = salary + hra + da
print("The gross price: ",int(gross))



'''--------------------21)----------------------'''
unit = int(input("Enter the units: "))
bill=0
if unit<=50:
    bill = unit*0.5
    
elif unit<=150:
    bill = 25 + ((unit-50)*0.75)

elif unit<= 250:
    bill = 62.5 +((unit-150)*1.20)

else:
    bill = 220 +((unit-250)*1.50)
    
tax = bill * 0.2
totalBill = bill+tax
print(f"The total bill is {totalBill}/-")









