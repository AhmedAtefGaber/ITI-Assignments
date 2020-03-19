#include <stdio.h>
#include <conio.h>


int main()
{
int num,max,min,count;
clrscr();
printf("enter a number\n ");
scanf("%d",&num);
max=min=num;
for(count=1;count< 5;count++)
{
clrscr();
printf("enter a number\n ");
scanf("%d",&num);
if( num > max)
{max=num;}

if(num < min)
{min=num;}

 }


 printf("the max is %d \n",max);
 printf("the min is %d",min);

getch();




return 0;
}