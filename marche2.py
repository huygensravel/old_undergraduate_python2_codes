import visual
from scipy import *

#definit la scene 
sehatra=visual.display()

N=200


(x_init,y_init,z_init)=(0,0,0)
(x_fin,y_fin,z_fin)=(0,0,0)

#boucle de parcourt pour simuler le deplacement
for compteur in range(N):

	visual.rate(10)
		
	tampon=rand()*4
	"""structure conditionnel controlant la marche aleatoire"""
	if tampon==0 :
		(x_fin,y_fin,z_fin)=(x_init,y_init+1,z_init)
	elif tampon==1 :
		(x_fin,y_fin,z_fin)=(x_init,y_init-1,z_init)
	elif tampon==2 :
		(x_fin,y_fin,z_fin)=(x_init+1,y_init,z_init)
	elif tampon==3 :
		(x_fin,y_fin,z_fin)=(x_init-1,y_init,z_init)

	
	lalana=visual.curve(  pos=[(x_init,y_init,z_init),(x_fin,y_fin,z_fin)], color= visual.color.blue )
       	lalana.visible=True
		
	(x_init,y_init,z_init)=(x_fin,y_fin,z_fin)

visual.show=True
