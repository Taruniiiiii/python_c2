#two sum
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
            break
    
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


"""#design browsw hist
class BrowserHistory:
    def __init__(self,homepage):
    def visit(self,url):
    def back(self,steps):
    def forward(self,steps):
        
"""