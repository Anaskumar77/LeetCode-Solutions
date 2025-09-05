
matrix = [
[1,1,1],
[2,2,2],
# [3,3,3,3],
[4,4,4]]

def hello(matrix):
    m = matrix
    l = len(m)
    for i in range(l):
        for j in range(l):
            print(i,j,"<+>",j,l-i-1)
            temp = m[i][j]
            m[i][j] = m[j][l-i-1]
            m[j][l-i-1] = temp
    print(m[0],"\n",m[1],"\n",m[2])

hello(matrix)