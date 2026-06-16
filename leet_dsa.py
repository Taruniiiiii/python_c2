"""#two sum
def two_sum(num,target):
    di={}
    for i in range(len(num)):
        res=target-num[i]
        if res in di:
            return [di[res],i]
        di[num[i]]=i
        
#palindrome
s="A man, a plan, a canal: Panama"
ex=""
for word in s:
    if s.isalnum():
        ex+=word.lower()
reverse=ex[::-1]
if ex==reverse:
    print("palindrome")
else:
    print("not palindrome")
    
#duplicates
nums=[1,2,3,1]
rep=False
for i in nums:
    if nums.count(i)>1:
        rep=True
if rep:
    print("yes dups")
else:
    print("no dups")
    
#anagram
strs = ["act","pots","tops","cat","stop","hat"]
for i in strs:
    grp=[]
    for j in strs:
        if sorted(i)==sorted(j):
            if j not in grp:
                grp.append(j)
    print(grp)
#freq ele
nums=[1,2,2,3,3,3]
k=2
uni=[]
for i in nums:
    if i not in uni:
        uni.append(i)
uni.sort(key=nums.count,reverse=True)#how many times the num appenrs
print(uni[:k])
#sudoku
board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
for row in board:
    new=[]
    for num in row:
        if num in new:   
            print("invalid sudoku")
            break
        else:
            new.append(num)
    
#parking
class parkingSystem:
    def __init__(self,big,medium,small):
        self.big=big
        self.medium=medium
        self.small=small
    def addCar(self,carType):
        if carType==1 and self.big>0:
            self.big-=1
            return True
        elif carType==2 and self.medium>0:
            self.medium-=1
            return True
        elif carType==3 and self.small>0:
            self.small-=1
            return True
        return False
big=int(input("enter slots:"))
medium=int(input("enter slots:"))
small=int(input("enter slots:"))
p=parkingSystem(big,medium,small)
carType=int(input("enter car type:"))
print(p.addCar(carType))


#design browsw hist
class BrowserHistory:
    def __init__(self,homepage):
    def visit(self,url):
    def back(self,steps):
    def forward(self,steps):
        
#pract
#palindrome
x=input("ENter a word: ")
for i in x:
    if x==x[::-1]:
        print("palinfrome")
        break
    else:
        print("not palindrome")
        break
#anagram
a=input("enter a word:")
b=input("enter another word:")
if sorted(a)==sorted(b):
    print("anagram")
else:
    print("not anagram")
#duplicate
num=[1,2,3]
for i in num:
    if num.count(i)>1:
        print("duplictes found")
        break
    else:
        print("duplicates not found")
        break
#rev string
i="hello"
for letter in i:
   print(i[::-1])
   break
#freq  count
w="apple"
for letter in w:
    print(letter,w.count(letter))

#max num
ex=[11,2,5,3,9,5,1]
print(max(ex),"is max",min(ex),"is min")

#sorting
s=[22,19,34,39,10,32]
print(sorted(s))
#lar num

x=[22,19,34,39,10,32]
x.sort()
print(x[-2])

#linear search
l=[22,19,34,39,10,32]
target=10
found=False
for i in l:
    if i==target:
        found=True
if found:
    print("ele found")
else:
    print("ele not found")
    
#find index
i=[5,8,2,9]
target=8
for x in i:
    if x==target:
        print(i.index(target))
        
t=[2,1,2,3,2,1,1]
count=0
for i in t:
    if t.count(i)>1:
        count+=1
print(count)
    
#search w in li
ex=["apple","banana","grape"]"""
class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		nums[:] = sorted(set(nums))
		return len(nums)        
class Solution:
    def numberOfSteps(self, num: int) -> int:
        step_count=0
        while num!=0:
            if num%2==0:
                num=num//2
                res=num
            else:
                num=num-1
            step_count+=1
        return step_count
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum=nums[0]
        max_sum=nums[0]
        for num in nums[1:]:
            current_sum=max(num,current_sum+num)
            max_sum=max(max_sum,current_sum)
        return max_sum
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        lis=[]
        for num in range(left,right+1):
            temp=num
            valid=True
            while temp>0:
                digit=temp%10
                if digit==0 or num%digit!=0:
                    valid=False
                temp=temp//10
            if valid:
                lis.append(num)
        return lis
#leet
    
class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):

            return False

        char_to_word = {}

        word_to_char = {}

        for ch, word in zip(pattern, words):

            if ch in char_to_word:

                if char_to_word[ch] != word:

                    return False

            else:

                char_to_word[ch] = word

            if word in word_to_char:

                if word_to_char[word] != ch:

                    return False

            else:

                word_to_char[word] = ch

        return True
def compareTriplets(a, b):
    alice=0
    bob=0
    for i in range(3):
        if a[i]>b[i]:
            alice+=1
        elif a[i]<b[i]:
            bob+=1
    return [alice,bob]
def quickSort(arr):
    left = []
    equal = []
    right = []
    p=arr[0]

    for ele in arr:
        if ele<p:
            left.append(ele)
        elif ele>p:
            right.append(ele)
        else:
            equal.append(ele)
    return left+equal+right

def getTotalX(a, b):

    count = 0

    for num in range(max(a), min(b) + 1):

        valid = True

        for x in a:

            if num % x != 0:

                valid = False

        for y in b:

            if y % num != 0:

                valid = False

        if valid:

            count += 1

    return count
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        if m*n!=r*c:
            return mat
        flat=[]
        for row in mat:
            for ele in row:
                flat.append(ele)
        res=[]
        for i in range(0,len(flat),c):
            res.append(flat[i:i+c])
        return res

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for row in grid:
            for i in row:
                if i<0:
                    count+=1
        return count        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for ch in letters:
            if ch>target:
                return ch
        return letters[0]

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):

                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]
        return nums        
t=int(input())
for _ in range(t):
    n,x=map(int,input().split())
    arr=list(map(int,input().split()))
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    print(n-ans)
##DSA####


#Searching algorithms


#1. Linear seaarch
"""

arr = list(map(int,input().split()))

t = int(input())

for i in range(len(arr)):
    if arr[i]==t:
        print(i)

"""

#2 Binary Search
"""
arr = list(map(int,input().split()))

t = int(input())


l = 0
r = len(arr)-1

while l<=r:
    m = (l+r)//2

    if arr[m]==t:
        print(m)
        break
    elif arr[m]<t:
        l = m+1
    else:
        r = m-1
"""

#Sorting----Techiques


#arr = [1,5,6,7,3,2] ------------------------------main
#      [1,5,6,3,7,2]
#      [1,5,6,3,2,7]---jth => i=0 --> 6-(i+1) = n-i-1

#      [1,5,3,6,2,7]
#      [1,5,3,2,6,7] => i=1

#      [1,3,5,2,6,7]
#      [1,3,2,5,6,7] => i=2

#      [1,2,3,5,6,7] => i=3

#      [1,2,3,5,6,7] => i=4

#      [1,2,3,5,6,7] => i=5

"""
i=0
last 1
i=1
last 2
"""

def bubblesort(arr): 
    n = len(arr)#6
    for i in range(n): #6 #0-5---0,1,2,3,4,5 ====> n 
        for j in range(0, n-i-1): #I=0,1 ---> 1====0 ===> (n-i-1)
            if arr[j]>arr[j+1]: #
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr
        
arr = list(map(int,input().split()))
print(bubblesort(arr))

# time complexity = o(n)*o(n-i-1) = O(n2)


    
n = 5

lst = [1,2,3,4,5]

       0 1 2 3 4

       l   m   r

       

       

isbadversion(m)== true or false
---> true = right = mid-1
---> false = left = mid+1


#Selection sort------

#arr = [20,12,10,15,2] --len=5

#arr = [2,12,10,15,20] --i=0 ===5-2== n-i-1=3

#arr = [2,10,12,15,20] --i=1

#arr = [2,10,12,15,20] --i=2

#arr = [2,10,12,15,20] --i=3

#arr = [2,10,12,15,20] --i=4

#time complexity: --- o(n)*o(n-i-1)= O(n*(n-i-1))= O(n2)



def selection_sort(arr):
    n = len(arr) #5
    for i in range(n): #0-5 ====> i=0,1,2,3 ---n
       min_idx = i #2
       for j in range(i+1,n): #3-5 ====>j=3,4 ---n-i-1
           if arr[j] < arr[min_idx]: #arr[4]<arr[2] ==> 20<12
               min_idx = j #
       arr[i],arr[min_idx] = arr[min_idx], arr[i]# arr[2],arr[2]= arr[2],arr[2] ==>
    return arr
       
    

ls = list(map(int,input().split()))
print(selection_sort(ls))

arr = [5, 3, 4, 1, 2]

for i in range(1, len(arr)):

    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:

        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

print(arr)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new=[]
        for i in nums:
            new.append(i*i)
        new.sort()
        return new
        