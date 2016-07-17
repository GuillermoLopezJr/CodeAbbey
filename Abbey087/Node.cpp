#include "Node.h"

Node::Node(int e, Node* rt, Node* lt) {
    elem  = e;
    right = rt;
    left  = lt;
}

Node::Node(Node& node) {
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

ostream& operator<<(ostream& os, const Node& node) {
    os << "(";
    if (node.left == nullptr) {
        os << "-";
    }
    else {
        os << node.left->elem;
    }
    os << "," << node.elem << ",";
    if (node.right == nullptr) {
        os << "-";
    }
    else {
        os << node.right->elem;
    }
    os << ")";

    return os;
}
