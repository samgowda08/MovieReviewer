'''
a = 1
b = 'Python'
c = 33.53
print('{} , {} and {}'.format(a,b,c))
print('{1}, {0} and {2}'.format(a,b,c))
print("X value is: {x}. Y value is : {y}.".format(x=2,y='Visual'))
'''
# FUNCTIONS 
'''
def greet():
    print("Hello Guyssss")

greet()
greet()

def greet_two(greeting):
    print(greeting)
greet_two("Howdy")

def greet_three(greeting='Rohan'):
    print(greeting)
greet_three()

def many_types(x):
    if x < 0:
        return "Hello , How are you?"
    else:
        return 0
print(many_types(1))
print(many_types(-1))
'''
'''
def sum(a,b):
    c = a + b
    return c    
def subt(a,b):
    c = a - b
    return c
def mul(a,b):
    c = a * b
    return c
def div(a,b):
    c = a / b
    return c
def display():
    a = int(input("Enter the first number: "))
    b = int (input("Enter the second number: "))
    choice = int(input('Enter your operation \n 1 for sum \n 2 for subtraction \n 3 for multiplication \n 4 for division\n'))
    if(choice==1):
        print("Sum of the number is ",sum(a,b))
    elif(choice==2):
        print("Subtraction of the number is ",subt(a,b))
    elif(choice==3):
        print(mul(a,b))
    elif(choice==4):
        print(div(a,b))
    else:
        print("Invalid")
display()
'''
'''
def isPrime(n):
    flag = 0
    for i in range(2,(n+1)//2):
        if(n%i==0):
            flag = 1
            break
    if flag == 1:
        return 0
    else:
        return 1            
n = int(input("Enter the Number: "))
if isPrime(n) == 1:
    print('{} is a Prime Number'.format(n))
else:
    print('{} is not a Prime Number'.format(n))
'''
'''
def part(n):
    if n < 4:
        return 0
    else:
        a = []
        count = 0
        for i in range(1,n+1):
            for j in range(1,i+1):
                for k in range(1,j+1):
                    for l in range(1,k+1):
                        if (i+j+k+l)==n:
                            count += 1
                            a.append([i,j,k,l])
    print("The number of ways are: ",count)
    print("The possible ways: ")
    print(a)
num = int(input("Enter the Number: "))
part(num)
'''
'''
def digit(n):
    sum = 0 
    prod = 1
    while n:
        temp = n%10
        if temp==0:
            pass
        else:
            sum += temp
            prod *= temp
        n = n//10
    print("The sum of the digits is: {}".format(sum))
    print("The Product of the digits is: {}".format(prod))
n = int(input("Enter the digits: "))
digit(n)
'''
'''
def check(n,m):
    count = 0 
    while n:
        temp = n%10
        if temp==2 or temp==3 or temp==5 or temp==7:
            count+=1
        n = n//10
    if count==m:
        return True
    else:
        return False
n = int(input("Enter the Number: "))
count = 0
for i in range(2,n+1):
    if check(i,len(str(i))):
        count+=1
print("The Possible Numbers:",count)
'''
