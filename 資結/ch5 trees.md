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
# threaded binary tree 
```c
void insucc(TreePtr tree) {
	TreePtr temp = NULL;
	temp = tree->rightchild;
	if (!temp->rightThread) {
		while (!temp->leftThread) // caution
			temp = temp->leftchild;
	}
	return temp;
}

void tinorder(TreePtr tree) {
	TreePtr temp = tree;
	for (;;) {
		temp = insucc(temp);
		if (temp == tree) break;
		printf("%d", temp->data);
	}
}
```
## question
1. why header root->rightchild point to itself ?
	ANS : the structure "original tree is the header's root's leftchild"
2. 如果沒有將 root->rightchild = root 的話會發生甚麼問題呢 ?
    ANS : 在 insucc 的 operation 會出問題，舉個例子，如果
```handdrawn-ink
{
	"versionAtEmbed": "0.2.4",
	"filepath": "picture/Ink/Drawing/2024.9.12 - 14.29pm.drawing"
}
```
所以如果 node 的 rightchild 沒有東西並且不是 threadpointer，就要將 rightThread 設為 false 並且 rightchild pointer 指向<mark style="background: #BBFABBA6;">自己</mark>
