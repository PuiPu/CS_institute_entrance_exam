# 基本關係
1. reflexive
		1. 問題
			1. reflexive 一定要包含所有的 $$aRa, \forall a \in A$$
			ex. Let A = {1,2,3}, if R = {(1,1), (2,2)}, then R is not reflexive (because it should include (3,3))
2. symmetric

| symmetric                                   | asymmetric                                      | anti-symmetric                                         |     |
| ------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------ | --- |
| $$\forall a,b\in A,\:aRb \Rightarrow bRa $$ | $$\forall a,b\in A,\:aRb \not\Rightarrow bRa $$ | $$\forall a,b\in A,\:aRb \wedge  bRa \Rightarrow a=b$$ |     |
	1. 問題 
		1. symmetric 是一定要包含所有的 ? $$aRb \wedge bRa \in A \:,\forall a,b \in A $$ANS : <mark style="background: #FF5582A6;">NO</mark> , 他的 forall 是指說 R裡面只要出現 (a,b) 就必須出現 (b,a)，而不是說整個集合 A 都要存在
			ex. 假設 A = {1,2,3}, R 包含於 AxA，則 R = {(1,2), (2,1), (2,2)} 具 symmetric
#  2-6 <mark style="background: #FFB8EBA6;">鴿籠定理</mark>
## 定義
### intuitive
> If *k* is a positive integer and *k+1* or more objects are placed into k boxes, then there is at least one box containing two or more of the objects.
### generalized
> If *N* objects are placed into k boxes, then there is at least one box containing at least floor(*N/K*) objects.
## 想法
1. 想 worst case 以後，其他剩下的都滿足條件，所以再依照題目條件去多選幾個 items
2. 把 items 根據條件分組，再從每個 group 選一個 (worst case) 以後，再多選 1 個以上，就可以確保至少兩個符合相同條件
# 2-7 計數問題
> 此章注重在 <mark style="background: #FFF3A3A6;">infinite</mark> set 的 cardinality(基數)
## 可數集、不可數集
> 假設 A 為一個集合，若 A 為有限集合或 A ~ Z+，則稱 A 為可數集 (countable set)，否則為不可數集 (uncountable set)
