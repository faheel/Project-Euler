/*
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
	Find the sum of all the primes below two million.
*/

#include <iostream>
#include <cmath>

using namespace std;

bool isPrime(int num)
{
	for (int i = 2; i <= sqrt(num); i++)
		if (num%i == 0 && num != i)
			return false;
	
	return true;
}

int main()
{
	long long sum = 0;
	
	for (int num = 2; num < 2000000; num++)
		if (isPrime(num))
			sum += num;
			
	cout << "Sum of all primes less than 2 million = " << sum;

	return 0;
}

