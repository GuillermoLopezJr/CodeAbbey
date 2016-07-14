#include "Node.h"

Node::Node(int e = 0, Node* rt = NULL, Node* lt = NULL) {
    elem  = e;
    right = rt;
    left  = lt;
}

Node::Node(Node* node) {
    elem  = node.getElem();
    right = node.getRight();
    left  = node.getLeft();
}

int Node::getElem() {
    return elem;
}

Node* Node::getRight() {
    return right;
}

Node* Node::getLeft() {
    return left;
}
