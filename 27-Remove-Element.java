import java.util.*;
import java.util.stream.*;
class Solution {
    public int removeElement(int[] nums, int val) {

    List<Integer> l=IntStream.of(nums).filter(x -> x!=val ).boxed().collect(Collectors.toList());
int j=0;
    for (Integer i:l)
    nums[j++]= i;
    return j;


    }
}