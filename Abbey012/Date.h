#include <iostream>
using namespace std;
class Date{
public:
	static const int SECOND = 1;
	static const int MINUTE = 60 * SECOND;
	static const int HOUR = 60 * MINUTE;
	static const int DAY = 24 * HOUR; 

	long int day, hr, min, sec;
	Date(){}
	Date(long int day, long int hr, long int min, long int sec);
	long int totalSec() const;
	Date operator-(const Date& date2);

	friend ostream& operator<<(ostream& os, const Date& date);

};

Date::Date(long int day, long int hr, long int min, long int sec){
	this->day = day;
	this->hr  = hr;
	this->min = min;
	this->sec  = sec;
}

long int Date::totalSec() const{
	return (day*DAY + hr * HOUR + min * MINUTE + sec);
}

Date convertSecToDate(long int totalSec){
	int dayCounter, hrCounter, minCounter, secCounter;
	dayCounter = hrCounter = minCounter = secCounter = 0;
	
	while(totalSec >= Date::DAY){
		dayCounter++;
		totalSec -= Date::DAY;
	}

	while(totalSec >= Date::HOUR){
		hrCounter++;
		totalSec -= Date::HOUR;
	}

	while(totalSec >= Date::MINUTE){
		minCounter++;
		totalSec -= Date::MINUTE;
	}

	secCounter = totalSec;
	
	Date date (dayCounter, hrCounter, minCounter, secCounter);
	return date;
}


Date Date::operator-(const Date& date2){
	Date returnDate;
	date2.totalSec();
	long int elapsedSec = this->totalSec() - date2.totalSec(); 	
	returnDate = convertSecToDate(elapsedSec);		
	return returnDate;	
}

ostream& operator<<(ostream& os, const Date& date){
	os << "(" << date.day << " " << date.hr << " " << date.min << " " << date.sec << ")";
	return os;

}
