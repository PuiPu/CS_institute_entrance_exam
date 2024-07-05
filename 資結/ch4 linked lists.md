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
