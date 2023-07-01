class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        #The approach is to take two dummay arrays and store the values of the rows and columns whose value is zero. then traverse the rpws and columns separately and make them zero.
        row=len(matrix)
        col=len(matrix[0])
        r,c=[],[]


        for i in range(row):
            for j in range(col):
                if(matrix[i][j]==0):
                    # print('indexes', i,j)
                    r.append(i)
                    c.append(j)
                    
        # print(matrix)
        for elements in r:
            for j in range(col):
                matrix[elements][j]=0
           
        for elements in c:
            for j in range(row):
                matrix[j][elements]=0

        return matrix
