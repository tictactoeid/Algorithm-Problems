import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int x: scoville) {
            heap.add(x);
        }

        while (heap.size() >= 2) {
            int food1 = heap.poll();
            if (food1 >= K) {
                break;
            }
            int food2 = heap.poll();
            int new_food = food1 + food2 * 2;
            heap.add(new_food);
            answer++;
        }
        if (heap.size() < 2 && heap.peek() < K) {
            return -1;
        }


        return answer;
    }



}