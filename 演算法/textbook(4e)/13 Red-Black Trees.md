# 13-1 Properties of red-black trees
## red-black properties
1. every node is either red or black
2. the root is black
3. every leaf (NIL) is black
4. if a node is red, then both its children are black
5. for each node, all simple paths from the node to descendant leaves contain the same number of black nodes
## black-height bh(x)
> bh(x) : number of black nodes on any simple path from
## operation
- SEARCH, MINIMUM, MAXIMUM, SUCCESSOR, PREDECESSOR take *O*(lg n) time
# 13-2  Rotations
> rotation := preserve binary-search-tree property ???

![[Pasted image 20240730160501.png]]
![[Pasted image 20240730160824.png]]
```
left rotate(x, y)
	1. replace x with y
	2. y.left = x
	3. x.right = y.left (because BST property : y.left.data > x.right.data)
```

# 13.3 Insertion
## modify...
![[Pasted image 20240730161919.png]]
## to ...
![[Pasted image 20240730162000.png]]
## fixup
![[Pasted image 20240730162103.png]]
![[Pasted image 20240731164124.png]]
### case 1
> violate 
> 	1. property 2 : { root is black }
> 	2. property 4 : { red node cannot have a red child}
> solution
> 	1. 
