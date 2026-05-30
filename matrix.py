#add
matrix=[[1,2],[3,4]]
tot=0
for i in matrix:
    for ele in i:
        tot+=ele
print(tot)

#max
matrix=[[1,2],[3,4]]
max_ele=matrix[0][0]#i and j
for i in matrix:
    for ele in i:
        if ele>max_ele:
            max_ele=ele
print(max_ele)

#matrix
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
res=[[0,0],[0,0]]
for i in range(len(a[0])):
    for j in range(len(b)):
        for k in range(len(b[0])):
            res[i][j]=a[i][k]*b[k][j]
print(res)