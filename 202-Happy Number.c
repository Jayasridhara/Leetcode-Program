int  sum(int);
bool isHappy(int n){
   
   int m =sum(n);
   while(m!=1 && m!=n)
   {
       n=sum(n);
       m=sum(sum(m));

   }
  return (m==1);
        
}


int sum(int n)
{int s=0,r;
    while(n!=0)
            {
               r=n%10;
               s=s+r*r;
               n=n/10;

            }
return s;
}