# 3-3
## 問題
1. 子空間畫成 van diagram 就一定包含在裡面嗎 ?
	ANS : subspace 指的是 dimension 會小於原空間，而不是只實際的大小  ex. subspace 可以等於本身的 space

```handdrawn-ink
{
	"versionAtEmbed": "0.2.4",
	"filepath": "picture/Ink/Drawing/2024.8.1 - 10.21am.drawing"
}
```

2. span(S) 為包含 S 之最小子空間，why ?

```handdrawn-ink
{
	"versionAtEmbed": "0.2.4",
	"filepath": "picture/Ink/Drawing/2024.8.1 - 10.24am.drawing"
}
```

3. ker(A) 定義 ?
	1. Ax = 0 (null space) , x 為 A 的 kernal
		
```handdrawn-ink
{
	"versionAtEmbed": "0.2.4",
	"filepath": "picture/Ink/Drawing/2024.8.1 - 10.27am.drawing"
}
```

## 判斷是否為線性組合
1. 將向量變成列矩陣
2. 判斷是否可以形成 0 列
## 生成空間
> span(v1, v2, ... , vn) = all set of linear combination of v1, v2, ... , vn called the span(S)
1. A 的列空間 RS(A) 為 A 的生成空間
2. A 的行空間 CS(A) 為 A 的生成空間
## linear (in)dependent
- linear dependent
	1. 如果要知道是誰跟誰組成 linear combination 的話，要把 vector 化成行向量，接著做 rref，如果有 0 列，看其他列的倍數就知道是其他 vectors 的線性組合的常數 ?
- linear independent
	1. 如果化成 row matrix 後做 row operation 不能得到 0 列，就代表 linear independent
# 3-4
## basis
### 問題
1. 怎麼把 
$$
span(
\begin{bmatrix}1&0\\0&0\end{bmatrix},
\begin{bmatrix}0&1\\1&0\end{bmatrix},
\begin{bmatrix}0&0\\0&1\end{bmatrix}
)
$$
flatten 並且化成 (1)行向量矩陣 (2)列向量矩陣，並且判斷 dependency ?
## 兩定理
### 生成裁減定理
> 1. 原本的 vector space 可以 span V，但是不為線性獨立集，所以並非 basis
> 2. 因此，可以透過刪減 u，來得到 linear independent 的 vector
> 3. 這樣就符合 basis 的定義 (span & linear independent)
### 獨立擴增定理
> 1. 雖然原本就是 linear independent 的 vector，但是因為沒有 span V，所以還可以找到 $$u\not\in span(S),\: S\:\cup u\:is\: linear\:independent\:set$$
> 2. 所以一直加，就可以找到 span V 的 set
> 3. 這樣就符合 basis 的定義
---
從 thm 3-18 Steinitz 代換定理的證明後面就不懂了... (2024/8/10)