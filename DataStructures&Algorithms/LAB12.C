#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

int main()
{
int i,sum=0,s;
int* ptr;
clrscr();
printf("how many numbers do you need:\n");
scanf("%d",&s);
ptr=(int*)malloc(sizeof(int)*s);
clrscr();

if(ptr)
{

 for(i=0;i<s;i++)
  {
   printf("please enter the number %d ",i+1);
   scanf("%d",ptr+i);
   sum=sum+ptr[i];
  }

clrscr();

 for(i=0;i<s;i++)
  {
    printf("\n       number %d = %d \n   ",i+1 , *(ptr+i));
  }
 free(ptr);
}

printf("\n \n  the sum of numbers =  %d",sum);


getch();

return 0;
}