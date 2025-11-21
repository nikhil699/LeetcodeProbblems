// Transpose of Matrix
// Socho ki ek matrix ko 90° clockwise rotate karna matlab kya hai?
// Jo top row hai, wo ban jaati hai last column.
// Jo bottom row hai, wo ban jaati hai first column.
// Basically, rows → columns ban jaati hain in reverse order.
// Isko efficient tarike se karne ke liye do steps use karte hain:
// Transpose the matrix (rows ko columns bana do).

// 1 2 3      1 4 7
// 4 5 6  →   2 5 8
// 7 8 9      3 6 9


// Reverse each row (taaki clockwise rotation ho jaaye).

// 1 4 7      7 4 1
// 2 5 8  →   8 5 2
// 3 6 9      9 6 3




// Time : 0(n)
// Space : 0(n)
import java.lang.Math;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.stream.Collectors;
public class solution{

    public  int[] moveZeroToRight(int[] arr)
        {
            int[] result = new int[arr.length];

            for(int i=0;i<arr.length;i++){
                result[i] = 0;
            }

            int p = 0;

            for(int item = 0; item < result.length; item++){
                if(arr[item] != 0){
                    result[p] = arr[item];
                    p = p + 1;
                }
            }

            return result;
        }

        // Rotate a Matrix by 90 Degrees Clockwise
        // Time : 0(n)
        // Space : 0(n)

        public int[][] rotateAMatrixBy90Degree(int[][] arr){
            
            for(int i = 0; i < arr.length;i++){
                for(int j = i+1 ; j < arr.length;j++){
                    int temp = arr[i][j];
                    arr[i][j] = arr[j][i];
                    arr[j][i] = temp;
                }
            }

            for(int i = 0; i < arr.length; i++){
                   int left = 0;
                   int right = arr.length - 1;

                   while(left < right){
                    int temp = arr[i][left];
                    arr[i][left] = arr[i][right];
                    arr[i][right] = temp;
                    left = left + 1;
                    right = right - 1;
                   }

                
            }

            return arr;
        }

        // Sort a HashMap by Values

        public void sortValuesInHashmap(){
            HashMap<Integer,Integer> storage = new HashMap<>();

            storage.put(1,23);
            storage.put(3,03);
            storage.put(7,34);
            storage.put(6,90);
            storage.put(9,10);
            storage.put(2,04);
            storage.put(8,19);
            storage.put(4,12);
            

            // entrySet().stream() → map ke key-value pairs ko stream mein convert
            // sorted(Map.Entry.comparingByValue()) → values ke hisaab se sort
            // Collectors.toMap(...) → stream ko nayi LinkedHashMap mein collect
            // (oldVal, newVal) -> oldVal → agar duplicate key ho to purani value rakhe
            // LinkedHashMap::new → insertion order maintain kare

            LinkedHashMap<Integer, Integer> sortedMap = 
                storage.entrySet()
                .stream()
                .sorted(Map.Entry.comparingByValue())
                .collect(Collectors.toMap(Map.Entry::getKey, Map.Entry::getValue, (oldVal, newVal) -> oldVal,
                LinkedHashMap :: new
                ));

            System.out.println(sortedMap);

        }


        // water can be trapped after raining.
        // The water tapped between the bars is being the maximum heights of their left and thrir right .
        // Trapped water at bar i = min(maxLeft[i], maxRight[i]) - height[i]
        // Agar result negative ho jaye, to 0 water trap hota hai us position par.
        // Use pre-computed left max array aur right max array for O(n) solution.

        public int maximumTappedWater(int[] nums){
            int[] leftMax = new int[nums.length];
            int[] rightMax = new int[nums.length];

            if(nums.length == 0){
                return 0;
            }
            
            leftMax[0] = nums[0];
            for(int i=1;i<nums.length;i++){
                leftMax[i] = Math.max(nums[i], leftMax[i-1]);
            }
            
            rightMax[nums.length - 1] = nums[nums.length - 1];
            for(int i = nums.length - 2; i >= 0; i--){
                rightMax[i] = Math.max(rightMax[i+1], nums[i]);
            }


            int trappedWater = 0;
            for(int i = 0; i < nums.length; i++){
            trappedWater += Math.min(leftMax[i], rightMax[i]) - nums[i];
             }

            return trappedWater;

        }

        class ListNode {
            int val;
            ListNode next;
            ListNode(int x) { val = x; }
        }

        
        public ListNode rotateFromCenter(ListNode head) {
                if (head == null || head.next == null) return head;
        
                // Step 1: Find middle using slow-fast pointer
                ListNode slow = head, fast = head, prev = null;
                while (fast != null && fast.next != null) {
                    prev = slow;
                    slow = slow.next;
                    fast = fast.next.next;
                }
        
                // Step 2: Break list into two halves
                prev.next = null; // first half end
        
                ListNode secondHalf = slow;
                ListNode firstHalf = head;
        
                // Step 3: Go to end of second half and attach first half
                ListNode temp = secondHalf;
                while (temp.next != null) {
                    temp = temp.next;
                }
                temp.next = firstHalf;
        
                // Step 4: Return new head
                return secondHalf;
            
        }
        

        public static void main(String[] args) {

            int[] arr = new int[]{1,0,-2,0,0,5,9,6};
            solution sol = new solution();
            int k = arr.length;
            int result[] = sol.moveZeroToRight(arr);

        for(int i=0; i<k; i++)
        {
            System.out.println(result[i]);
        }

        int[][] matrix = {
            {1,2,3},
            {4,5,6},
            {7,8,9}
        };

        int[][] output = sol.rotateAMatrixBy90Degree(matrix);

        for(int[] row : output)
        {
            for(int o : row){
                System.out.println(o+ " ");
            }
            System.out.println();
        }
      
        sol.sortValuesInHashmap();

        int[] nums = new int[]{0,1,0,2,1,0,1,3,2,1,2,1};

        System.out.println(sol.maximumTappedWater(nums));

        System.out.println(sol.rotateFromCenter(null));
        
        }


}