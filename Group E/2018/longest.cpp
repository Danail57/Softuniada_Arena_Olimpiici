#include <iostream>
#include <string>
using namespace std;


int main()
{
    int k;
    string s;
    cin >> k;
    cin >> s;

    int n = s.length();
    int left = 0, max_len = 0, start_idx = -1;
    int count[26] = {0};
    int unique_k_letters = 0;

    for (int right = 0; right < n; right++)
    {
        if (s[right] >= 'a' && s[right] < 'a' + k)
        {
            if (count[s[right] - 'a'] == 0)
                unique_k_letters++;
            count[s[right] - 'a']++;
        }
        while (unique_k_letters > 1)
        {
            if (s[left] >= 'a' && s[left] < 'a' + k)
            {
                count[s[left] - 'a']--;
                if (count[s[left] - 'a'] == 0)
                    unique_k_letters--;
            }
            left++;
        }
        if (unique_k_letters == 1)
        {
            int current_len = right - left + 1;
            if (current_len > max_len) {
                max_len = current_len;
                start_idx = left;
            }
        }
    }
    if (max_len == 0) {
        cout << 0 << endl;
    } else {
        cout << max_len << endl;
        cout << s.substr(start_idx, max_len) << endl;
    }
}
