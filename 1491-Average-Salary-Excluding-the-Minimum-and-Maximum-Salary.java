import java.util.*;
class Solution {
    public double average(int[] salary) {
Arrays.sort(salary);
int s=0;
    for(int i=1;i<salary.length-1;i++)
    s+=salary[i];
    return (double)s/(salary.length-2);
    }

}