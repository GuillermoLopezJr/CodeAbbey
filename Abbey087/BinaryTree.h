#include "Node.h"
#include <iostream>

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
    //traversals
    void preOrderTraversal(Node* node);
    void inOrderTraversal(Node* node);
    void postOrderTraversal(Node* node);
    friend ostream& operator<<(ostream& os, const BinaryTree& tree);
};

//ostream& operator<<(ostream& os, const BinaryTree& tree) {
 //  cout << tree.getRoot() << endl;
//}



