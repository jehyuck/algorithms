#include <string>
#include <iostream>
#include <vector>

using namespace std;

void bfs(vector<vector<int>> &computers, int idx){
    // cout << idx << endl;
    computers[idx][idx] = 0;
    for(int i = 0; i < computers.size(); i++) {
        if (computers[idx][i] == 0) continue;
        computers[idx][i] = 0;
        computers[i][idx] = 0;
        bfs(computers, i);
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    
    for(int i = 0; i < n; i++) {
        if (computers[i][i] == 0) continue;
        answer += 1;
        computers[i][i] = 0;
        bfs(computers, i);
    }
    return answer;
}