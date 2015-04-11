# Title:            newtonMethod.py
# Author:           Maples7
# Function:         Calculate the convergence region of x^4-1=0 using Newton Method
# Date:             2015-03-26
# Link:             http://www.cnblogs.com/maples7/

# for drawing picture
import numpy as np
import pylab as pl

pointDiff = 1e-2        # diff for points
buff = pointDiff        # diff for values
times = 10              # maxium times for Loops

# range for x and y
x_down = -2          
x_up = 2
y_down = x_down
y_up = x_up

def f(x):
    """
    f(x) = x^4 - 1
    """
    return (complex)(x*x*x*x-1)

def fd(x):
    """
    f'(x) = 4x^3
    """
    return (complex)(4*x*x*x)

def newtonMethod(x0, n = times, maxiter = pointDiff, tol = buff):
    """
    Newton Method:
    x0:         infinite value of X[n]
    n:          times for Loop
    maxiter:    diff for X[n] - X[n-1]
    tol:        diif for f(x) - 0
    return the solution of f(x) or None (Convergence or Divergence)
    """
    v = f(x0)
    for k in range(n):
        try:
            x1 = x0 - v/fd(x0)
        except:                                     # For fd(x0)=0
            return None
        v = f(x1)
        if abs(x0-x1) < maxiter or abs(v) < tol:    # Convergence
            return x1
        x0 = x1
    return None     # Divergence

def floatrange(start,stop,steps):
    ''' 
    Computes a range of floating value.
        
        Input:
            start (float)  : Start value.
            end   (float)  : End value
            steps (integer): Number of values
        
        Output:
            A list of floats
        
        Example:
            >>> print floatrange(0.25, 1.3, 5)
            [0.25, 0.51249999999999996, 0.77500000000000002, 1.0375000000000001, 1.3]
    '''
    return [start+float(i)*(stop-start)/(float(steps)-1) for i in range(steps)]

points = {}

# Loop for every point in choosen area and determine which part of points it belongs to 
for x in floatrange(x_down, x_up, (int)(4/pointDiff)):
    for y in floatrange(y_down, y_up, (int)(4/pointDiff)):
        x0 = complex(x, y)
        value = newtonMethod(x0)
        if value != None:
            exist = False
            for e in points.keys():
                if e != 'Divergence' and abs(e-value)<pointDiff:
                    points.setdefault(e, []).append(x0)
                    exist = True
                    break
            if not exist:
                points.setdefault(value, []).append(x0)
        else:
            points.setdefault('Divergence', []).append(x0)

# Draw the picture
colors = ['or', 'om', 'ok', 'og', 'ob']
i = 0
plot = []
for e in points.keys():
    color = colors[i]
    x = []
    y = []
    if e != 'Divergence':
        label = str(complex(round(e.real, 2), round(e.imag, 2)))
    else:
        label = e
    for point in points[e]:
        x.append(point.real)
        y.append(point.imag)
    draw = pl.plot(x, y, color, label=label)
    plot.append(draw)
    i += 1
pl.title('The convergence region of x^4-1=0')
pl.xlabel('x: real part')
pl.ylabel('y: imag part')
pl.xlim(x_down, x_up)
pl.ylim(y_down, y_up)
pl.legend(numpoints=1)
pl.show()
             