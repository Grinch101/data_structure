# Because each of the triply-nested for loops runs exactly n iterations,
#  and each execution takes constant time, the SQUARE-MATRIX-MULTIPLY procedure takes O(n^3) time.
#   You might at first think that any matrix multiplication algorithm must take O(n^3) time,
#   since the natural definition of matrix multiplication requires that many multiplications.
#    You would be incorrect, however: we have a way to multiply matrices in O(n^3) time.
#     We shall see Strassen’s remarkable recursive algorithm for multiplying n x n matrices.
#     It runs in O(n^lg7) time, Strassen’s algorithm runs in O(n^2.81) time,
#      which is asymptotically better than the simple SQUARE-MATRIXMULTIPLY procedure.

import numpy as np

def squarify_and_split(mat):

    n = int(mat.shape[0]/2)
    return mat[:n,:n], mat[:n, n:], mat[n:, :n], mat[n:, n:]

def strassen_multiply(A, B):
    if A.shape[0] == 1:
        return A*B
    else:
        a,b,c,d = squarify_and_split(A)
        e,f,g,h = squarify_and_split(B)

        p1 = strassen_multiply(a, f - h)  
        p2 = strassen_multiply(a + b, h)        
        p3 = strassen_multiply(c + d, e)        
        p4 = strassen_multiply(d, g - e)        
        p5 = strassen_multiply(a + d, e + h)        
        p6 = strassen_multiply(b - d, g + h)  
        p7 = strassen_multiply(a - c, e + f)  
    
        # Computing the values of the 4 quadrants of the final matrix c
        c11 = p5 + p4 - p2 + p6  
        c12 = p1 + p2           
        c21 = p3 + p4            
        c22 = p1 + p5 - p3 - p7

        C = np.vstack( ( np.hstack((c11,c12)), np.hstack((c21,c22)) ) )
        return C
    
########################
# test:
A = np.array([i for i in range(1,17)]).reshape((4,4))
B = np.array([i for i in range(1,17)]).reshape((4,4))

C_1 = strassen_multiply(A,B)
C_2 = np.dot(A,B)

print(C_1 == C_2)