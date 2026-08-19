from numpy import linspace, concatenate

def linear(data,x_axis):
    new_axis=[]
    new_data=[]
    for i in range(0, len(data)-1):
        x=linspace(x_axis[i],x_axis[i+1],100)
        new_data.append((((x_axis[i+1]-x)*data[i]+(x-x_axis[i])*data[i+1])/(x_axis[i+1]-x_axis[i])))
        new_axis.append(x)
    return concatenate(new_data),concatenate(new_axis)


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



#need to get to chapeter 6
def spline(data,x_axis):
    new_axis=[]
    new_data=[]
    for i in range(0, len(data)-1):
        x=linspace(x_axis[i],x_axis[i+1],100)
        a=(x_axis[i+1]-x)/(x_axis[i+1]-x_axis[i])
        b=(x-x_axis[i])/(x_axis[i+1]-x_axis[i])
        c=(1/6)*(a**3-a)(x_axis[i+1]-x_axis[i])**2
        d=(1/6)*(b**3-b)(x_axis[i+1]-x_axis[i])**2

        new_data.append(a*data[i]+b*data[i+1]+c*+d)
        new_axis.append(x)
    return concatenate(new_data),concatenate(new_axis)


    

