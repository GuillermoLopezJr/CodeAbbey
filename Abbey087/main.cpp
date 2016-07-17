#include <iostream>
#include "BinaryTree.h"

using namespace std;

int main() {
    int testCases = -1;
    cout << "input data:" << endl;
    cin >> testCases;
    int data[testCases];

    for (int i = 0; i < testCases; i++) {
        cin >> data[i];
    }

    BinaryTree tree(data[0]);

    for (int i = 1; i < testCases; i++) {
       tree.insert(data[i]);
    }
    tree.inOrderTraversal(tree.getRoot());
   return 0;
}

