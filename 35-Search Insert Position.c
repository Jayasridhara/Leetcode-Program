int searchInsert(int* nums, int numsSize, int target){
    int c=0,i;
for(i=0;i<numsSize;i++)
{
if(target>nums[i])
c++;
}
printf("%d",c);
return c;

}