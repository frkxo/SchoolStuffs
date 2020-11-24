'''
    author: Frrkxo
    created: 24.11.2020
'''

MAX = 100

def printtMatrices(M, rowSize, colSize):
    for i in range(rowSize):
        for j in range(colSize):
            print(M[i][j], end=" ")

        print()

#for matrix multiplication
def multiplyMatrices(row1, col1, A,
                     row2, col2, B):
    C = [[0 for i in range(MAX)] for j in range(MAX)]

    #checking the multiplication is possible
    if(row2 != col1):
        print("Not possible!")
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



        






