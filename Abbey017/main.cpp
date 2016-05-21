#include <iostream>
using namespace std;

//function prototype
int getCheckSum(int arr[], int SIZE);

int main(){
	cout << "input date: " << endl;
	int size;
	cin >> size;
	int arr[size];
	
	for (int i = 0; i < size; i++){
		int elt;
		cin >> elt;
		arr[i] = elt;
	}

	cout << "\nanswer: " << endl;
	int checkSum = getCheckSum(arr, size);
	cout << checkSum << endl;
	return 0;
}

int getCheckSum(int arr[], int SIZE){
	long int result = 0;
	const int SEED = 113;
	const int LIMIT = 10000007; 

	for (int i = 0; i < SIZE; i++){
		result = (result + arr[i]) * SEED;
		if (result >= LIMIT){
			result = result % LIMIT;
		}
	}
	return result;
}
