# tree recursive definition
> A tree is a finite set of one or more nodes such that
> (1) there is a specially designated node call <mark style="background: #FFB8EBA6;">root</mark>
> (2) the remaining nodes are partitioned into n>=0 <mark style="background: #ABF7F7A6;">disjoint set</mark> T_1, T_2, ... , T_n, where each of these sets is a tree, T_1, ... , T_n are called the subtrees of the root
# terminology
1. degree = # subtrees
2. degree of the tree = maximum degree of the nodes in the tree
# question
1. Why we can translate k-degree tree to <mark style="background: #FFF3A3A6;">binary tree</mark> ? ANS : 因為 tree  children 的 order 不重要
	1. 但是，binary tree 的 order 就有關係
# representation
## array representation
1. 好處 : 
	1. 節省空間當 complete binary tree
	2. 簡單
2. 壞處 : 
	1. 浪費空間當 skewed binary tree
## linked representation
1. 為何會需要 ? ANS : 當需要 insert 或 deletion 在 middle tree node 時，array representation 會要搬移很多 nodes