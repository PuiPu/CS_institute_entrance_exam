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
		1. 