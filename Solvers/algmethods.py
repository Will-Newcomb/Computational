import numpy as np

def Diagonal_solver(Matrix,b_vector):
    diagnoal=np.diagonal(Matrix)
    solution=b_vector/diagnoal
    return solution

def lower_diag(Matrix, B_vector):
    solution=[]
    diag=np.diagonal(Matrix)
    solution.append(B_vector[0]/diag[0])

    for i in range(1,len(B_vector)):
        temp=np.dot(Matrix[i,:i], solution)
        solution.append((B_vector[i]-temp)/diag[i])
    return solution

def upper_diag(Matrix, B_vector):
    size=len(B_vector)
    solution = np.zeros(len(B_vector))
    diag=np.diagonal(Matrix)

    solution[size-1]=(B_vector[size-1]/diag[size-1])
    for i in range(size-2,-1,-1):
        temp=np.dot(Matrix[i,i:],solution[i:])
        solution[i]=((B_vector[i]-temp)/diag[i])
    return solution



def determent(Matrix):
    det=0
    if np.shape(Matrix)[0]==2:
        return (Matrix[0,0]*Matrix[1,1]-Matrix[1,0]*Matrix[0,1])

    for j in range(len(Matrix)):
        minor = np.delete(Matrix,0,0)
        minor = np.delete(minor,j,1)
        det += ((-1)**j) * Matrix[0, j] * determent(minor)
    return det


def cofactor_minor(Matrix,B_vector):
    rows=np.shape(Matrix)[0]
    cofac=np.zeros((rows,rows))
    for i in range(rows):
        for j in range(rows):
            minor = np.delete(Matrix,i,0)
            minor = np.delete(minor,j,1)
            det=determent(minor)
            cofac[i,j]=det*(-1)**(i+j)
    det=np.dot(cofac[0],Matrix[0])
    inverse_matrix=np.transpose(cofac*(1/det))
    Solution = np.matvec(inverse_matrix, B_vector)
    return Solution


def LU_decomp_doo(Matrix,B_matrix):
    size=len(Matrix)
    L=np.zeros((size,size))
    U=np.zeros((size,size))
    x=np.zeros(size)
    np.fill_diagonal(L,1)

    for j in range(0,size):
        for i in range(0,j+1):
            U[i,j]=Matrix[i,j]-np.dot(L[i,:i], U[:i, j])

        for i in range(0,size):
            L[i,j]=(1/U[j,j])*(Matrix[i,j]-np.dot(L[i, :j], U[:j, j]))

    sol=lower_diag(L,B_matrix)
    sol=upper_diag(U,sol)
    return sol



        