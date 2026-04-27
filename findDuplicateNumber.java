import java.util.HashMap;

public class findDuplicateNumber {
    public int findDuplicate(int[] nums) {
        // HashMap<Integer, Integer> hm = new HashMap<Integer, Integer>();

        // for(int item : nums){
        //     hm.put(item, hm.getOrDefault(item, 0) + 1);
        // }

        // for(int item : hm.keySet()){
        //     if(hm.get(item) > 1){
        //         return item;
        //     }
        // }

        // return -1;

        // Floyd's Tortoise and Hare (Cycle Detection)

        int slow = nums[0];
        int fast = nums[0];
        
        do { 
            slow = nums[slow];
            fast = nums[nums[fast]];
        }while( slow != fast);
        
        
        slow = nums[0];

        while( slow != fast){
            slow = nums[slow];
            fast = nums[fast];
        }
        
        return fast;



    }

    public static void main(String[] args){

        int[] nums = new int[]{1,3,4,2,2};
        findDuplicateNumber fd = new findDuplicateNumber();
        System.out.println(fd.findDuplicate(nums));
    }
    
    
}
