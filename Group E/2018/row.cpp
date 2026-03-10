#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s;
    int k = 0, count = 0;
    cin >> s;
    cin >> k;

    int n = s.length();
    for (int i = 0; i < n; i++)
    {
        int zeros = 0;
        for (int j = i; j < n; j++)
        {
            if (s[j] == '0')
                zeros++;
            if (zeros == k) count++;
            if (zeros > k) break;
        }
    }
    cout << count << endl;
}
