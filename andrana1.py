"""
    * Create a class for particle objects, that stores their name, 3D coordinates and color. Afterwards, create a program that read particle data from a file, create the particles and store them in an array. Finally, the program will print all the particles. 

"""

class particule:			#declaration de la class particule
	
	"""
	cree la classe particule avec comme attribut   :
	1_ les coordonnees : X_coordonee,Y_coordonee,Z_coordonee , 
	2_ la couleur 
	3_ le nom 	 
	
	"""
	
	(X_coordonee,Y_coordonee,Z_coordonee )=(0,0,0)
	Couleur_Particule='blue'			#constante de la particule :la couleur 	
	nom_Particule='zavatra'
	
	def __init__(self,X_coordonee,Y_coordonee,Z_coordonee,nom_Particule,Couleur_Particule):
		"""
		constructeur
		"""		
		self.__X_coordonee=X_coordonee			#les attributs
		self.__Y_coordonee=Y_coordonee
		self.__Z_coordonee=Z_coordonee
		self.__nom_Particule=nom_Particule
		self.__Couleur_Particule=Couleur_Particule
		
	def lecture_coordoonne(self,X_coordonee,Y_coordonee,Z_coordonee):	
		"""
		lecture des coordonnee par rapport a X,Y,Z
		"""
		self.__X_coordonee=X_coordonee			
		self.__Y_coordonee=Y_coordonee
		self.__Z_coordonee=Z_coordonee

	def lecture_nomParticule():
		"""
		lecture du nom de la particule
		"""
		self.__nom_Particule=nomParticule

	def lecture_couleurParticule():
		"""
		lecture de la couleur de la particule
		"""
		self.__Couleur_Particule=Couleur_Particule

	def ecriture_coordoonne():
		"""
		retourne des coordonnee par rapport a X,Y,Z
		"""
		return 	self.__X_coordonee,self.__Y_coordonee,self.__Z_coordonee

	def ecriture__nomParticule():
		"""
		retourne le nom de la particule
		"""
		return self.__nom_Particule

	def ecriture__couleurParticule():
		"""
		retourne la couleur de la particule
		"""
		return self.__Couleur_Particule
		
	def __str__(self):
		"""
		definit le mode de sortie a l'ecran de la classe particule
		"""
		
	        Particule = {}
		Particule ="  Nom de la particule : %s \n" %self.__nom_Particule
		Particule +="  Coordonnees de la particule : \n \t %f" %self.__X_coordonee
		Particule +="\t %f"%self.__Y_coordonee
		Particule +="\t %f \n"%self.__Z_coordonee
		Particule +="  Couleur de la particule : %s" %self.__Couleur_Particule
		
		
	        return Particule 

if __name__=='__main__':
	zavatra=particule(X_coordonee=1,Y_coordonee=1,Z_coordonee=1,Couleur_Particule='white',nom_Particule="izy")
	print zavatra
