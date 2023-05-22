#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
 
using namespace std;
string solution(string s) {
    string answer = "";
    istringstream ss(s);
    
    vector<int> v;
    string tmp;
    while (getline(ss, tmp, ' ')) {
        v.push_back(stoi(tmp));
    }
    
    sort(v.begin(),v.end());
    
    answer += to_string(v.front())+" "+ to_string(v.back());
    return answer;
}
