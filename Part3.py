import numpy as np


def printMatrix(A, starting_index, rows, columns):
    starting_row = starting_index[0]
    starting_column = starting_index[1]
    C = []
    for i in range(starting_row,rows+1):
        B = []
        for j in range(starting_column,columns+1):
            B.append(A[i][j])
        C.append(B)        
    print(C)


def MatAdd(A,B):
    add = 0
    D = []
    for i in range(len(A)):
        C = []
        for j in range(len(A[i])):
            add = A[i][j] + B[i][j]
            C.append(add)
        D.append(C)
    return D
    
    
def MatAddPartial(A,B,start,size):
    add = 0
    starting_row = start[0]
    starting_column = start[1]
    C = []
    D = []
    for i in range(starting_row,len(A)):
        E = []
        for j in range(starting_column,len(A[i])):
            E.append(A[i][j])
        C.append(E)
    
    for i in range(starting_row,len(B)):
        E = []
        for j in range(starting_column,len(B)):
            E.append(A[i][j])
        D.append(E)
        
    result = MatAdd(C, D)
    return result
            

def MatMul(A,B):
    D = []
    for row in A:
        C = []
        column = 0
        for i in range(len(row)):
            add = 0
            for j in range(len(B)):
                mul = row[j] * B[j][column]
                add = add + mul
            C.append(add)
            column += 1        
        D.append(C)
    return D
  
def MatMulStrassen(A, B):
    if A.size == 1 or B.size == 1:
        return A * B

    n = A.shape[0]

    if n % 2 == 1:
        A = np.pad(A, (0, 1), mode='constant')
        B = np.pad(B, (0, 1), mode='constant')

    m = int(np.ceil(n / 2))
    a = A[: m, : m]
    b = A[: m, m:]
    c = A[m:, : m]
    d = A[m:, m:]
    e = B[: m, : m]
    f = B[: m, m:]
    g = B[m:, : m]
    h = B[m:, m:]
    p1 = MatMulStrassen(a, f - h)
    p2 = MatMulStrassen(a + b, h)
    p3 = MatMulStrassen(c + d, e)
    p4 = MatMulStrassen(d, g - e)
    p5 = MatMulStrassen(a + d, e + h)
    p6 = MatMulStrassen(b - d, g + h)
    p7 = MatMulStrassen(a - c, e + f)
    result = np.zeros((2 * m, 2 * m), dtype=np.int32)
    result[: m, : m] = p5 + p4 - p2 + p6
    result[: m, m:] = p1 + p2
    result[m:, : m] = p3 + p4
    result[m:, m:] = p1 + p5 - p3 - p7

    return result[: n, : n]
        

def main():
    A = np.array([[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]])
    B = np.array([[1, 2, 3, 4], [5, 6, 7, 8],[9, 10, 11, 12], [13, 14, 15, 16]])
    printMatrix(A, (0,1), 2, 2)
    print(MatAdd(A, B))
    print(MatAddPartial(A, B, (1,1), 1))
    print(MatMul(A, B))
    print(MatMulStrassen(A, B))


if __name__ == "__main__":
    main()
    
