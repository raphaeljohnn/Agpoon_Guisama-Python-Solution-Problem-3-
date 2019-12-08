# Approximating the data according to the least-norm
# error vector
import numpy as np
import math
# element input 
def approximate(element):
# Set the coefficients of the first column to x
    x = element[:,0]
# Set the coefficients of the seocond column to y
    y = element[:,1]
# Set the least norm to infinity 
    least=math.inf
# loop i in the degree of x from 0-10
    for i in range(0,10):
        if i == len(x):
            break
        p=np.polyfit(x,y,i)
        y2=np.polyval(p,x)
# compute for the error vector
        error = y-y2
        errorvector=np.linalg.norm(error)
        if errorvector<least:
            least=errorvector
            bestfit=p
    print(bestfit)