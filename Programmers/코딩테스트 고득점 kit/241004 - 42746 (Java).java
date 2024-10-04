import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";

        String[] strings = new String[numbers.length];

        for (int i=0; i<numbers.length; i++) {
            strings[i] = Integer.toString(numbers[i]);
        }


        Comparator<String> comparator = new Comparator<>() {
            @Override
            public int compare(String n1, String n2) {
                // String s1 = n1.repeat(3);
                // String s2 = n2.repeat(3);
                // return -1 * s1.compareTo(s2);
                return (n2+n1).compareTo(n1+n2);
            }
        };

        Arrays.sort(strings, comparator);
        //System.out.println(Arrays.toString(strings));
        answer = String.join("", strings);
        int start = 0;
        int end = answer.length() - 1;
        while (start <= end && answer.charAt(start) == '0') {
            start++;
        }
        if (end-start > 0)
            return answer.substring(start, end+1);

        return "0";
    }
}