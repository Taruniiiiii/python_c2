"""#1 print name
def namee(name="taruni"):
    print(name)
namee()

#2 add 2 nums
def add_nums(a,b):
    sum=a+b
    return sum
print(add_nums(3,4))"""

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

#func with *args and **kwargs
def b(*args,**kwargs):
    odd_tot=0
    eve_tot=0

    for val in args:
        if val%2==0:
            odd_tot+=val
    for val in kwargs.values():
            if val%2!=0:
                eve_tot+=val
    return (odd_tot, eve_tot)
print(b(1,2,3,5,4,6, a=9,b=8,i=1))
            
            
#default and multiple return(combined)
def stats(a, b=10):
    return a+b, a*b

print(stats(5))      # uses default
print(stats(57,83))   # overrides default

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=0
        right=n
        while left<=right:
            mid=(left+right)//2
            res=guess(mid)
            if res==0:
                return mid
            elif res==1:
                left=mid+1
            else:
                right=mid-1

class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        left = 1
        right = num

        while left <= right:

            mid = (left + right) // 2

            if mid * mid == num:
                return True

            elif mid * mid < num:
                left = mid + 1

            else:
                right = mid - 1

        return False
    #leet
def bonAppetit(bill, k, b):
    actual_bill=(sum(bill)-bill[k])//2
    if actual_bill==b:
        print("Bon Appetit")
    else:
        print(b-actual_bill)
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            for j in range(len(heights)-i-1):
                if heights[j]<heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
                    names[j],names[j+1]=names[j+1],names[j]
        return names
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n=len(heights)
        original=heights[:]
        
        for i in range(n):
            for j in range(0,n-i-1):
                if heights[j]>heights[j+1]:
                    heights[j],heights[j+1]=heights[j+1],heights[j]
        count=0
        for i in range(n):
            if original[i]!=heights[i]:
                count+=1
        return count
        