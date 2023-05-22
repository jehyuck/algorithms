#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

int solution(string numbers) {
    int answer = 0;
    
    vector<int> nums;
    set<int> result;
    for(int i=0; i < numbers.size(); i++){
        nums.push_back(numbers[i] - '0');
    }
    sort(nums.begin(), nums.end());
    
    do {
        int tmp = 0;
        
        for(int i = 0; i < nums.size(); i++){
            tmp *= 10;
            tmp += nums[i];
            result.insert(tmp);
        }
        result.insert(tmp);
    } while (next_permutation(nums.begin(), nums.end()));
    
    vector<int> resultVector;    
    for(auto iter = result.begin(); iter != result.end(); iter++)
        resultVector.push_back(*iter);
    sort(resultVector.begin(), resultVector.end());
    int max_value = *(resultVector.end() - 1);
    
    vector<int> che(max_value * 2 + 1, 0);
    che[1] = 1;
    che[0] = 1;
    int idx = 1;
    while (idx < max_value) {
        idx++;
        if (che[idx] == 1) continue;
        
        int value = 1;
        int tempIdx = idx;
        while (tempIdx <= max_value) {
            value++;
            tempIdx = value * idx;
            che[tempIdx] = 1;
        }
    }
    for (auto iter = resultVector.begin(); iter < resultVector.end(); iter++){
        if (che[*iter] == 1) continue;
        answer++;
    }
    
    return answer;
}