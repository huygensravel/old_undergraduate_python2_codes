#!/usr/bin/python

from anta import *
from Tkinter import *

"""
anta contient les donnees ils sont contenues dans un dictionnaire nomme membre, declare comme variable global aux deux fichiers anta et Gestion 
pour l'enregistrement voir fonction enregistre
"""

# WE MUST PRESS RETURN AFTER EACH ENTREE
#EXAMPLE Nom complet : blabla (RETURN)
#        Age:blabla (RETURN)
#THIS PROGRAMM HAVE A BIG PROBLEM : AFTER CLOSING THE WINDOW, ALL THE DATA ARE LOSED.HOW TO SAVE THE DATA IN A FILE AND READ FILE FOR GETTING THE DATA AGAIN ?
#il faut cliquer fort sur les boutons

#===progammeInterfaceGraphiqueUtilisateur=============================================================

def creat_bouton(Fen):
	"""
	creation des boutons a mettre sur la fenetre
	"""
	bou1=Button(Fen,text='Quiter',command=Fen.quit,bg="#ec8e01",width=24)
	bou1.grid(row=8,column=0)
	bou2=Button(Fen,text='Chercher par nom',command=NomRecherche,bg="#f17b13",width=24)
	bou2.grid(row=0,column=0)
	bou3=Button(Fen,text='Chercher par age',command=AgeRecherche,bg="#f17b13",width=24)
	bou3.grid(row=1,column=0)
	bou4=Button(Fen,text='Ajouter membre',command=Ajout,bg="#f17b13",width=24)
	bou4.grid(row=2,column=0)
	bou5=Button(Fen,text='Supprimer membre',command=suppr,bg="#f17b13",width=24)
	bou5.grid(row=3,column=0)
	bou6=Button(Fen,text='Lister par nom',command=listage,bg="#f17b13",width=24)
	bou6.grid(row=4,column=0)
	bou7=Button(Fen,text='Age moyenne',command=moyenneAge,bg="#f17b13",width=24)
	bou7.grid(row=5,column=0)
	bou8=Button(Fen,text='Age Ecart Type',command=ecarType,bg="#f17b13",width=24)
	bou8.grid(row=6,column=0)
	bou9=Button(Fen,text="Histogramme frequences d`ages",command=plot_age,bg="#f17b13",width=24)
	bou9.grid(row=7,column=0)
	bou10=Button(Fen,text='Enregistrer',command=enregistre,bg="#ec1225",width=24)
	bou10.grid(row=9,column=0)

def creat_label(Fen):
	"""
	creation des labels a cote des champs d'entrees
	"""
	global texte1,texte2
	texte1=Label(Fen,text='Nom complet')
	texte2=Label(Fen,text='Age')
	texte1.grid(row=0,column=1)
	texte2.grid(row=1,column=1)


def creat_entree(Fen):
	"""
	creation des champs d'entrees
	"""
	global entree1,entree2
	entree1=Entry(Fen,bg="light blue",foreground="brown",font='verdana')      #f17b13
	entree2=Entry(Fen,bg="light blue",foreground="brown",font='verdana')
	entree1.grid(row=0,column=2)
	entree2.grid(row=1,column=2)


def saisie1(event):
	"""
	enregistrement des valeur entree dans le champ d'entree entree1 par l'utilisateur dans la variable global anarana 
	"""
	global entree1,anarana
	anarana=entree1.get()
	


def saisie2(event):
	"""
	enregistrement des valeur entree dans le champ d'entree entree2 par l'utilisateur dans la variable global taona
	"""
	global entree2,taona
	taona=entree2.get()


def lecture():
	"""
	lecture des valeurs introduites dans les champs d'entrees
	"""
	global entree1,entree2
	entree1.bind('<Return>',saisie1)
	entree2.bind('<Return>',saisie2)
	
def cree_individu():
	global anarana,taona
	return {NOM:anarana,AGE:taona}





#=====Progamme Lien Entre Interactif et Mode Graphique========================================




# def test_entree():
# 	"""
# 	test si l'utiliasareur entre bien ce qu'il faut
# 	"""
# 	global taona,anarana 
# 	tampon1=(type(taona)==int)
# 	tampon2=(type(anarana)==str)
# 	if tampon1!=True or tampon2!=True:
# 		texte_space.delete(1.0,END)	
# 		texte_space.insert(INSERT,"L'age doit etre un entier et le	nom une chaine de caracters s'il vous plait.")


def NomRecherche():

#test_entree()
	existance=rechercheParNom(anarana)
	
	if existance:
		tampon=str((membre[anarana][AGE]))
		result="%s est bien dans la societe et est age de " %anarana + tampon +" ans "
		
	elif not existance:
 		result="Aucune persone du nom %s dans la societe" %anarana
	
	texte_space.delete(1.0,END)	
        texte_space.insert(INSERT,result)


def AgeRecherche():
#test_entree()
	vokatra=rechercheParAge(taona)
	texte_space.delete(1.0,END)
	if vokatra==[]:
		result="Aucune personne de cet age dans la societe"
		texte_space.insert(INSERT,result)
	else:
		texte_space.insert(INSERT,"Voici les personnes correspondant a cet age :	")
		for zavatra in vokatra:
			texte_space.insert(INSERT,zavatra+" 	")



def Ajout():
#test_entree()
	ajout_membre(cree_individu())
		
def suppr():
#test_entree()
	global anarana
	supr_membre(anarana)	

def listage():
	global membre 
	texte_space.delete(1.0,END)
	if membre!={}:
	
		texte_space.insert(INSERT, "Voici les membres de la societe :  ")
		for individu in membre:
			"""
			boucle de parcour pour le listage des membres
			"""
			
	     		texte_space.insert(INSERT,individu + " 	- ") 
  
	else:
		texte_space.insert(INSERT, "Il n'y a  aucun membre dans la societe ")

def moyenneAge():
	tampon=Average(collectAge())
	tampon=str(tampon)
	texte_space.delete(1.0,END)
	texte_space.insert(INSERT, "La moyenne d'age est de   "+ tampon +" ans")

def ecarType():
	tampon=ecart_type(collectAge())
	tampon=str(tampon)
	texte_space.delete(1.0,END)
	texte_space.insert(INSERT, "L'ecart type des ages est   "+ tampon )






#=====progammeInteractif======================================================================
#programme de gestion des membres d'une societe 




from math import sqrt
import pylab 

"""
on utilisera un dictionnaire pour contenir tout les membres et les clefs seront les noms des membres

de meme pour les attributs de chaque membre on utilisera egalement un dictionnaire comme conteneur et les clefs serontegalements les noms des membres

"""

#pour gobal voir le main programme
def ajout_membre(nouv_membre):
	"""
	ajout d'un membre , le nouveau membre est deja un dictionnaire 
	"""
	global membre,NOM
	membre[nouv_membre[NOM]]=nouv_membre

def supr_membre(nom_membre):	
	"""
	suppression d'un membre en donnant son nom (les clefs sont les noms)
	sans valeur de retour ,supprime simplement l'entite indexe par nom_membre du dictionnaire des membres
	"""
	global membre
	del(membre[nom_membre])

def rechercheParNom(Nom=""):
	"""
	recherche d'un membre par sa clef qui est son nom 
	retourne 
	"""
	global membre
	return membre.has_key(Nom)

def rechercheParAge(Age):
	"""
	recherche des membres ayant le meme age Age
	retourne ces membres sous forme de liste
	"""
	global membre,NOM,AGE
	resultat=[] 						#initialise un liste vide
	for element in membre:
		"""
		boucle de parcour pour tester tout les membres
		"""
		if  Age==membre[element][AGE] :                
			"""
			teste si le membre a l'age Age et l'ajoute a la liste de retour si  oui
			"""
			resultat.append(membre[element][NOM])

	return resultat	

def collectAge():
	"""
	collecte les ages des membres, il peut y avoir des doublon : Comment l'eviter?
	retourne les valeurs trouvees sous forme de liste
	"""
	global membre,AGE
	listAge=[]
	for element in membre:
		listAge.append(int(membre[element][AGE]))
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
	plot la courbe  des frequences des ages a l'aide la librairie pylab
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


def enregistre():
	"""
	enregistre les donnees dans le fichier anta.py 
	
	"""
	global membre
	tampon=str(membre)
	za=open('anta.py','w')
	za.write('global membre\nmembre='+tampon)
	za.close()







#====Main======================================================================================

if __name__=='__main__':
	global entree1,entree2,texte1,texte2,membre,NOM,AGE,anarana,taona
	anarana=""
	taona=1
	NOM='nom'
	AGE='age'
		
	fenetre=Tk()
	fenetre.title("Gestion des membres")
	creat_bouton(fenetre)
	creat_label(fenetre)
	creat_entree(fenetre)
	can1=Canvas(fenetre,bg="black")
	can1.grid(row=2,column=1,rowspan=7,columnspan=2)
	texte_space=Text(can1,bg="white",width=40,height=10,foreground="blue",font='verdana')#cree une zone de texte dans le canvas can1 
	
	texte_space.pack()
	lecture()   
	
	fenetre.mainloop()
	
