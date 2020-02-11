from scipy import sqrt, linspace, zeros
import pylab

a=1
N=500
t=linspace(0.6,3,N)
z=zeros(N)

def f(x):
     return a*(x/(x**2-0.25)**2-1/x**3)

z=f(t)

pylab.plot (t,z,'b')
pylab.show()



