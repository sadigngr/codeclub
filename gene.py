'''
Stores the data and functions for GeneID and CellType objects. 

We store gene Bases and cell types as objects because it's easier and 
more readable.

'''
import math
class Cell:

	def __init__(self,Name,Bases = list()):
<<<<<<< HEAD
		''''
		Gets the cell types and gene ids.
		
		Returns : None 

		Gets:
		CellTYpe as String 
		GeneIDs as list of ID objects
		'''
		
=======

>>>>>>> a4011551b2a2f8552326ba757678d5e956f8c6b1
		self.Name = Name
		self.Bases = Bases

	@property
	def bases(self):
<<<<<<< HEAD

=======
		
>>>>>>> a4011551b2a2f8552326ba757678d5e956f8c6b1
		return self.Bases

	@property
	def name(self):
<<<<<<< HEAD
		''' 
		Returns the cell type

		Returns : String
		'''
=======
>>>>>>> a4011551b2a2f8552326ba757678d5e956f8c6b1

		return self.Name

	def add(self,ID):
		self.GeneIDs.append(ID)

class Base:

	def __init__(self,Name = str(),CellType = str(),Expressions = list()):

		self.CellType = CellType
		self.Expressions = Expressions
		self.Name = Name

	@property
	def expressions(self):
		for i in range(len(self.Expressions)):
			self.Expressions[i] = self.Expressions[i] ** 2
		 
		return self.Expressions
	@property
	def name(self):
		return self.Name
	@property
	def celltype(self):
<<<<<<< HEAD
		'''
		Returns 
		'''
		return self.CellType
=======
		
		return self.CellType
>>>>>>> a4011551b2a2f8552326ba757678d5e956f8c6b1
