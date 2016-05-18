#include <iostream>
#include "Date.h"
using namespace std;


//function prototype.
Date getDate();
void printDates(const Date dates[], int size);

int main(){	
	cout << "input data: " << endl;
	int size;
	cin >> size;
	Date dates[size];

	for(int i = 0; i < size; i++){
		Date date1 = getDate();
		Date date2 = getDate();	
		Date interval = date2 - date1;
		dates[i] = interval;
	}	
	cout << "\nanswer: " << endl;
	printDates(dates, size);
	return 0;
}

Date getDate(){
	int day, hr, min, sec;
	cin >> day >> hr >> min >> sec;
	Date date (day, hr, min, sec);
	return date;
}

void printDates(const Date dates[], int size){
	for(int i = 0; i < size; i++){
		cout << dates[i] << " ";
	}
}
