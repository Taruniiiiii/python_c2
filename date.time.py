"""li=map(int,input().split())
for n in li:
    print(n*n)
##type2
li=map(int,input().split())
li1=[]
for i in li:
    li.append(i*i)
print(li1)"""

#print primes till 100 using functions
def is_prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
for num in range(2,101):
    if is_prime(num):
        print(num)
        
import datetime
now=datetime.datetime.now()
print(now)
print(now.year)
print(now.month)

#math module
# Print the lowest value
print(min(5,10))
# Print the highest value
print(max(5,10))
# Print the absolute value
print(abs(-7.25))
# Print 4 to the power of 3
print(pow(4,3))
