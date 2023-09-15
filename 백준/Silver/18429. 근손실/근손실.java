import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N, K = 0;
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        List<Integer> li = new ArrayList<>();
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < N; i++) {
            li.add(Integer.parseInt(st.nextToken()));
        }
        boolean[] visit = new boolean[N];
        System.out.println(dfs(500, K, li, N, 0, visit));
    }

    public static int dfs(int crt, int minus, List<Integer> li, int N, int crtCount, boolean[] visit) {
        if (crt < 500) {
            return 0;
        }
        if (crtCount >= N) {
            return 1;
        }

        int rtn = 0;

        for (int i = 0; i < N; i++) {
            if (visit[i]) continue;
            visit[i] = true;
            rtn += dfs(crt - minus + li.get(i), minus, li, N, crtCount + 1, visit);
            visit[i] = false;
        }
        return rtn;
    }
}