import sys
import os

# Adds the parent directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from numpy import linspace, concatenate, array
import numpy as np
import Solvers.algmethods as am

def linear(data,x_axis):
    new_axis=[]
    new_data=[]
    for i in range(0, len(data)-1):
        x=linspace(x_axis[i],x_axis[i+1],10)
        new_data.append((((x_axis[i+1]-x)*data[i]+(x-x_axis[i])*data[i+1])/(x_axis[i+1]-x_axis[i])))
        new_axis.append(x)
    return concatenate(new_data),concatenate(new_axis)


def linear_vector(data,x_axis,specific_point= None):
    new_axis=[]
    new_data=[]
    start_points=x_axis[:-1]
    end_points=x_axis[1:]      
    start_data=data[:-1]
    end_data=data[1:] 

    if specific_point is None:
        x=linspace(start_points,end_points,10)
        new_data=(((end_points-x)*start_data+(x-start_points)*end_data)/(end_points-start_points))
        return new_data,x
    else:
        idx = np.int_(np.floor((specific_point - x_axis[0]) / (x_axis[1] - x_axis[0]))) 
        new_data=(((x_axis[idx+1]-specific_point)*data[idx]+(specific_point-x_axis[idx])*data[idx+1])/(x_axis[idx+1]-x_axis[idx]))
        return new_data


def Lagrange(data,x_axis):
    polynominal_term=1
    polynominal=0
    x=linspace(x_axis[0],max(x_axis),1000)
    for i in range(0,len(data)):
        for j in range(0,len(x_axis)):
            if i != j:
                temp=(x-x_axis[j])/(x_axis[i]-x_axis[j])
                polynominal_term = polynominal_term*temp
        polynominal += polynominal_term * data[i]
        polynominal_term=1
    return polynominal,x



#need to get to chapeter 6 cant use chapter 5 differenation as does not guarentee continunity
def spline(data,x_axis,specific_point= None):

    size=len(x_axis)
    #creating the matrix and vector to solve
    b_vec=np.zeros(size)
    matrix=np.zeros((size,size))
    #creating the arrays to place our results
    f=np.array([])
    x_ax=np.array([])

    #inital conditions
    matrix[0,0]=1
    b_vec[0]=0
    matrix[size-1,size-1]=1
    b_vec[size-1]=0 

    #creating the matrix and vector to solve
    for i in range(1,len(x_axis)-1):
        b_vec[i]=(((data[i+1]-data[i])/(x_axis[i+1]-x_axis[i]))-((data[i]-data[i-1])/(x_axis[i]-x_axis[i-1])))
        matrix[i,i-1:i+2]=([x_axis[i+1]/6-x_axis[i]/6,x_axis[i+1]/3-x_axis[i-1]/3,x_axis[i]/6-x_axis[i-1]/6])

    #solving the equations
    solution=am.LU_decomp_doo(matrix,b_vec)

    #checking if you want lines to be made or the value at a specific point
    if specific_point is None:
        for i in range(0,size-1):
            x=linspace(x_axis[i],x_axis[i+1],80)

            A=((x_axis[i+1]-x)/(x_axis[i+1]-x_axis[i]))
            B=((x-x_axis[i])/(x_axis[i+1]-x_axis[i]))
            C=((1/6)*(A**3-A)*(x_axis[i+1]-x_axis[i])**2)
            D=((1/6)*(B**3-B)*(x_axis[i+1]-x_axis[i])**2)

            f=np.append(f,A*data[i]+B*data[i+1]+C*solution[i+1]+D*solution[i])
            x_ax=np.append(x_ax,x)
        return f,x_ax
    else:
        idx = np.int_(np.floor((specific_point - x_axis[0]) / (x_axis[1] - x_axis[0]))) 
        A=((x_axis[idx+1]-specific_point)/(x_axis[idx+1]-x_axis[idx]))
        B=((specific_point-x_axis[idx])/(x_axis[idx+1]-x_axis[idx]))
        C=((1/6)*(A**3-A)*(x_axis[idx+1]-x_axis[idx])**2)
        D=((1/6)*(B**3-B)*(x_axis[idx+1]-x_axis[idx])**2)

        f=A*data[idx]+B*data[idx+1]+C*solution[idx+1]+D*solution[idx]
        return f



    

