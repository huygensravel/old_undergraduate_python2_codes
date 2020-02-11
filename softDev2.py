
#programme de gestion des membres d'une societe 
from math import sqrt
import pylab 

"""
on utilisera un dictionnaire pour contenir tout les membres et les clefs seront les noms des membres

de meme pour les attributs de chaque membre on utilisera egalement un dictionnaire comme conteneur et les clefs serontegalements les noms des membres

"""

#=========pour gobal voir le main programme=================
def ajout_membre(nouv_membre):
	"""
	ajout d'un membre , le nouveau membreest deja un dictionnaire 
	"""
	global membre,nom
	membre[nouv_membre[nom]]=nouv_membre

def supr_membre(nom_membre=""):	
	"""
	suppression d'un membre en donnant son nom (les clefs sont les noms)
	sans valeur de retour ,supprime simplement l'entite indexe par nom_membre du dictionnaire des membres
	"""
	global membre
	del membre[nom_membre]

def rechercheParNom(Nom=""):
	"""
	recherche d'un membre par sa clef qui est son nom 
	retourne 
	"""
	global membre,nom
	return membre.has_key(Nom)

def rechercheParAge(Age):
	"""
	recherche des membres ayant le meme age Age
	retourne ces membres sous forme de liste
	"""
	global membre,nom,age
	resultat=[] 						#initialise un liste vide
	for element in membre:
		"""
		boucle de parcour pour tester tout les membres
		"""
		if  Age==membre[element][age] :                
			"""
			teste si le membre a l'age Age et l'ajoute a la liste de retour si  oui
			"""
			resultat.append(membre[element][nom])

	return resultat	

def collectAge():
	"""
	collecte les ages des membres, il peut y avoir des doublon : Comment l'eviter?
	retourn les valeurs trouver sous forme de liste
	"""
	global membre,age
	listAge=[]
	for element in membre:
		listAge.append(membre[element][age])
	return listAge


def Average(variable_Al):
	"""
	calcul et retourne la moyenne d'une varieble aleatoire discrete a loi uniforme
	la variable est donne sous forme de liste en parametre en entree 
	"""
	count=0
	for valeur in variable_Al:
		count+=valeur 
	return count/len(variable_Al)

def ecart_type(variable_Al):
	"""
	calcul et retourne l'ecart type d'une varieble aleatoire discrete a loi uniforme
	la variable est donne sous forme de liste en parametre en entree 
	"""
	count=0
	average=Average(variable_Al)
	for valeur in variable_Al:
		count+=(valeur-average)**2 
	variance=count/len(variable_Al)
	return sqrt(variance)

def Min_liste(liste):
	"""
	retourne le minimum d'une liste
	n'est pas utilise ici mais utiliser lors de la conception pour certains tests
	"""
	minimum=liste[0]
	for count in range(len(liste)):
		if liste[count]<minimum:
			minimum=liste[count]
	return minimum,count

def permut(premier,dernier): 
	"""
	permut le contenue de deux variable : premier et dernier,sans valeur de retour
	"""
 	parm=premier
 	premier=dernier
 	dernier=parm


def trie_croissant(liste):
	"""
	trie d'une liste par selection , on prend le plus petit et en le met en 1ere place et on fait de meme avec le restes de la liste.
	"""

	for place_definitive in range(len(liste)):
	    """
	    boucle de parcour pour repeter l'operation  len(liste) fois
	    """	
  	    idx_minimum=place_definitive	#initialisation de l'index du minimum a l'etape place_definitive+1  (si on compte a partir de 1)

	    for i in range(len(liste)) :
		"""
		boucle de parcour pour tester le reste de la liste
		"""

		if(liste[i]>liste[idx_minimum]):
			idx_minimum=i   
			tampon=liste[idx_minimum]
			liste[idx_minimum]=liste[place_definitive]
			liste[place_definitive]=tampon
			   

def plot_age():
	"""
	plot la courbe des frequences des ages a l'aide la librairie pylab
	"""
	liste_age=collectAge()		
	dicoAge={}
	for age in liste_age:
		dicoAge[age]=dicoAge.get(age,0)+1

	X_age=[]  	
	Y_age=[]
	for age in dicoAge:
		X_age.append(age)  	
	        Y_age.append(dicoAge[age])
	pylab.plot(X_age,Y_age)	
	pylab.grid()
	pylab.show()




if __name__=='__main__'	:
	global nom,age,membre
	membre={}
	nom='nom'
	age='age'
	z={nom:'ravelomanana huygens','date de naissance':[16,05,2085],age:22}
	y={nom:'ravelomanana bernoulli','date de naissance':[15,11,2025],age:15}	
	ajout_membre(z)
	ajout_membre(y)
	print membre
	print "\n"
	supr_membre(y[nom])
	print membre
	print "\n"
	ajout_membre(y)
	print membre
	print "\n"
	print rechercheParAge(15)
	listeAge=collectAge()
	print listeAge
	print Average(listeAge)
	print ecart_type(listeAge)
	print "\n"
	print membre.keys()
	print Average(listeAge)
	existance=rechercheParNom('ravelomanana bernoulli')
	if existance :
		print membre['ravelomanana bernoulli'][age]
	print Min_liste([4,21,1,6,3,7])
 	a=[4,21,1,6,3,7]
	print trie_croissant(a)	
	print a
	plot_age()
