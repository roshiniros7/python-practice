#swaping of elements using lists

#a=["apple", "banana", "microsoft"]
#temp=a[0]
#a[0]=a[2]
#a[2]=temp
#print(a)

# for loop

a=["apple", "banana", "microsoft"]
for element in a:
    print(element)

b=[10,20,5]
total=0
for e in b:
    total=total+e
print(total)

#range function
# for elements from 1 to 4
c= list(range(1,5))
print(c)
#we can write same elements using for

total2 = 0
for i in range(1, 5):
    total2 += i #total2=total2+i
print(total2)


def function0(x):
    return x + 1
y=function0(2)
print(y)

total3 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)



total4 = 0
for i in range(1, 100):
    if i % 5 == 0:
        total4 += i
print(total4)

x ="awesome"
def func():
    x= "fantastic"
    print("python is " + x )
func()

print("python is " + x)

x = "awesome"
def myfunc():
    global x
    x="fantastic"
myfunc()
print(" my   "+ x)







