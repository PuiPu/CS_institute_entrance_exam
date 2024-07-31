#include <iostream>
using namespace std;

typedef struct treeNode *treePointer;
typedef struct treeNode {
    treePointer root, left, right, parent;
    char color;
    int data;
} treeNode;

class RB_TREE {
public:
    treePointer T = NULL;
    void left_rotate(treePointer T, treePointer x);
};

void RB_TREE::left_rotate(treePointer T, treePointer x) {
    treePointer y = new treeNode();
    y = x->right;
    x->right = y->left;
    if (y->left != NULL)
        y->left->parent = x;
    y->parent = x->parent;
    if (x->parent == NULL)
        T->root = y;
    else if (x == x->parent->left)
        x->parent->left = y;
    else 
        x->parent->right = y;
    y->left = x;
    x->parent = y;
}

int main() {
    treePointer root = new treeNode();

    root->data = 0;
    root->color = 'b';
    root->right = root->left = NULL;
    

}