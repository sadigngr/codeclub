'''
Prepares the data for the modeling process. Creates Base and Cell objects to handle the data easily.


_READ() => Reads the txt files.

	Gets : path as string .
	Returns : The metadata as list.

_ID() => Creates a dictionary from the given metadata.

	Gets : The metadata from _READ().
	Returns :  The Bases and Cell Types from metadata as dictionary.

_DF() => Returns the expressions of the base.

	Gets :  The Base.
	Returns : The expressions of the base, using the dataframe created from the data.training.txt.nosync.txt, as list.

_PAIR() => Pairs the Base Objects with Cell objects. 
	
	Gets : None
	Returns : The Cell objects and the Base objects within, as list.


'''

from gene import *
import pandas as pd
import time
import numpy
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

df = pd.read_table("data.training.txt.nosync.txt")
print(df.dtypes)
print(type(df["AGCTTTACACCAAC"][2]))
print(df.head())
def timer(func):
	def wrapper(*args, **kwargs):
		a = time.time()
		return func(*args, **kwargs)
		b = time.time()
		print(f"Islem {b - a} saniye surdu.")
	return wrapper

def _READ(path):
	with open(path,"r") as f:
		return [l.strip() for l in f.readlines()]

def _ID(metadata):	
	sozluk = {}
	
	CellTypes = list()
	for i in metadata: 
		if "CellID" not in i:
			for j in range(len(i)):
				if i[j] == "\t":
					if i[j:] not in sozluk:
						sozluk[i[j:]] = i[:j]
					else:
						sozluk[i[j:]] += "," + i[:j]	
	return sozluk
	
def _PAIR():
	baslangic = time.time()
	CellTypes = list()
	Bases = list()
	sozluk = _ID(_READ("meta.data.training.CellTypes.txt.nosync.txt"))
	ilk = True
	for i in sozluk.keys():

		for k in sozluk[i].split(","):
			a = time.time()

			baseObj = Base(k,i,df[k].values)
			print(df[k].values)
			b = time.time()

			print(f"Obje Olusturma Islemi {b - a} saniye surdu.")
			Bases.append(baseObj)
			del baseObj

		name = i.replace("\t","")
		cellObj = Cell(name,Bases)
		CellTypes.append(cellObj)
		Bases = []
		del cellObj

	bitis = time.time()
	print(f"Toplam islem {bitis - baslangic} saniye surdu.")
	return CellTypes

def X_Y():
	bas = time.time()
	X = list()
	y = list()
	for i in _PAIR():
		for j in i.bases:
			X.append((j.name,j.expressions))
			y.append(j.celltype)


	X_train, X_test, y_train, y_test = train_test_split(X , y, test_size=0.2)
	svm_model = SVC(C = 1.0,kernel='linear')
	svm_model.fit([k[1] for k in X_train], y_train)
	print("Model Oluşturuldu.")

	y_pred = svm_model.predict([l[1] for l in X_test])

	for i in range(len(X_train)):
		try:
			print(X_test[i][0]," : ", y_pred[i])
		except IndexError:
			break

	accuracy = svm_model.score([m[1] for m in X_test], y_test)

	print("Doğruluk : ",accuracy)
	bit = time.time()
	print(f"ISLEM {bit - bas} SANIYE SURDU.")

if __name__ == "__main__":
	X_Y()