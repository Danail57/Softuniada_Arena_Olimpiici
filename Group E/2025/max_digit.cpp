#include <iostream>
#include <vector>
using namespace std;


int get_digit(int number, int k)
{
	if (k == 1) return number / 100;
	if (k == 2) return (number / 10) % 10;
	if (k == 3) return number % 10;
}

int solve(vector <int> numbers, int k)
{
	int max_digit = -1;
	for (int i = 0; i < numbers.size(); i++)
	{
		int current_digit = get_digit(numbers[i], k);
		if (9 + (current_digit - 5) > 8)
		{
			if (current_digit > max_digit)
			{
				max_digit = current_digit;
			}
		}
	}
	return max_digit;
}

int main()
{
	int first_3_digit_number, second_3digit_number, third_3_digit_number, k;
	vector <int> numbers = { first_3_digit_number, second_3digit_number, third_3_digit_number };
	int result = solve(numbers, k);
	if (result == -1)
	{
		cout << "No" << endl;
	}
	else {
		cout << result << endl;
	}
	return 0;
}
