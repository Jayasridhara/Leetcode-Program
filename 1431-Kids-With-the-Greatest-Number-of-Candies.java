class Solution {
     
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
       List<Boolean> l = new ArrayList<>();
        for(int i=0;i<candies.length;i++)
        {
            int f=1;
           int  c = extraCandies + candies[i];
           for(int j : candies)
           if(j>c)
           {
               f=0;
               l.add(false);
               break;
           }
           if(f==1)
           l.add(true);
        }
        return l;
    }
}