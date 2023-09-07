import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws Exception{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int F,S,G,U,D;
		F = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());
		G = Integer.parseInt(st.nextToken());
		U = Integer.parseInt(st.nextToken());
		D = Integer.parseInt(st.nextToken());
		
		ArrayDeque<Integer> que = new ArrayDeque<>();
		boolean visit[] = new boolean[F+1];
		boolean isAns = false;
		int[] ud = new int[2];
		int level = 0;
		que.offer(S);
		visit[S] = true;
		while (!que.isEmpty() && !visit[G]) {
			int size = que.size();
			
			while(--size >= 0) {
				int crt = que.poll();
				
				ud[0] = crt + U;
				ud[1] = crt - D;
				for (int i = 0; i < 2; i++) {
					if (outBound(ud[i], F)) continue;
					if (visit[ud[i]] == true) continue;
					visit[ud[i]] = true;
					que.offer(ud[i]);
				}
			}
			level++;
		}
		System.out.println(visit[G] ? level : "use the stairs");
	}

	private static boolean outBound(int i, int f) {
		if (i < 1 || i >f)return true;
		return false;
	}
}
