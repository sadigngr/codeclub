'''
Stores the data and functions for GeneID and CellType objects.

We store gene Bases and cell types as objects because it's easier and
more readable.

'''
import math
class Cell:

	def __init__(self,Name,Bases = list()):
		''''
		Gets the cell types and gene ids.

		Returns : None

		Gets:
		CellTYpe as String
		GeneIDs as list of ID objects
		'''

		self.Name = Name
		self.Bases = Bases

	@property
	def bases(self):
        '''
        Returns the bases

        Gets : None

        Returns : List
    '''
		return self.Bases

	@property
	def name(self):
		'''
		Returns the cell type

		Returns : String
		'''

		return self.Name

	def add(self,ID):
		self.GeneIDs.append(ID)

class Base:

	def __init__(self,Name = str(),CellType = str(),Expressions = list()):
		'''
		Gets the Base name and the list of expressions

		Returns : None
		'''
		self.CellType = CellType
		self.Expressions = Expressions
		self.Name = Name

	@property
	def expressions(self):

		return self.Expressions
	@property
	def name(self):
		return self.Name
	@property
	def celltype(self):
		'''
		Returns
		'''
		return self.CellType
