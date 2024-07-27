# definition
```
# Graph (G)
	1. vertices V(G)
	2. edge E(G)
		a. directed (u,v)
		b. undirected <u,v> : [u is tail, v is head]
# Subgraph
	1. V(G') belongs to V(G)
	2. E(G') belongs to E(G)		

# Restriction (simple path)
	1. self-loop
	2. multigraph

# Type
	1. complete graph 
		a. (undirected) : #edges = n(n-1)/2
		b. (directed) : #deges = n(n-1)

# Definition
	1. (u,v) is an edge in E(G), then...
		a. u and v are adjacent
		b. (u,v) is incident on vertice u and v 
	2. <u,v> is an edge in E(G), then...
		a. u is adjacent to v
		b. v is adjacent from u
	3. degree
		def.
			number of edges incident to that vertex 
		a. undirected graph
		b. directed graph
			1. in-degree : head
			2. out-degree : tail

# undirected graph : connected
	1. edge (u,v) is connected, then...
		a. there is a path from u to v (v to u)
	2. graph G is connected, then...
		a. each pair (u,v) in graph has a path from u to v (v to u)
	
	| Note. 
	|	 tree is connected acyclic (no cycles) graph

# directed graph : connected
	1. graph G in conntected, then...
		a. each pair <u,v> in graph has a path from u to v
		b. each pair <v,u> in graph has a path from v to u 

# undirected graph : connected component (or component) H
	Def. 
		a. maximal connected subgraph
		b. "Maximal" means that "G contains no other subgraph is both connected               and property contains H"  	

# directed graph : strongly connected component
	Def.
		a. maximal subgraph that is strongly connected
```
# graph representation
## adjacency matrix
> Pro : quickly check whether there is an edge for vertices i ,  j
> Con : 
> 	1.  Sparse graph 
> 		a. waste memory space
> 		b. identify exist edge need O(n^2) 
$$a[i,j] = 
\begin{cases}
w \quad if \; (i,j) \in E \\
0 \quad otherwise
\end{cases}$$
### degree
	$$ 
	\begin{aligned}
	degree = row\:sum = \sum^{n-1}_{j\:=\:0} a[i][j]
	\end{aligned}
	\tag{undirected graph}
	$$
	$$	
	\begin{aligned}
		\begin{cases}
			\quad in-degree = row \: sum = \sum^{n-1}_{j\:=\:0} a[i][j] \\
			\quad out-degree = column \: sum = \sum^{n-1}_{i\:=\:0} a[i][j]
		\end{cases}
	\end{aligned}
	\tag{directed graph}
	$$

## adjacency list
> Concept
> 	1.  repesent only edges is needed only in G
> Note
> 	1.  vertices in each chain are not required to be ordered
> Pro
> 	1.  access in O(1)
> Con
> 	1. space = # nodes + 2 * # edges chain nodes = O( n + 2e )
```
# head
	1. vertex i
# chain
	1. vertices : adjacent from vertex i
	2. data field : index of adjacent vertex
# degree
	1. directed graph
		a. number of nodes in chain 
	2. undirected graph
		a. out degree = number of nodes in the chain
		b. in degree = complex ...
		   | inverse adjacency list : contain a node for each vertex adjacent to                the vertex |
```
> 為什麼要有 inverse adjacency list ? ANS : 因為 inverse 以後，outdegree 就會變成 indegree (cool)
## adjacency multilist
> Concept
> 	1. remember the other connected edges (edge based)
# network
## definition
> a graph with weighted edges

