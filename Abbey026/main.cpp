//find GCD and LCM using Euclidean Algo.
#include <iostream>
#include <sstream>
#include <string>
using namespace std;

//fuction prototype
int getGCD(int, int);

int main(){
	cout << "input data: " << endl;
	int TEST_CASES;
	cin >> TEST_CASES;
	cout << "\nanswer: " << endl;
	for(int i = 0; i < TEST_CASES; i++){
		int num1, num2;
		cin >> num1 >> num2;
		int gcd = getGCD(num1, num2);
		int lcm = num1 * num2 / gcd;
		ostringstream output;
		output << "(" << gcd << " " << lcm << ") ";
		cout << output.str();
	}
	return 0;
}

int getGCD(int a, int b){
	bool remFlag = false;
	while (remFlag == false){
		if (a > b){
			int rem = a % b;
			a = rem;
			if (rem == 0) {
				remFlag = true;
			}
			
		}
		else{
			int rem = b % a;
			b = rem;
			if (rem == 0) {
				remFlag = true;
			}
		}
	}
	return ( (a > b) ? a : b);
}
