import visual
from scipy import *
"""
generation de point pseudoaleatoire en 3 dimensions dans un domaine  ellitique
"""
#defini la scene 
sehatra=visual.display()
"""
les constantes
"""
#nombre d'iteration
N=10000#21122174
#parametres de precesion
LAMBDA=1/1221
#longueur d'u segment  par etape
LONGUEUR=5*10**(-7)
"""
fin constantes
"""
#les axes
A=7
B=3
C=8
#position initial
(x_init,y_init,z_init)=(0,0,0)
#initialisation des parametres 
nutation=0
precesion=pi
rayon=0
#boucle de parcourt pour simuler le deplacement

for compteur in range(N):
#while True:
	visual.rate(10)
	A=LONGUEUR*1/3*rand()
	B=LONGUEUR*1/2*rand()
	C=LONGUEUR*1/5*rand()
	x=14573*rand()
	y=rand()
	angle_nutation=(x*2*pi)/(1+abs(x))
	angle_precesion=exp(-LAMBDA*y)*2*pi
	x_translat=rand()
	y_translat=rand()
	z_translat=rand()
	x_fin=A*sin(angle_nutation)*cos(angle_precesion)+x_translat
	y_fin=B*sin(angle_nutation)*cos(angle_precesion)+y_translat
	z_fin=C*cos(angle_nutation)+z_translat
        line=visual.curve(pos=[(x_init,y_init,z_init),(x_fin,y_fin,z_fin)],color=visual.color.blue)
	(x_init,y_init,z_init)=(x_fin,y_fin,z_fin)
visual.show=True


