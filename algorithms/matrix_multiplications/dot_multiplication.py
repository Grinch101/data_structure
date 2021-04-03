# Because each of the triply-nested for loops runs exactly n iterations, 
# and each execution of line 7 takes constant time,
#  the SQUARE-MATRIX-MULTIPLY procedure takes O(n^3) time.


import numpy as np

def dot_multiplication(A,B):
    
    C_nrow = A.shape[0]
    C_ncol = B.shape[1]
        
    C = np.array([0 for i in range(0, C_ncol*C_nrow)])
    C = C.reshape((C_nrow, C_ncol))
    output = 0
    for j in range(0, C_ncol):
        for i in range(0, C_nrow ):
            output = 0
            for idx in range(A.shape[1]):
                output = output + A[i,:][idx] * B[:,j][idx]
            C[i,j] = output

    return C




############################################
# ### Test:
# A = np.array([i for i in range(1,11)])
# A = A.reshape((5,2))

# B = np.array([i for i in range(1,21)])
# B = B.reshape((2,10))

# C1 = dot_multiplication(A,B)
# C2 = np.dot(A,B)

# print(C1 == C2)
