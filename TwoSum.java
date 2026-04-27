import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {

        // using HashMap
        HashMap<Integer, Integer> countFreq = new  HashMap<Integer, Integer>();


        for(int item = 0; item < nums.length; item++){
            int k = target - nums[item];

            if(countFreq.containsKey(k)){
                return new int[] {countFreq.get(k), item};
            }

            countFreq.put(nums[item], item);

        }

        return new int[] {};
    }

    public static void main(String[] args){
        
        int[] nums = new int[]{2,2,1,1,1,2,2};
        int target = 9;

        TwoSum sol = new TwoSum();

        System.out.println(sol.twoSum(nums, target));

    }

}
