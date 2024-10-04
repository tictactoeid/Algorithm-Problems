import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";

        String[] strings = s.split(" ");

        int max = Integer.MIN_VALUE;
        int min = Integer.MAX_VALUE;
        // System.out.println(Arrays.toString(strings));
        for (String x: strings) {
            int n = Integer.parseInt(x);
            if (max < n) {
                max = n;
            }
            if (min > n) {
                min = n;
            }
        }

        answer += Integer.toString(min);
        answer += " ";
        answer += Integer.toString(max);

        return answer;
    }
}