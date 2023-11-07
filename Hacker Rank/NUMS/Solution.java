class Solution {
    public static void main(String[] args) {
        int i;
        int [] nums = {-1,0,3,5,9,12};
        int solution = 0, target = 9;
        int left = 0, right = nums.length - 1;
        for(i = 6; i < nums.length; i--){
            if(target == nums[i]){
                solution = i;
                System.out.println(solution);
                
            }else{
                solution = nums[0];
                System.out.println(solution);
            }
        }
    }
}