import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList <Integer> data = new ArrayList<>();
        int temp = -1;
        for(int num:arr){
            if(temp!=num){
                data.add(num);
                temp = num;
            }
        }
        return data.stream().mapToInt(i->i).toArray();


    }
}