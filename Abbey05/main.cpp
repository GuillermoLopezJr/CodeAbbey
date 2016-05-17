#include <iostream>
using namespace std;

//fuction prototype
int getMin(int arr[], const int SIZE);
void printArr(int arr[], const int SIZE);

int main(){
	cout << "Enter data: " << endl;
	int totalTriplets;
	cin >> totalTriplets;

	int minArr[totalTriplets];
	for(int i = 0; i < totalTriplets; i++){
		int first, second, third;
		cin >> first >> second >> third;
		int list[3] = { first, second, third };
		minArr[i] = getMin(list, 3);
	}

	cout << "Answer: " << endl;
	printArr(minArr,totalTriplets);
	return 0;
}

int getMin(int arr[], const int SIZE){
	int min = arr[0];
	for(int i = 0; i < SIZE; i++){
		if (arr[i] < min){
			min = arr[i];
		}
	}	
	return min;
}

void printArr(int arr[], const int SIZE){
	for(int i = 0; i < SIZE; i++){
		cout << arr[i] << " ";
	}
}
