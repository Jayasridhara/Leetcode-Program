int averageValue(int* nums, int n)
{
    int c=0,i,j,s=0,a;
    for(i=0;i<n;i++)
    if(nums[i]%2==0 && nums[i]%3==0)
    {
        s=s+nums[i];
        c++;
    }
    if(c>0)
    {
        a=s/c;
        return a;
    }
    else
    return 0;

}