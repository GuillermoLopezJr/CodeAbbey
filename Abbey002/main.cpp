#include <iostream>
using namespace std;

int main(){
	int totalNum;
	cout << "Input data: " << endl;
	cin >> totalNum;

	int total = 0;
	int num;
	for(int i = 0; i < totalNum; i++){
		cin >> num;
		total += num;
	}

	cout << "Total is: " << total << endl;
	return 0;
}
