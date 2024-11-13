import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    static final int inf = 10_000 * 100 + 1;

    static class Node {
        int time;
        int sumTime = -1;
        int count = 0;
        List<Integer> adj;
        public Node(int time, List<Integer> adj) {
            this.time = time;
            this.adj = adj;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        Set<Integer> visit = new HashSet<>();

        Map<Integer, Node> adj = inputAdjMap(br, N, visit);

        Iterator<Integer> visitIter = visit.stream().iterator();
        int answer = inf;

        Queue<Integer> que = new ArrayDeque<>();

        while (visitIter.hasNext()) {
            int nodeNumber = visitIter.next();
            que.add(nodeNumber);
        }
        answer = bfs(adj, que);
        System.out.println(answer);
    }

    private static int bfs(Map<Integer, Node> adj, Queue<Integer> que) {
        int rtn = 0;

        while (!que.isEmpty()) {
            int ele = que.poll();
            Node crt = adj.get(ele);
            if (crt.sumTime > rtn) {
                rtn = crt.sumTime;
            }
            for (int i = 0; i < crt.adj.size(); i++) {
                int next = crt.adj.get(i);
                Node nextNode = adj.get(next);

                nextNode.count -= 1;
                nextNode.sumTime = Math.max(nextNode.sumTime, crt.sumTime + nextNode.time);
                if (nextNode.count == 0) {
                    que.add(next);
                }
            }
        }
        return rtn;
    }

    private static Map<Integer, Node> inputAdjMap(BufferedReader br, int n, Set<Integer> visit) throws IOException {
        Map<Integer, Node> adj = new HashMap<>();
        StringTokenizer st;
        StringTokenizer[] sts = new StringTokenizer[n + 1];
        for (int i = 1; i < n + 1; i++) {
            int time, len;
            st = getTokenizer(br);
            time = getInt(st);
            sts[i] = st;
            adj.put(i, new Node(time, new ArrayList<>()));
        }
        for (int i = 1; i < n + 1; i++) {
            int len = getInt(sts[i]);
            if (len == 0) {
                visit.add(i);
                adj.get(i).sumTime = adj.get(i).time;
            }
            adj.get(i).count = len;
            inputAdj(adj, visit, len, sts[i], i);
        }
        return adj;
    }

    private static void inputAdj(Map<Integer, Node> adj, Set<Integer> visit, int len, StringTokenizer st, int crtNode) {
        for (int j = 0; j < len; j++) {
            int node = getInt(st);
            adj.get(node).adj.add(crtNode);
        }
    }

    private static int getInt(StringTokenizer st) {
        return Integer.parseInt(st.nextToken());
    }

    static StringTokenizer getTokenizer(BufferedReader br) throws IOException {
        return new StringTokenizer(br.readLine());
    };
}