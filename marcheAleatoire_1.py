from scipy import *
import pylab

T=25
x=zeros(T)
y=zeros(T)

for i in range(1,T):
	tampon=rand()*4

	if tampon==0 :
		x.append(x[i-1]+1)
	elif tampon==1 :
		x.append(x[i-1]-1)
	elif tampon==2 :
		y.append(x[i-1]-1)
	elif tampon==3 :
 		y.append(x[i-1]+1)	

	pylab.plot(x,y,'b')
pylab.show()
