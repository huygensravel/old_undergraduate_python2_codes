from scipy import sqrt, linspace, zeros
import pylab

a=1
N=100
t=linspace(0.5,4,N)
z=zeros(N)
y=zeros(N)

def f(x):
     return a*(1/x)**3

def g(x):
     return a/((x**2+0.25)*sqrt(x**2+0.25))

z=f(t)
y=g(t)

pylab.plot (t,z,'b')
	pylab.plot (t,y,'r')
pylab.show()


