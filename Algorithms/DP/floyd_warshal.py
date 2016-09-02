"""
Floyd Warshal : All pair shortest path Algorithm

"""

inf=float('inf')
graph = [
    [0, 3, 8, inf, -4], 
    [inf, 0, inf, 1, 7], 
    [inf, 4, 0, inf, inf], 
    [2, inf, -5, 0, inf], 
    [inf, inf, inf, 6, 0]
]

def floyd_warshall(graph):
		n=len(graph)
		D=graph
		for k in range(n):
			for i in range(n):
				for j in range(n):
					if i==j:
						D[i][j]=0
					else:
						D[i][j]=min(D[i][j],D[i][k]+D[k][j])
		return D
def get_min_dist(D):
    if negative_cost_cycle(D):
        return "Negative cost cycle"
    return min(i for d in D for i in d)

def negative_cost_cycle(D):
    n = len(D)
    for i in range(n):
        if D[i][i] < 0:
            return True
    return False

if __name__=="__main__":
	print(floyd_warshall(graph))
