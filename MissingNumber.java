import java.util.Arrays;
public class MissingNumber {
    public int missingNumber(int[] nums) {
            // Arrays.sort(nums); // n log n
            // for(int i=0; i<nums.length; i++){ // n
            //     if(nums[i] != i){
            //         return i;
            //     }
            // }
            // return nums.length;

            int target = (nums.length * (nums.length  + 1)) / 2;

            int totalSum = 0;
            for(int i=0; i<nums.length; i++){ 
                totalSum += nums[i];
            }

            return target - totalSum;
    }

    public static void main(String[] args){

        int[] arr = new int[]{9,6,4,2,3,5,7,0,1};
        MissingNumber mn = new MissingNumber();
        System.out.println(mn.missingNumber(arr));

    }
}
