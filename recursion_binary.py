#!/usr/bin/env python

rem = [';','(',')',',',':','.','?','!','=','¿','\'']
#le saque el \n porque el split al parecer entiende 
#que tiene que separar por espacio y nuevas lineas


class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data
		self.counter = 1


	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)	
				else:
					self.right.insert(data)
			elif data == self.data:
				self.counter +=1                     
		else:
			self.data = data
		            	
		return 


def PrintInOrder (knot):
	if knot.left is not None:
		PrintInOrder(knot.left)
	print (knot.data)
	if knot.right is not None:
		PrintInOrder(knot.right)
	return


def CreateListInOrder(knot, lista):
	if knot.left is not None:
		CreateListInOrder(knot.left, lista)	
	lista.append(tuple([knot.data , knot.counter]))
	if knot.right is not None:
		CreateListInOrder(knot.right, lista)
	return	



def clean(lista):
	for i in lista:	
		if i in rem :
			lista.remove(i) 
		else:
			continue
	return lista

def GenerateOccrrList(f):
	list_dirty = list(f.read())
	list_clean = clean(list_dirty)
	list_clean = ''.join(list_clean)
	wrd_list = list_clean.split()

	rooterino = Node(wrd_list[0])

	for i in wrd_list[1:]:
		rooterino.insert(i)

	Tidy_List = list() 
	CreateListInOrder(rooterino, Tidy_List)
	Tidy_List.sort(key = lambda tup: tup[1])
	return Tidy_List

def DensUnic(lista, key):
	occ=0
	for i in lista:
		if i[1] == key:
			occ+=1
		else:
			break

	unoporc=occ/len(lista)
	return unoporc


def GetCoord (data):
	counter=0 
	data_grph=list()
	for i in data:
		aux = [counter,i[1]]
		data_grph.append(aux)
		counter+=1
	return data_grph
	
#def insert_in_order(Node knot_t, lista ):
#	if knot_t is None:
#		print('faggot, this is empty')
#		return
#	insert_in_order_(Node knot_t, lista )
#	return
		




#main?


from pylab import figure, text, scatter, show
import codecs 
import numpy as np
import matplotlib.pyplot as plt

f = codecs.open('/home/vancii/Documents/Algoritmos/ICOM/final/text.txt',encoding='utf/8', mode='r+')
data = GenerateOccrrList(f)
CoordXY = GetCoord(data)

zip(*CoordXY)
leg = '%s %f ' % ('Densidad Unica = ', DensUnic(CoordXY,1))
graph=plt.scatter(*zip(*CoordXY),label=leg)
plt.legend(loc='upper left')
plt.title('Ocurrencia de palabras')
plt.xlabel('Palabra x-esima')
plt.ylabel('# Menciones')
plt.show(graph)


#me gustaria que le des una carpeta full de 
#archivos y hhaga un GenerateOccrList

