# from anta import *
# global a

# za=open('sa.py','a')
# za.write('global a\na=[1,2,3]')
# za.close()

dico={'a':1,'b':2,'c':3,'d':4}

def ecrit_sur_fichier(nom_fichier):
	toerana=open(nom_fichier,'a')
	for clef,entite in dico.iteritems():
		toerana.write(clef+'>')
		tampon=str(entite)
		toerana.write(tampon+'\n')
	toerana.close()



def lecture_su
	
ecrit_sur_fichier('izy.txt')
#print type(a)
# from Tkinter import *

# class window(Toplevel):
# 	def __init__(self):
# 		Toplevel.__init__(self)
# class window2(Frame):
# 	def __init__(self):
# 		Frame.__init__(self)
# 		self.pack()
# 		b = Button(self,command = window)
# 		b.pack()
# win = window2()
# win.mainloop()
