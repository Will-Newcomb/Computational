from cmath import exp, pi


def FFT(f, padding): # f is an array
    f=list(f)
    N = len(f)
    if N & (N-1) != 0 and padding==True:
        Temp=N.bit_length() - 1
        Offset=N-2**Temp
        if Offset>0:
            Temp+=1
            Offset=abs(N-2**Temp)    
            f = f + [0]*Offset
    N=len(f)        
    return FFT_recursion(f), N


def FFT_recursion(f):
    N = len(f)
    if N == 1:
        return [f[0]]

    farray_even = FFT_recursion(f[::2]) # size N/2
    farray_odd = FFT_recursion(f[1::2] ) # size N/2

    farray = [0] * N
    for p in range(0, (N//2)):

        farray[p] = farray_even[p] +exp(1j*2*pi*p/N)*farray_odd[p]
        farray[p+N//2] = farray_even[p] - exp (1j*2*pi*p/N)* farray_odd[p]
    return farray


def DFT(f):
    N=len(f)
    f_tild=[0]*(N)
    for j in range(0,N):
        for i in range(0,N):
            f_tild[j]+=f[i]*exp(1j*2*pi*j*i/N)
    return f_tild
