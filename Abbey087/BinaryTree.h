#include "Node.h"
using namespace std;

class BinaryTree {
private:
    Node* root;

public:
    BinaryTree();
    BinaryTree(int elem);
    void setRoot(Node* n);
    bool isEmpty();
    Node* insert(Node* n, int elem);
    void insert(int elem);
    Node* getRoot();
};
