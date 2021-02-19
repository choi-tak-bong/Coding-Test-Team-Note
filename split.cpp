// 출처: https://ssungkang.tistory.com/

#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;

vector<string> split(string str, char delimiter);

int main()
{
    // Example
    string test = "min sung kang";
    vector<string> result = split(test, ' ');
    for (int i = 0; i < result.size(); i++)
    {
        cout << result[i] << " ";
    }
}

vector<string> split(string str, char delimiter)
{
    vector<string> answer;
    stringstream ss(str);
    string temp;

    while (getline(ss, temp, delimiter))
    {
        answer.push_back(temp);
    }

    return answer;
}
