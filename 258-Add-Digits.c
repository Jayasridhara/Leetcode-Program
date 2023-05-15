int addDigits(int num){
 
int  s=0;
int r;
if(num==0)
return s;
else
{
   do{
while(num!=0)
{
      r=(int)num %10;
      s=(unsigned int)s+r;
  num/=10;
}
     num=s;  
       
 }while(num>=9);
}

        return (int)num;

}