import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

class Node {
    int count;
    int clipboard;

    public Node(int count, int clipboard) {
        this.count = count;
        this.clipboard = clipboard;
    }

    public Node(Node n) {
        this.count = n.count;
        this.clipboard = n.clipboard;
    }

    static Node copy(Node n) {
        return new Node(n);
    }

    static Node clipBoard(Node n) {
        return new Node(n.count, n.count);
    }

    static Node copyWrite(Node n) {
        return new Node(n.count + n.clipboard, n.clipboard);
    }

    static Node deleteOne(Node n) {
        return new Node(n.count - 1, n.clipboard);
    }
}

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int answer = 0;
        int target = Integer.parseInt(br.readLine());
        int[][] visit = new int[4000][4000];
        boolean exitFlag = true;

        List<Node> que = new ArrayList<>();

        Node start = new Node(1, 0);
        visit[1][0] = 1;

        que.add(start);

        while (!que.isEmpty() && exitFlag) {
            List<Node> temp = new ArrayList<>();
            answer += 1;
            for (var ele : que) {
                if (allExecute(temp, ele, visit, target)) {
                    exitFlag = false;
                }
            }
            que = temp;
        }
        System.out.println(answer);
    }

    static public boolean allExecute(List<Node> list, Node n, int[][] visit, int target) {
        Node newNode = Node.copyWrite(n);
        if (addNode(list, newNode, visit, target)) return true;

        newNode = Node.clipBoard(n);
        if (addNode(list, newNode, visit, target)) return true;

        newNode = Node.deleteOne(n);
        if (addNode(list, newNode, visit, target)) return true;
        return false;
    }

    public static boolean addNode(List<Node> list, Node n, int[][] visit, int target) {
        if (n.count == target) return true;
        if ( checkBound(n) && visit[n.count][n.clipboard] == 0) {
            visit[n.count][n.clipboard] = 1;
            list.add(n); 
        }
        return false;
    }

    private static boolean checkBound(Node n) {
        return 0 <= n.count && n.count < 4000 && 0 <= n.clipboard && n.clipboard < 4000;
    }
}
