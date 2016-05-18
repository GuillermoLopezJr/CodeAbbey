#include <iostream>
#include <vector>
using namespace std;

//function prototype
int getCheckSum(vector<int> nums);
int bubbleSort(vector<int>& nums); //first-step towards bubbleSort
void swap(vector<int>& nums, int index, int swpIndex);

int main(){
	cout << "input date: " << endl;
	int elt;
	vector<int> nums;
	while(cin >> elt && elt != -1){
		nums.push_back(elt);
	}

	int swaps = bubbleSort(nums);
	int checkSum = getCheckSum(nums);

	cout << "\nanswer: " << endl;

	cout << swaps << " " <<  checkSum << endl;
	return 0;
}

void swap(vector<int>& nums, int index, int swpIndex){
	int temp = nums[index];
	nums[index] = nums[swpIndex];
	nums[swpIndex] = temp;
}

int bubbleSort(vector<int>& nums){
	int swaps = 0;	
	for(int i = 0; i < nums.size()-1; i++){
		if(nums[i] > nums[i+1]){
			swap(nums, i, i+1);
			swaps++;
		}
	}	
	return swaps;
}

int getCheckSum(vector<int> nums){
	long int result = 0;
	const int SEED = 113;
	const int LIMIT = 10000007; 

	for (int i = 0; i < nums.size(); i++){
		result = (result + nums[i]) * SEED;
		if (result >= LIMIT){
			result = result % LIMIT;
		}
	}
	return result;
}
