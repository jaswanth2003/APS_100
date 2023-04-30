def booleanMatrix(matrix):
     
    r= len(matrix)
    c=len(matrix[0])
    row=[0]*r 
    col=[0]*c 
    # print( r,c)
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==1:
                row[i]=1
                col[j]=1
                 
    for i in range(r):
        for j in range(c):
            if row[i]==1 or col[j]==1:   
                matrix[i][j]=1
         
            


 

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        matrix = []
        for i in range(r):
            line = [int(x) for x in input().strip().split()]
            matrix.append(line)
        booleanMatrix(matrix)
        for i in range(r):
            for j in range(c):
                print(matrix[i][j], end=' ')
            print()