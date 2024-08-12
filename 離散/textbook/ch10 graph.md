# 10-2 Graph Terminology and Special Types of Graphs
## degree of the graph
1. loop 要算兩次
## vertex
1. isolated : degree = 0
2. pendant (吊墜) : degree = 1 (p.s. 就像有一根繩子吊一個物品)

```handdrawn-ink
{
	"versionAtEmbed": "0.2.4",
	"filepath": "picture/Ink/Drawing/2024.8.11 - 15.12pm.drawing"
}
```
# 10-3 Representing Graphs and Graph Isomorphism
## isomorphic definition (不是主要的定義，真正的定義在 p.706)
> there is a one-to-one correspondence between vertices of the two graphs that preserves the adjacency relationship
## 怎麼判斷 simple graph 是不是 isomorphic ?
### <mark style="background: #FFF3A3A6;">Graph Invariant</mark>
- same number of ... (because of one-to-one correspondence)
	1. vertices
	2. edges
### 但是 ...
1. 這樣還是不能確保滿足所有 loop invariant 一定就是 isomorphic
2. 現今沒有一個 graph invariant set 可以確定滿足後就一定會是 isomorphic
### 儘管如此
1. graph invariant 還是可以去判斷 graph 不是 isomorphic，只要不滿足其中一項 graph invariant
