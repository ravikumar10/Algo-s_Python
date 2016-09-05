"""
Problem : The maximum subarray prblem is the task of finding the contiguous subarray within a one-dimensional array of Numbers
					which has the largest sum.
"""

def max_value_contiguous_subsequence(arr):
	A=[arr[0]]+[0]*(len(arr)-1)
	max_to_here=arr[0]
	for i in range(1,len(arr)):
		A[i]=max(arr[i],arr[i]+arr[i-1])
		max_to_here=max(max_to_here,A[i])
	return max_to_here

if __name__=="__main__":
  x = [-2,-3,4,-1, -2, 1, 5, -3]
  y = [-2,1,-3,4, -1, 2, 1, -5, 4]
  z = [-1, 3, -5, 4, 6, -1, 2, -7, 13, -3]
  print (map(max_value_contiguous_subsequence, [x, y, z]))

  	