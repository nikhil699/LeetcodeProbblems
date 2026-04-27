import java.util.HashMap;

public class subarraySumEqualsK {
    public int subarraySum(int[] nums, int k) {
        // count of every element
        HashMap<Integer, Integer> countFreq = new HashMap<Integer, Integer>();
        countFreq.put(0,1);

        int count = 0;
        int prefixSum = 0;

        for(int item=0; item < nums.length; item++){
            prefixSum += nums[item];

            if(countFreq.containsKey(prefixSum - k)){
                count += countFreq.get(prefixSum - k);
            }

            countFreq.put(prefixSum,countFreq.getOrDefault(prefixSum, 0) + 1);
        }

        return count;

    }

    public static void main(String[] args){
        int[] nums = new int[]{1,2,3};

        int k = 3;

        subarraySumEqualsK sol = new subarraySumEqualsK();

        System.out.println(sol.subarraySum(nums, k));
    }

}
