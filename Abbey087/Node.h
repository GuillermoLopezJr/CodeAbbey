#include <iostream>
using namespace std;

class Node {
private:
    friend class BinaryTree;
    int elem;
    Node* right;
    Node* left;

public:
    Node(int e = 0, Node* rt = nullptr, Node* lt = nullptr);
    Node(Node& node); 
    int getElem();
    Node* getRight();
    Node* getLeft();
    friend ostream& operator<<(ostream& os, const Node& node);
};
