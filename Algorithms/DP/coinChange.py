#!/usr/bin/python
"""
Problem : Coin Change Problem

"""

def coin_change(total,coins):
	M=len(coins)
	table=[[0]*M for i in range(total+1)]
	for i in range(M):
		table[0][i]=1
	for i in range(1,total+1):
		for j in range(M):
			#count the total solution excluding coin[j]
			x=table[i][j-1] if j > 0 else 0
			y=table[i-coins[j]][j] if i-coins[j] >=0 else 0
			table[i][j]=x+y
	return table[total][M-1]

if __name__=="__main__":
	print coin_change(10, [2, 3, 5, 6]) 
	print coin_change(5, [2, 3, 5])
	print coin_change(4, [1, 2, 3])     
