'''
    author: Frrkxo
    created: 25.11.2020
'''
import numpy as np

s = int(input("For multiply two matrices press 1, for transpose a matrix press 2 ==>"))
 

if(s == 1):
    MAX = 100

    def printtMatrices(M, rowSize, colSize):
        for i in range(rowSize):
            for j in range(colSize):
                print(M[i][j], end=" ")

            print()                             #jump to another line


    #for matrix multiplication
    def multiplyMatrices(row1, col1, A,
                        row2, col2, B):
        C = [[0 for i in range(MAX)] for j in range(MAX)]

        #checking the multiplication is possible
        if(row2 != col1):
            print("There is no resultant matrix!")
            return

        for i in range(row1):
            for j in range(col2):
                C[i][j] = 0
                for k in range(row2):
                    C[i][j] += A[i][k] * B[k][j]      #main computation

        print("Resultant Matrix: ")
        printtMatrices(C, row1, col2)


    #the main code
    if __name__ == "__main__":

        A = [[0 for i in range(MAX)]
                for j in range(MAX)]
        B = [[0 for i in range(MAX)]
                for j in range(MAX)]

        #First matrix input
        row1 = int(input("Enter the number of rows of 1st Matrix: "))
        col1 = int(input("Enter the number of columns of 1st Matrix: "))

        print("Enter the elements of 1st Matrix:")
        for i in range(row1):
            for j in range(col1):
                A[i][j] = int(input("A[" + str(i) + "][" + str(j) + "]: "))

        #Second matrix input
        row2 = int(input("Enter the number of rows of 2nd Matrix: "))
        col2 = int(input("Enter the number of columns of 2nd Matrix: "))

        print("Enter the elements of 2nd Matrix: ")
        for i in range(row2):
            for j in range(col2):
                B[i][j] = int(input("B[" + str(i) + "][" + str(j) + "]: "))

        #first matrix representation
        print("First Matrix: ")
        printtMatrices(A, row1, col1)

        #second matrix representation
        print("Second Matrix: ")
        printtMatrices(B, row2, col2)

        multiplyMatrices(row1, col1, A, row2, col2, B)


elif(s == 2):

    #matrix properties from user
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns:"))

    F = [[0 for i in range(rows)]
            for j in range(cols)]

    #matrix component from user
    print("Enter the elements of Matrix: ")
    for i in range(rows):
        for j in range(cols):
            F[i][j] = int(input("A[" + str(i) + "][" + str(j) + "]: "))

    #input matrix
    print("<------Your Matrix is------>")
    for f in F:
        print(f)

    result = [[0 for i in range(rows)] for j in range(cols)]

    #transpose time
    for r in range(rows):
        for c in range(cols):
            result[c][r] = F[r][c]

    print("Transpose matrix is: ")
    for r in result:
        print(r)


else:
    print("Enter a valid value to make computation!!!")    