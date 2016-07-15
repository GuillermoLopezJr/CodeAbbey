#include "BinaryTree.h"

BinaryTree::BinaryTree() {
    root = nullptr;
}

BinaryTree::BinaryTree(int elem) {
    root = new Node(elem);
}

void BinaryTree::setRoot(Node* n) {
    root = n;
}

Node* BinaryTree::getRoot() {
    return root;
}

bool BinaryTree::isEmpty() {
    return (root == nullptr);
}

Node* BinaryTree::insert(Node* n, int elem) {
    if (n == nullptr) {
        n = new Node(elem);
    }
    else if (elem < n->elem) {
        n->left = insert(n->left, elem);
    }
    else if (elem > n->elem) {
        n->right = insert(n->right, elem);
    }
    else {
        //error occured
    }
    return n;
}

void BinaryTree::insert(int elem) {
   root =  insert(root, elem);
}
