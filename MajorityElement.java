import java.util.HashMap;

public class MajorityElement {
    public int majorityElement(int[] nums) {
        int majority = nums.length / 2;

        HashMap<Integer, Integer> countFreq = new HashMap<Integer, Integer>();

        for(int item = 0;item < nums.length; item++){
            countFreq.put(nums[item], countFreq.getOrDefault(nums[item], 0) + 1);
        }

        for(int item : nums){
            if(countFreq.get(item) > majority){
                return item;
            } 
        }
        return -1;    
    }

    public static void main(String[] args){
        
        int[] nums = new int[]{2,2,1,1,1,2,2};

        MajorityElement sol = new MajorityElement();

        System.out.println(sol.majorityElement(nums));

    }
}


