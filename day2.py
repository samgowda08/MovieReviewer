''' 
print("My",end="->")
print("Name",end="->")
print("is",end="->")
print("Sampath",end="")
'''
'''
print("My","Name","is","Sampath",sep=" ++++ ")
print("My","Name","is","Sampath",sep=" ---> ")
print("My","Name","is","Sampath",sep="\t+++\t")
print("My","Name",'is','Sampath',sep=" +++ ",end=" ***")
'''

# if 2>1 and 4<5:
#     print("\t2 is Greater than 1",sep="===",end="\n*****************************")
# print("\n\tEnd of the program")
'''
a,b,c = 31 , 15 , 9

if a>b and a>c:
    print("a is the greatest")
elif b>a and b>c:
    print("b is the greatest")
else:
    print("c is the greatest")
    '''
 ##or
'''
a,b,c = 12,33,4
print(max(a,b,c))
print(min(a,b,c))
'''
'''
a,b,c,d,e = 2,4,5,6,7
num = 5
if num in (a,b,c,d,e):
    print("Number is present")
else:
    print("Number is not present")
    '''
'''
n=1
while(n<101):
    print(n)
    n += 1
print("End of the program")
'''
'''
n=0
while(n<101):
    if (n%2!=0):
        print(n)
    n +=1
 '''
'''
for i in (10,20,30,40):
     print(i)
for i in range(1,11,1):
    print(i)
'''
'''
n = 1234
a = 0
while(n>0):
    temp = n%10
    a = a * 10 + temp
    n = n//10
print(a)
'''
'''
e = 0
o = 0
for i in range(1,101):
    if(i%2!=0):
        o += i  
    else:
        e += i       
print("Sum of Odd Number is ",o)
print("Sum of Even number is ",e)
'''
'''
for i in range(1,11):
    a = i**2 -1
    print(a,end=",")
''' 
'''  
 a = 1
 for i in range(5):
     print(a,end=",")
     a = a*2
'''
'''
for i in range(1,11):
    if(i%2==0):
        print(i**2,end="-")
    else:
        print(i**2,end="+")
'''

    