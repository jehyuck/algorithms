import java.util.PriorityQueue;

class Solution {
    
    static void setPriorityQueue(String[] timetable, PriorityQueue<Integer> waiters) {
        for(String time : timetable) {
            waiters.add(timeToInt(time));
        }
    }
    
    static int timeToInt(String time) {
        String[] hourMinute = time.split(":");
        int hour = Integer.parseInt(hourMinute[0]) * 60;
        int minute = Integer.parseInt(hourMinute[1]);
        return hour + minute;
    }
    
    static String intToTime(int time) {
        int hour = time / 60;
        int minute = time % 60;
        return String.format("%02d:%02d", hour, minute);
    }
    
    public String solution(int n, int t, int m, String[] timetable) {
        String answer = "";
        int arrivedBusCount = 0;
        int arrivedBusTime = timeToInt("09:00");
        PriorityQueue<Integer> waiters = new PriorityQueue();
        setPriorityQueue(timetable, waiters);
        
        while (arrivedBusCount < n) {
            if (arrivedBusCount != 0) arrivedBusTime += t;
            int busCount = 0;
            
            while (!waiters.isEmpty() && busCount != m) {
                if (waiters.peek() > arrivedBusTime) break;
                if (arrivedBusCount == n - 1 && busCount == m - 1) {
                    return intToTime(waiters.poll() - 1);
                }
                waiters.poll();
                busCount += 1;
            }
            arrivedBusCount += 1;
        }
        return intToTime(arrivedBusTime);
    }
}