#1 print name
def namee(name="taruni"):
    print(name)
namee()

#2 add 2 nums
def add_nums(a,b):
    sum=a+b
    return sum
print(add_nums(3,4))

#3If no name is given, print "Guest
def ex(name="guest"):
    print("hello "+name)
ex()

#4odd por eve
def eveodd(n):
    if n%2==0:
        print("even")
    else:
        print("odd")
eveodd(7)

#5largest num
a,b,c=map(int,input().split())
if a>b and a>c:
    print(a)
elif b>c:
    print(b)      
else:
    print(c)
    
#6sum using args
def summ(*numbers):
    total=0
    for num in numbers:
        total+=num
    return total

print(summ(1,2,5,44,32))
    
        
#7Count how many even numbers are passed
def ex2(*numbers):
    count=0
    for num in numbers:
        if num%2==0:
            count+=1
    print(count)
ex2(3,22,44,23,54,2,21)

#8
def test(**x):
    print(x)

test(a=1, b=2)

#9
def ov(**kwargs):
    for value in kwargs.values():
        print(value)
ov(t=2,a=1,r=7)

#10
def func(a,b,c,**kwargs):
    print(a,b,c)
    print(kwargs)
func(2,3,4,p=10,q=99)

#1
def cpn(*args):
    count=0
    for num in args:
        if num>0:
            count+=1
    return count
print(cpn(-10,2,-4,22,-44,23,28,87,43))    

#2 sum integers
def soi(**kwargs):
    sum=0
    for val in kwargs.values():
        if type(val)==int:
            sum+=val
    return sum
print(soi(a=3,b=2,c="s",d=4,s=3,f=43,h="sd"))


            