import java.util.*;
import java.util.stream.*;
class Solution {
    public int   removeDuplicates(int[] nums) {
        
     List<Integer> l =   IntStream.of(nums).distinct().sorted().boxed().collect(Collectors.toList());
        System.out.println(l);
      int j=0;
      for(Integer i:l)
      {
         nums[j++] = i;
      }
return j;
    }
}