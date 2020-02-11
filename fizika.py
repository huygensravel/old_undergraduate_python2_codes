import visual
from scipy import *


"""definition de la fonction force en fonction des coordonnees"""
def force(position):
	global K,S
	"""position est le vecteur position"""
	tampon=zeros(3)
	"""les deux denominateurs"""
	denomi_1=sqrt((position[0]*position[0]+(position[1]+S*0.5)*(position[1]+S*0.5)+position[2]*position[2]))**3
	denomi_2=sqrt((position[0]*position[0]+(position[1]-S*0.5)*(position[1]-S*0.5)+position[2]*position[2]))**3

	"""tampon est le vecteur force de composante suivant x tampon[0]
	,suivant y tampon[1],suivant z tampon[2] idem pour le vecteur position"""
	tampon[0]=K*position[0]*(-1/denomi_1 + 1/denomi_2)
	tampon[1]=K*(-(position[1]+S*0.5)/denomi_1 + (position[1]-S*0.5)/denomi_2)
	tampon[2]=K*position[2]*(-1/denomi_1 + 1/denomi_2)
	
	return tampon

"""calcul de la vitesse a partir de la vitesse et position precedente"""
def calculvitesse(vitesseAnterieure,positionAnterieure,masse):

	global PAS
	tampon=zeros(3)
	hery=force(positionAnterieure)
	for i in range(3):
		tampon[i]=PAS*hery[i]*1/masse
		tampon[i]=vitesseAnterieure[i]+tampon[i]

	return tampon


"""calcul les positions a l'aide de l'approximation avec la formul de Taylor de degree 1"""
def position(vitesseAnterieure,positionAnterieure):
	
	global PAS
	tampon=zeros(3)
 	for i in range(3):
		tampon[i]= positionAnterieure[i]+PAS*vitesseAnterieure[i]

	return tampon


"""effectue l'iteration , valeur de retour les vecteurs positions"""
def iteration(vitesseInitiale,positionInitiale,masse):
	
	global IT,position
	

	a=zeros(3)
	b=zeros(3)
	LesPositions=[]
	LesVitesses=[]
	#LesAccelerations[]
		
	LesPositions.append(positionInitiale)
	LesVitesses.append(vitesseInitiale)
	compteur=0
	print LesVitesses,LesPositions

	"""boucle de recherche pour effectuer les IT iterations """
	#position=vectorize(position)
	#calculvitesse=vectorize(calculvitesse())
	while compteur<IT-1:
		print LesVitesses[compteur],LesPositions[compteur]
		print "\n"
		a=position(LesVitesses[compteur],LesPositions[compteur])
		LesPositions.append(a)
		b=calculvitesse(LesVitesses[compteur],LesPositions[compteur],masse)
		LesVitesses.append(b)
                compteur=compteur+1

	return LesPositions
	
	
"""fonction faisant la lecture des position et vecteur initiale , valeur de retour ces valeurs"""	

def lectureCondition(vitesse,position):

	position=input("\n entrer la position initiale \t ")
		
	vitesse=input("\n entrer la vitesse initiale \t ")

	print "\n"

"""fonction effectuant la lecture des donnees initiales"""
def entree(vitesse,Position):
	
	print "\n"
	vitesse=input("entree la vitesse initiale \t")
	Position=input("\n entree la position initiale \t")
	

"""fonction effectuant la simulation et calculant les positions"""
def graphisme(vitesse,Position,masse):

	sehatra=visual.display()
	LesPositions= iteration(vitesse,Position,masse)
	chargeNeg=visual.sphere()
	chargeNeg.visible=False
	chargePos=visual.sphere()
	chargePos.visible=False
	chargePos.color=(0,0,79)
	chargeNeg.color=(0,0,79)
	particule=visual.sphere()
	particule.visible=False
	chargeNeg.pos = (0, -0.5, 0)
	chargeNeg.radius = 0.1
	chargePos.pos = (0, 0.5, 0)
	chargePos.radius=0.1
	chargeNeg.visible=True
	chargePos.visible=True
	particule.radius=0.07
	particule.color=(79,0,0)
	particule.visible=True
	axisX = visual.curve( pos=[ (-5, 0, 0), (5, 0, 0) ], color= visual.color.green)
	axisY = visual.curve( pos=[ (0, -5, 0), (0, 5, 0) ], color= visual.color.green)
	axisZ = visual.curve( pos=[ (0, 0, -5), (0, 0, 5) ], color= visual.color.green)
	for compteur in range(1,len(LesPositions)):
			visual.rate(10)
			posiIniti=tuple(LesPositions[compteur-1])
			posiFinal=tuple(LesPositions[compteur])
			trajectoire = visual.curve(pos=[posiIniti,posiFinal],color= visual.color.blue)
			particule.pos=posiFinal
			#trajectoire.append( pos= (5, 0, 0) )
	sehatra.show()

#__________fonction principale______________________

if __name__=='__main__':

	"""constante K = q^2/4*pi*epsilon_0 , S = ecartement  des deux poles , IT nombre d'iterations ,
	   PAS longueur du pas de discretisation """
	global K,S,IT,PAS
	PAS=0.1
	masse=1
	IT=100
	K=1
	S=1
	vitesse=array([0,0,0]) #vitesse initiale
	Position=array([0,2,0])  #position initiale
        #lectureCondition(vitesse,position)
	print vitesse,Position
	print "\n "
	print "vitesse"
	print  position(vitesse,Position)
	print "\n"
	"""
	LesPositions= iteration(vitesse,Position,masse)
	
	for compteur in range(IT):

		print "\t"
		print LesPositions[compteur]
		print "\n"
	"""
	graphisme(vitesse,Position,masse)


