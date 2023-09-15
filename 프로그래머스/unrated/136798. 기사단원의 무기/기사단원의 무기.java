class Solution {
    public int check(int n){
        int cnt=0;
        for(int i=1; i*i<=n; i++){
            if(i*i==n){
                cnt+=1;
            }else if(n%i==0){
                cnt+=2;
            }
        }
        return cnt;
    }
    public int solution(int number, int limit, int power) {
        int result = 0;
        for(int i=1; i<=number; i++){
            int num = check(i);
            if(num>limit){
                result += power;
            }else{
                result += num;
            }
        }
        return result;
    }
}