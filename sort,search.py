


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
"""
"""
    
n = 5

lst = [1,2,3,4,5]

       0 1 2 3 4

       l   m   r

       

       

isbadversion(m)== true or false
---> true = right = mid-1
---> false = left = mid+1

"""

#Selection sort------

#arr = [20,12,10,15,2] --len=5

#arr = [2,12,10,15,20] --i=0 ===5-2== n-i-1=3

#arr = [2,10,12,15,20] --i=1

#arr = [2,10,12,15,20] --i=2

#arr = [2,10,12,15,20] --i=3

#arr = [2,10,12,15,20] --i=4

#time complexity: --- o(n)*o(n-i-1)= O(n*(n-i-1))= O(n2)

"""

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
"""               
    

#Insertion sort
#arr == [5 4 2 1 6 3] == [5 5 2 1 6 3]===[4 5 2 1 6 3] - i=1

#arr =  [4 5 5 1 6 3] == [4 4 5 1 6 3]===[2 4 5 1 6 3] - i=2

#arr =  [2 4 5 5 6 3] == [2 4 4 5 6 3]===[1 2 4 5 6 3] - i=3

#arr =  [1 2 4 5 6 3]                                  - i=4

#arr =  [1 2 4 5 6 6] == [1 2 4 5 5 6]===[1 2 4 4 5 6] == [1 2 3 4 5 6]
"""
def insertion_sort(arr): 
    n = len(arr)#6

    for i in range(1,n): # 1,6== 1,2,3,4,5
        key = arr[i]#3
        j = i-1#4

        while j>=0 and arr[j]>key:#2>3
            arr[j+1] = arr[j] # 5=4
            j-=1#1

        arr[j+1] = key # arr[2]=3
    return arr
n = list(map(int,input().split()))
print(insertion_sort(n))
        
   """ 



#inserion sort---
"""
1. consider 1st ele as sorted

2. 2nd ele = key

3. compare key ele with elements before it

4. insert if key<prev ele, shift left

5. repeat

"""


#Merge sort--------------------

"""
def merge_sort(arr):# [8,6,4,9,1,2]
    n = len(arr)
    l = 0
    r = n-1
    if n>1:
        mid = (l+r)//2 

        left = arr[:mid+1]
        right = arr[mid+1:]

        #print("before:",left, right)

        merge_sort(left)
        merge_sort(right)

        #print("after", left, right)


        i=j=k=0

        while i< len(left) and j < len(right):
            if left[i]<right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1

            k+=1

        while i< len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k] = right[j]
            j+=1
            k+=1

    return arr
  
    
a = [8,6,4,9,1,2]
print(merge_sort(a))

"""

#Quick sort-----------
"""
def quick_sort(arr):
    n = len(arr)
    if n<=1:
        return arr

    pivot = arr[n//2]
    left = []
    middle=[]
    right = []
    for x in arr:
        if x<pivot:
            left.append(x)
        elif x==pivot:
            middle.append(x)

        else:
            right.append(x)
    return quick_sort(left)+middle+quick_sort(right) 
            
a = [8,6,4,9,1,2]
print(quick_sort(a))            
            
"""
#06/07/2026
#counting sort--------------

#arr = [3 3 2 4]

"""
def counting_sort(arr):

    max_val = max(arr)

    count = [0]*(max_val+1) #[0 0 1 2 1]
                            # 0 1 2 3 4

    for num in arr: #3 3 2 4
        count[num]+=1
    

    j= 0
    for i in range(len(count)): #0
        while count[i]>0:
            arr[j] = i
            j+=1
            count[i]-=1

    return arr
a = [8,6,4,9,1,2]
b= [3, 3, 2, 4]
print(counting_sort(a)) 
print(counting_sort(b))             

"""

#Stable counting sort--------------
#a = [3, 3, 2, 4]
"""
def count_sort(arr):

    max_val = max(arr)

    count = [0]*(max_val+1)#[0 0 0 0 0] = [0 0 1 2 1]

    #freq
    for num in arr:
        count[num]+=1

    #cumulative count

    for i in range(1, len(count)): #[0 0 1 3 4]
        count[i]+=count[i-1]

    output = [0]*len(arr)

    #right-left--

    for j in reversed(arr):
        output[count[j]-1] = j
        count[j]-=1

    return output


b= [3, 3, 2, 4]
a = [8,6,4,9,1,2]

print(count_sort(a))
print(count_sort(b)) 
"""


#Radix sort-----------------
"""
def count_sort(arr, place):

    n = len(arr)
    output = [0]*n

    count = [0]*10 #[1 0 0 0 0 0 0 0 0 0]

    for i in range(0,n):
        index = arr[i]//place
        count[index%10]+=1

    for i in range(1,10):
        count[i]+=count[i-1]


    i = n-1

    while i>=0:

        ind = arr[i]//place
        output[count[ind%10]-1] = arr[i]
        count[ind%10]-=1
        i-=1

    for i in range(0,n):
        arr[i]= output[i]
        
    
        
def radix_sort(arr):
    max_ele = max(arr)

    place =1

    while max_ele//place>0:
        count_sort(arr, place)
        place*=10



a = [8,6,4,9,1,2]
b = [100, 201, 1, 810, 904, 6, 25]
radix_sort(b)
print(b)
"""



#Quick sort---Lomuto

"""


def lomuto(arr, low, high):

    pivot = arr[high]
    i = low-1

    for j in range(low, high-1):
        if arr[j]<=pivot:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    print(arr,i+1)
    return i+1


def quick_sort(arr,low, high):
    if low<high:
        pi = lomuto(arr,low,high)

        quick_sort(arr,low,pi-1)

        quick_sort(arr, pi+1, high)


    
a = [50,20,60,10,40]
print(quick_sort(a, 0, len(a)-1))


"""

#time complexity -- O(n) for complete ele traverse, O(logn) for partitioning ===> O(nlogn)

#Quick sort Hoare
"""

def hoare(arr,low,high):
    piv = arr[low]

    i = low-1
    j = high+1

    while True:

        i+=1

        while arr[i]<piv:
            i+=1

        j-=1

        while arr[j]>piv:
            j-=1

        if i>=j:
            return j


        arr[i],arr[j] = arr[j],arr[i]

def quick_sort(arr,low, high):
    
    if low<high:
        pi = hoare(arr,low,high)

        quick_sort(arr,low,pi)

        quick_sort(arr, pi+1, high)

        
a = [50,20,60,10,40]
quick_sort(a, 0, len(a)-1)
print(a)
        
"""



#walrus operator ====> :=,
"""
name = input("")

if len(name)>5:
    print("name:", name)


if (name:=input("enter ur name: ")) and (len(name)>5):
    print("name:", name)

"""

#Two pointers------
#arr must be sorted

"""
arr = list(map(int,input().split()))

target = int(input())

left = 0

right = len(arr)-1


while left<right:

    sum1 = arr[left]+arr[right]

    if sum1==target:
        print(left, right)
        break
    elif sum1<target:
        left+=1

    else:
        right-=1

"""

#valid palindrome------------
"""

def is_pal(s):
    left = 0

    right = len(s)-1

    while left<right:
        if s[left]!=s[right]:
            return False
        else:
            left+=1
            right-=1

    return True



s = input()
if is_pal(s):
    print("palindrome")

else:
    print("not a palindrome")

"""

##container with most water----------------

"""
hts = list(map(int,input().split()))

n = len(hts)

left = 0
right = n-1
max_area = 0

while left<right:

    area = min(hts[left], hts[right])*(right-left)

    max_area = max(area, max_area)

    if hts[left]<hts[right]:
        left+=1
    else:
        right-=1

print(max_area)

"""

#Range sum query------ 1D arr

"""
arr = list(map(int,input().split()))

pref = [0]*len(arr)

pref[0]= arr[0]

for i in range(1,len(arr)):
    pref[i]=pref[i-1]+arr[i]

l = int(input())
r = int(input())

if l==0:
    print(pref[r])

else:
    k = pref[r]-pref[l-1]

    print(k)

"""

#Prefix sum on 2d array------------------Range sum query on 2D arr

"""
def build_pref(matrix):

    rows = len(matrix)
    cols = len(matrix[0])


    prefix = [[0]*cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):


            current = matrix[i][j]

            top = prefix[i-1][j] if i>0 else 0

            left = prefix[i][j-1] if j>0 else 0
            

            top_left = prefix[i-1][j-1] if i>0 and j>0  else 0




            prefix[i][j] = current+top+left-top_left

    return prefix



def query(prefix, r1,c1,r2,c2):

    total = prefix[r2][c2] #22, 36

    top = prefix[r1-1][c2] if r1>0 else 0 #3, 10

    left = prefix[r2][c1-1] if c1>0 else 0 #0, 17

    top_left = prefix[r1-1][c1-1] if r1>0 and c1>0 else 0 #0, 3

    final = total-top-left+top_left #12

    return final

matrix = [
    [3,0,1,4,2],
    [5,6,3,2,1],
    [1,2,0,1,5],
    [4,1,0,1,7],
    [1,0,3,0,5]


    ]

k = build_pref(matrix)
for i in k:
    print(i)


answer = query(k, 1,0,3,1)
print("distance:", answer)


#longest subarr with sum =k: ------------------

def long_subarr(arr,k):

    pref_sum =0

    res_max = 0

    pref_map= {}

    for i in range(len(arr)):

        pref_sum+=arr[i]

        if pref_sum ==k:
            res_max = i+1

        if (pref_sum-k) in pref_map:
            length = i-pref_map[pref_sum-k]
            res_max = max(res_max,length)

        if pref_sum not in pref_map:
            pref_map[pref_sum]=i

    return res_max

arr = list(map(int,input().split()))

k int(input())
print(long_subarr(arr,k))"""

##input:
arr=['a', 'i', 'o', 'r', 't', 'u', 'o']
k=4
def slide(arr,k):
    count=0
    for i in range(k):
        if arr[i] in 'aeiou':
            count+=1
    max_count=count
        
    for i in range(k,len(arr)):
        if arr[i] in 'aeiou':
            count+=1
        if arr[i-k] in 'aeiou':
            count-=1
        max_count=max(max_count,count)
    return max_count
print(slide(arr,k))

#leet
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxi=nums[0]
        
        for i in range(len(nums)):
            product=1
            for j in range(i,len(nums)):
                product*=nums[j]
                if product>maxi:
                    maxi=product
        return maxi
#leet
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1




        