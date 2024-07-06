Time : 2024/7/5
# data structure
```c
typedef struct listNode *listPointer;
typedef struct listNode {
	int data;
	listPointer link;
}
```
> why C allow us to define "listPointer" before define "listNode" ? (p.149)

# operation
### insert
- Question
	1. Why " listPointer *first " need to be " pointer of listPointer " ? ANS : because list may be empty. (p.151)
	2. Why " listPointer x " DO NOT need to be " pointer of listPointer " ? ANS : because x don' change. (p.151)
```c
/* 
* first : first node in the list
* x : node precede wanted to insert
*/
void insert(listPointer *first, listPointer x, int data) {
	// create a new node
	listPointer tmp = (listPointer)malloc(sizeof(*listPointer));
	tmp->data = data;
	
	// if the list is empty
	if (*first == NULL) { // NOTE : not "first == NULL" 
		first->link = NULL;
		*first = tmp;
	}
	else {
		tmp->link = x->link;
		x->link = tmp;
	}
}
```
### delete
```c
/* 
* first : the first node of the list
* trail : node precede x
* x ; node wanted to delete
*/
void delete(listPointer *first, listPointer trail, listPointer x) {
	// delte the head
	if (trail == NULL) {
		*first = (*first)->link;
	}
	else {
		trail->link = x->link;
	}
	free(x);
}
```
### print
```c
void print(listPointer first) {
	printf("the list contain : ");
	for (; first; first = first->link) {
		printf("%d", first->data);
	}
	printf("\n");
}
```
---
Time : 2024/7/6
# stack
> 問題
> 	1. " i " 為 ith stack 還是不太懂為啥
```c
#define MAX_STACK 10
typedef struct element {
	int data;
} element;
typedef struct stack *stackPointer;
typedef struct stack {
	element data;
	stackPointer link;
}
stackPointer top[MAX_STACK];

/* --- operation --- */
void push(int i, element item) {
	stackPointer tmp = (stackPointer)malloc(sizeof(*stackPointer));		
	tmp->data = item;
	tmp->link = top[i];
	top[i] = tmp;
}

element pop(int i) {
	// pop the ith stack
	stackPointer tmp = top[i];
	element item;
	if (tmp == NULL) return stackEmpty();
	item = tmp->data;
	top[i] = tmp->link;
	free(tmp);
	return item;
}
```
# queue
> # addq ( i, item )
> 	1. if  queue 為空 (front == NULL) , 把 tmp 給 front
> 	2. if queue 不為空 , 把 rear 的 link 連上 tmp
> 	3. 最後 rear = tmp
> # deleteq (i)
> 	1. 跟 stack pop() 相同 
> # 問題
> 	1. deleteq(i) 是 pop 最前面的，不是 rear
```c
#define MAX_QUEUE 10
typedef struct element {
	int data;
} element;
typedef struct queue *queuePointer;
typedef struct queue {
	element data;
	queuePointer link;
};
queuePointer front[MAX_QUEUE], rear[MAX_QUEUE];

/* -- operation -- */
void addq(int i, element item) {
	queuePointer tmp = (queuePointer)malloc(sizeof(*queuePointer));
	tmp->data = item;
	if (front[i] == NULL) {
		front[i] = tmp;
	}
	else {
		rear[i]->link = tmp;
	}
	rear[i] = tmp;
}

element deleteq(int i) {
	queuePointer tmp = front[i];
	element item;
	if (tmp == NULL) return queueEmpty();
	item = tmp->data;
	front[i] = tmp->link;
	free(tmp);
	return item;
}
```
# polynomials

## 問題
1. 為甚麼 padd() 要有 initial node c, 並且最後要把它刪掉 ? (p.163)
2. why the total comparison is O(m+n) ?
## presented by circular linked list
## 問題
#### cpadd(polyPointer a, polyPointer b)
```c
polyPointer cpadd(polyPointer a, polyPointer b) {
	...
	do {
		switch (COMPARE(a->expo, b->expo)) {
			case -1:
				...
			case 0:
				if (startA == a) done = TRUE; // stop ???
				...
			case 1:
				...
		}
	} while (!done);
	// why don't need to attach the left of b
	lastC->link = c; // circular linked list
	return c;
}
```
# erase
## 問題
>1. 什麼時候才要 malloc 新的 node ? ANS : when list is empty. (p.166)
```
// reuse the memory space
1. list name : avaul (point to the front of the available list)
2. operation : 
	1. getNode()
	2. retNode()
```
## equivalance classes
> what is equivalance relation ? ANS : symmetric & reflexive & transitive  [[chapter 2| discete math relation]]
- 
