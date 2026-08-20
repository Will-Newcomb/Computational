def backwards_vector(data,stepsize):
    left_side = data[1:]
    right_side = data[:-1]
    diff=(right_side-left_side)/stepsize
    return diff

def forwards_vector(data,stepsize):
    left_side = data[1:]
    right_side = data[:-1]
    diff=(-left_side+right_side)/stepsize
    return diff

def central_vector(data,stepsize):

    central = (backwards+forwards)/2

