from scipy import zeros,array,sqrt
import visual


"""projet physique 2 AIMS V  """


"""question 1 : calcul approximatif  du champ cree par une
distribution  lineique continue de charge en faisant une
 discretisation suffisante de la ligne"""

"""calcul du module d'un vecteur"""
def module(vecteur):
	
	tampon=sqrt(vecteur[0]*vecteur[0]+vecteur[1]*vecteur[1]+vecteur[2]*vecteur[2])		
        return tampon

assert(module(array([1,1,1]))==sqrt(3))
	
"""calcul du champ cree par un point """
def champPonctuel(distance,charge):

	#k constante 
	k=1
	tampon=zeros(3)
	"""boucle de parcourt pour calculer tout les composantes 
	du vecteur champ"""
	
	for i in range(3):
		tampon[i]=distance[i]
	tampon_2=module(distance)
	tampon=1/(tampon_2*tampon_2*tampon_2)*k*charge*tampon
	return tampon

assert(any(champPonctuel(array([1,0,0]),1)==array([1,0,0])))

