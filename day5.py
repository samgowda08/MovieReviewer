# Whenever a function is called stack frames are created henc we can have a recursive function
    #But in  INLINE FUNCTION we cannot have recurssive function. Because no creation of stack frames
    
'''
greet_me = lambda: "Hello World"
print(greet_me())

strip_and_uppercase = lambda s: s.strip().upper()
print(strip_and_uppercase("  hello world  "))
'''
'''
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
add= lambda a,b: a+b
mul = lambda a,b: a*b
subt = lambda a,b: a-b
div = lambda a,b: a/b
print("Sum of the two numbers is ") 
print(add(a,b))
print("Subtraction of the two numbers is ") 
print(subt(a,b))
print("Division of the two numbers is ") 
print(div(a,b))
print("Multiplication of the two numbers is ") 
print(mul(a,b))
'''
# List is represented by the square brackets [] and elements inside it separated by the commas , 
'''
l1 = [1,3,'hello','hi']
print(l1,"\n",type(l1))
l1.append('hero')
print(l1)
l2 = [1,4,'python','coding']
print(l2)
l3 = []
l3.append(l1)
l3.append(l2)
print(l3)
for i in (l1):
    print(i,type(i))
l1.extend(l2)
print(l1)
l2.extend(range(1,11,2))
print(l2)
l4 = [1,2,3,4] + [5,6]
print(l4)
l5 = [10,20,30]
l6 = [40,50]

l7 = l5 + l6
print(l7)
'''
'''
a = [1,2,3]
b = [4,5,6]
a[2] = 55
print("printing the list",a)
print("printing the number in a list",a.index(55,2)) # Checks for 55 in the list a at position 2(3rd place)
# print(a.index(23))  --> Value Error
a.insert(2,30) # adds 30 at the 2nd position ( index, value)
print("Inserting the number  ",a)
print("length of the list is {}".format(len(a)))
a.pop(3) # removes element from given index
print("after popping",a)
a.append(2)
print("Adding the number(append)",a)
a.remove(2) #remove the 1st occurrence of the given value . If its not present it throws value error
print("Using the Remove",a)
a.sort()
print("After Sorting: ",a)
a.reverse()
print("After Reversing the string: ",a)
c = [2,35,66,1,3,2,4,66,1,3,52,2,3,2]
c.count(2)
print(c.count(2))
'''
'''
x = ['xyz','abcdef','ijk','lmn','opq']
print(list(map(len,x)))
a,b = map(int,input("Enter the number: ").split())
print(a,type(a))
print(b,type(b))

def func(x):            #func = lamba x: int(x)*int(x)
    x = int(x)
    return x*x
a,b = map(func,input("Enter the number: ").split())     #map(lamba x: int(x)*int(x))
print(a,b)
print(type(a),type(b))
'''