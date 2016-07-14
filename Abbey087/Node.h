using namespace std;

class Node {
private:
    friend class BinaryTree;
    int elem;
    Node* right;
    Node* left;

public:
    Node(int e = 0, Node* rt = NULL, Node* lt = NULL);
    Node(Node& node); 
    int getElem();
    Node* getRight();
    Node* getLeft();
}
