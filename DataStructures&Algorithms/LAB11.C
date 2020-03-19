#include <stdio.h>
#include <conio.h>

int main()
{
int ar[5],i,sum=0;
int* ptr;
ptr=ar;
clrscr();


for(i=0;i<5;i++)
{
 printf("please enter the number %d ",i+1);
 scanf("%d",ptr+i);
 sum=sum+ptr[i];
}
clrscr();

for(i=0;i<5;i++)
{
 printf("\n       number %d = %d \n   ",i+1 , *(ptr+i));
}

printf("\n \n  the sum of numbers =  %d",sum);


getch();

return 0;
}