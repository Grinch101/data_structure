import numpy as np
import math 

# # find the closest power 2
# def closest_power(tup):
#     max_side = max(tup[0],tup[1])
#     i = 1
#     while True:
#         if math.log(max_side + i , 2) == round(math.log(max_side + i , 2)):
#             output = i + max_side
#             break
#         else: i += 1
#     return output

# squarify a mat and fill with zeros
def squarify_and_split(mat):
    # shape = mat.shape
    # power = closest_power(shape)
    
    # # define a Zero matrix:
    # square_mat = np.zeros((power,power))
    # # broadcast:
    # square_mat[:shape[0] , :shape[1]] = mat
    
    square_mat = mat
    new_shape = mat.shape
    row = new_shape[0]//2
    col = new_shape[1]//2

    return square_mat[:row,:col], square_mat[:row, col:2*col], square_mat[row:2*row, :col] , square_mat[row:2*row, col:2*col]

def strassen_multiply(A, B):
    if len(A) == 1:
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