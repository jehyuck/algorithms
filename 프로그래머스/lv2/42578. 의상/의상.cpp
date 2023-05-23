#include <string>
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    
    map<string, vector<string>> partClothes;
    
    for(auto iter = clothes.begin(); iter < clothes.end(); iter++) {
        string cloth = (*iter)[0];
        string part = (*iter)[1];
        if (partClothes.find(part) == partClothes.end()) {
            vector<string> temp;
            temp.push_back(cloth);
            partClothes[part] = temp;
        } else {
            partClothes[part].push_back(cloth);
        }
    }
    
    for (auto iter = partClothes.begin(); iter != partClothes.end(); iter++) {
        int count = iter->second.size();
        answer *= (count + 1);
    }
    return answer - 1;
}