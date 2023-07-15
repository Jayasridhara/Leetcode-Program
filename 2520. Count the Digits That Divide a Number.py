int countDigits(int num){
    int a,c=0,r;
    a=num;
    while(num)
    {
        r=num%10;
        if (a%r==0)
        c++;
        num=num/10;
    }
    return c;

}