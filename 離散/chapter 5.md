Time : 2024/6/28
# 5-1
# 5-2
## 重點
- 解特徵方程式的時候，如果高於二次，可以用牛頓一次因式檢驗法 [[https://resource.learnmode.net/upload/flip/book/04/04badda80f82d7e2/3aa17cac2d86.pdf|牛頓一次因式檢驗法]]
## 問題
- 何謂特徵方程式 ? 怎麼來的 ?
- homogeneous ? non-homogeneous ?
- 在帶回 non-homogeneous 的時候要帶回 an(p) 不是 an(h)
## 加強
- k 階常係數遞迴關係式的定義要在熟悉
- homogeneous 的重根 form 不熟 + 推導
- non-homogeneous 計算很容易錯，慢慢來，確保每一步都是對的
---
> non-homogenous 後面的都先跳過，計算太多 ... (2024/6/30)

Time : 2024/6/30
## non-homogeneous
- question : [[non-homogeneous solution problem]]
---
Time : 2024/7/5
# 5-3
## 重點
- 就只是變數變換成常係數方程式
- 解 homogeneous 跟 particlular solution
## 問題
- 特殊的替換方式要記
# 5-4
## 問題
- 怎麼用 generating function 去解遞迴式 ? generating function 定義 ?
- 為什麼要乘以 x^n 然後取 sigma ?
	- 因為等式同乘 x^n 不影響等式
	- 在取 sum 也不影響等式
- a_n = generating function A(x) : x^n 的係數
## 重點
- [[partial fractional decomposition (calculas)]]
---
Time : 2024/7/6
# 5-5
## 重點
- 在展開遞迴式的時候可以分開展開比較不會亂 (5-77)
---
Time : 2024/7/7
#  5-6
## 重點
- Catalan number (卡特蘭數)
## 問題
- 遞迴問題怎麼生成 Cartalan number 的 ? 
	- ANS : 生成函數 (ch4) + 卷積 (ch4)
[[uva 514 rails]]
> number of binary tree is catalan number is too hard , 跳過 ... 
- 用組合證法不是很清楚，要再看