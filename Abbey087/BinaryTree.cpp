#include "BinaryTree.h"

BinaryTree::BinaryTree() {
    root = NULL;
}

BinaryTree::BinaryTree(int elem) {
    root = new Node(elem);
}

void BinaryTree::setRoot(Node* r) {
    root = r;
}

Node* BinaryTree::getRoot() {
    return root;
}

bool BinaryTree::isEmpty() {
    return (root == NULL);
}

