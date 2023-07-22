'''
a = 'abcdefg'
print(a[-1])
print(a[:])
print(a[::])
print(a[3:])
print(a[:4])
print(a[2:4])
print(a[::2])
print(a[1:4:2])
print('Negative Indices')
print(a[:-1])
print(a[:-2])
print(a[-1:])
print(a[3:1])
'''
'''
n = int(input("Enter the value: "))
for i in range(n):
    print("*"*n)        #Run it in the TERMINAL not in the output
'''
'''
n = int(input("Enter the number: "))

if(n>=2 and n<=10):
    for i in range(1,(n*n)+1):
        if(i%n==0):
            print(i)
        else:
            print(i,end="*")
else:
    print("Invalid Number")
'''
'''
n = int(input("Enter the number: "))
for i in range(1,n+1):
    print("* "*i)
for j in range(n-1,0,-1):
    print("* "*j)
'''
'''
n = 5
for i in range(n+1):
    for j in range(n,i,-1):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")
    print()
'''
'''
n = 5
for i in range((n*n),0,-n):
    for j in range(i-(n-1),i+1):
        if(j%n==0):
            print(j)
        else:
            print(j,end="*")
'''
'''
n = int(input("Enter the number: "))
flag = 0
for i in range(1,(n+1)//2):
    if(n%i==0):
        flag += 1
if(flag>=2):
    print(n,"is not a Prime Number")
else:
    print(n,"is a Prime Number")
'''        

    
    
        