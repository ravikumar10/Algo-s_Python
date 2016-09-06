"""

Selection sort

"""

def selection_sort(seq):
	for i in range(0,len(seq)):
		iMin=i
		for j in range (i+1,len(seq)):
			if seq[iMin] > seq[j]:
				iMin=j
		if i!=iMin:
			seq[i],seq[iMin]=seq[iMin],seq[i]
	return seq

if __name__=="__main__":
	seq = [-2,-3,4,-1, -2, 1, 5, -3]
	print (selection_sort(seq))