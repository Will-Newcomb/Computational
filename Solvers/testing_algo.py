import numpy as np
import algmethods as am

matrix=np.array([[12,2,3],
                 [1,3,12],
                 [1,4,8]])


B_matrix=[1,2,3]
det=am.determent(matrix)
what=am.LU_decomp_doo(matrix,B_matrix)
print(what)

#soltution= am.Diagonal_solver(matrix, B_matrix)
#print(soltution)