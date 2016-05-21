#include <iostream>
#include <ctype.h>
using namespace std;

int getScore(string line){
	int score = 0;

	for (char c : line){
		if (c != ' '){
			if (isdigit(c)){
				int digit = c - '0';
				score += digit;
			}
			else if (c == 'K' || c == 'Q' || c == 'J' || c == 'T'){
				score += 10;
			}			
			else if (c == 'A'){
				if ( (score + 11) > 21 ){
					score += 1;
				}
				else{
					score += 11;
				}
			}
		}
	}
	return score;
}

int main(){
	cout << "input data:" << endl;
	int size;
	cin >> size;
	int scores[size];
	cin.ignore();

	for (int i = 0; i < size; i++){
		string line;
		getline(cin, line);		
		scores[i] = getScore(line);
		
	}
	
	cout << "answer: " << endl;
	for (int i = 0; i < size; i++){
		if (scores[i] > 21){
			cout << "Bust ";
		}
		else{
			cout << scores[i] << " ";
		}
	}
	return 0;
}
