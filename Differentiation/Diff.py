import numpy as np

def backwards_vector(data,stepsize):
    left_side = data[1:]
    right_side = data[:-1]
    diff=(left_side-right_side)/stepsize
    result=np.append([0],diff)
    return result

def forwards_vector(data,stepsize):
    left_side = data[1:]
    right_side = data[:-1]
    diff=(left_side-right_side)/stepsize
    return np.append(diff,0)

def central_vector(data,stepsize):

    central = (backwards_vector(data,stepsize)+forwards_vector(data,stepsize))/2
    return central

step_size=10
data=np.array([1,2,3,4,5,6,67,21,3,12])
print(forwards_vector(data, step_size))
print(backwards_vector(data, step_size))
print(central_vector(data, step_size))


