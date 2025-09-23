def MySolution(matrix):
    height = len(matrix)
    width = len(matrix[0])

    rows = set()
    columns = set()
    for m in range(height):
        for n in range(width):
            if matrix[m][n] == 0:
                rows.add(m)
                columns.add(n)
    for m in range(height):
        for n in range(width):

            if m in rows:
                matrix[m][n] = 0
            if n in columns:
                matrix[m][n] = 0
  
    return matrix

      
print(MySolution([[0,1,2,0],[3,4,5,2],[1,3,1,5]]) )   


def TopSolution(matrix):
        m=len(matrix)
        n=len(matrix[0])
        row=[0]*m
        col=[0]*n
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row[i]=1
                    col[j]=1
        for i in range(m):
            for j in range(n):
                if row[i]==1 or col[j]==1:
                    matrix[i][j]=0
        return matrix