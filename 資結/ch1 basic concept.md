# Dynamic allocate memory
## 重點
- 良好習慣
	- 宣告 new pointer to NULL ptr
## 問題
- if requested memory is not avaliable, it return NULL
```c
typedef struct A {
	int data;
	int *ptr;
};

struct A test;
// structure member operator
(*test).data = 3;
test->data = 3; // shorten
```
