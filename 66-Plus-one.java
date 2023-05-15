import java.util.*;
class Solution {
    public int[] plusOne(int[] digits) {
int r;
int n=digits.length;
int i=n-1;
for(i=n-1;i>=0;i--)
{
if(digits[i]<9)
{
digits[i]+=1;
return digits;
}
else
digits[i]=0;
}

int nine[] = new int[digits.length + 1];
nine[0] = 1;
return nine;



    }
}