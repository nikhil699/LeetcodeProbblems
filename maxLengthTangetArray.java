public class maxLengthTangetArray {

    public void maxLengthArray(int[] nums, int target){
        int left = 0;
        int maxSum = 0;
        int maxCount = Integer.MAX_VALUE;

        for(int right = 0; right < nums.length; right++){

            maxSum = maxSum + nums[right];
 
            while(maxSum > target){
                maxSum = maxSum - nums[left];
                left = left + 1;
                maxCount = Math.min(maxCount, right - left + 1);
            }    
      
            
        }

        if (maxCount == Integer.MAX_VALUE) {
            System.out.println(0); // no valid subarray
        } else {
            System.out.println(maxCount);
        }

    }
    public static void main(String[] args) {
        int target = 7;
        int[] nums = {2,3,1,2,4,3,7};

        maxLengthTangetArray sol = new maxLengthTangetArray();
        sol.maxLengthArray(nums,target); // output = 2
        
    }
    
}
