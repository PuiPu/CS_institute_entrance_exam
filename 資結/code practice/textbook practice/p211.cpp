#include <iostream>
#define MAX_STACK 500
using namespace std;

// tree define
typedef TreeNode *TreePtr;
typedef struct TreeNode {
    int data;
    TreeNode *left, *right; 
} TreeNode;

// stack define
int top = -1;
TreePtr stack[MAX_STACK];
void push(TreePtr node) {
    if (top < MAX_STACK) {
        stack[top++] = node;
    }
}
TreePtr pop() {
    TreePtr ptr = stack[top];
    top--;
    return ptr;
}

// exercise 3 (錯)
void iterPreorder(TreePtr node) {
    for (;;) {
        for (; node; node = node->left) {
            push(node);
        }
        node = pop();
        if (!node) break; // empty stack
        node = node->right; 
    } 
}

// exercise 4 (想不到)
void iterPostorder(TreePtr node) {
    for (;;) {
        for (; node; node = node->left) {
            push(node);
        }
        node = pop();
        if (!node) break;
        node = node->right;
        if (node) printf("%d ", node->data);
    }
}

void main() {
    TreePtr root = NULL;
    root->data = 0;
    root->left = new TreePtr();

}