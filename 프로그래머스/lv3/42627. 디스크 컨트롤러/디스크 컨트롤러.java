import java.util.*;
import java.io.*;

class Solution {
    public PriorityQueue<int[]> makeQue() {
        return new PriorityQueue(new Comparator<int[]> () {
            @Override
            public int compare(int[] o1, int[] o2){
                return o1[1] - o2[1];
            }
        });
    }
    public int solution(int[][] jobs) {
        int answer = 0;
        Arrays.sort(jobs, (o1, o2) -> {return o1[0] - o2[0];});
        
        PriorityQueue<int[]> que = makeQue();
        int crt = 0;
        int i = 0;
        
        while (i < jobs.length) {
            // System.out.println(answer + " => "+ crt);
            if (crt < jobs[i][0]) {
                int[] ele;
                if (que.peek() != null) {
                    ele = que.poll();
                    crt += ele[1];
                } else {
                    ele = jobs[i];
                    crt = ele[0];
                }    
                answer += crt - ele[0];
            } else if(crt >= jobs[i][0]) {
                que.add(jobs[i]);
                i += 1;
            }
        }
        
        while (que.peek() != null) {
            int[] ele = que.poll();
            crt += ele[1];
            answer += crt - ele[0];
        }
        
        return answer/jobs.length;
    }
}