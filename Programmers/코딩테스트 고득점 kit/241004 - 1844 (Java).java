import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int answer = 0;

        int n = maps.length;
        int m = maps[0].length;

        boolean[][] visited = new boolean[n][m];

        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{0, 0, 1}); // r, c, dist

        while (!queue.isEmpty()) {
            int[] node = queue.poll();
            int[][] neighbors = new int[][] {
                {node[0]-1, node[1]},
                {node[0]+1, node[1]},
                {node[0], node[1]-1},
                {node[0], node[1]+1}
            };
            for (int[] neighbor: neighbors) {
                if (neighbor[0] == n-1 && neighbor[1] == m-1) {
                    return node[2] + 1;
                }

                if (0 <= neighbor[0] && neighbor[0] < n && 0 <= neighbor[1] && neighbor[1] < m) {
                    if (!visited[neighbor[0]][neighbor[1]] && maps[neighbor[0]][neighbor[1]] == 1) {
                        queue.add(new int[]{ neighbor[0], neighbor[1], node[2]+1 });
                        visited[neighbor[0]][neighbor[1]] = true;
                    }
                }

            }

        }

        return -1;
    }
}