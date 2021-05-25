from random import randint

class BubbleSort:
	def __init__(self, _array) :
		self._array = _array 
		 
	def sort(self ):

		for i in range(len(self._array)):
			isSorted = True
			for j in range(1 , len(self._array) - i):
				if (self._array[j] < self._array[j - 1 ]) :
				 	self._array = self._swap(self._array , j , j-1 )
				 	isSorted = False
			if (isSorted):
				return 
	def _swap(self , array , index1 , index2 ):
		
		temp = array[index1]
		array[index1] = array[index2]
		array[index2] = temp
		return array

	def PrintArray(self):
		array = self._array
		print(array , "\n" , "-"*20)

def main():
	myArray = [randint(0 , 10) for i in range(10)]
	Sorter= BubbleSort(myArray)
	Sorter.sort()
	print(myArray)
if __name__=="__main__":main()

# def swap(array , index1 , index2 ):
# 	temp = array[index1]
# 	array[index1] = array[index2]
# 	array[index2] = temp
# 	return array


# def sort(array):
# 	isSorted = True 
# 	for i in range(len(array)):
# 		isSorted = True
# 		for j in range(1 , (len(array) - i)):
# 			if array[j] < array[j-1] :
# 				array = swap(array , j , j-1)
# 				isSorted = False 
# 		if (isSorted):
# 			return


# def main():
# 	myArray = [4,6,2,1,9,3,0]
# 	sort(myArray)
# 	print(myArray)
# if __name__=="__main__":main()
