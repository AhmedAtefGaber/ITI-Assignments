#include <stdio.h>
#include <conio.h>

int main ()
{
int num[5],max,min,i;
clrscr();

for(i=0;i<5;i++)
{
printf("enter the the  num %d \n ",i+1);
scanf("%d",&num[i]);
}
clrscr();

max=min=num[0];


for(i=1;i<=4;i++)
{
  if(num[i]>max)
   {max=num[i];}

  if(num[i]<min)
   {min=num[i];}

}

printf("the man is %d \n",max);
printf("the min is %d \n",min);


getch();
return 0;
}