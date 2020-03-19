#include <stdio.h>
#include <conio.h>

int main()
{
int num1,num2,num3,num4,num5,max,min;
clrscr();
printf("enter the the  num1\n ");
scanf("%d",&num1);
printf("enter the num 2\n ");
scanf("%d",&num2);
printf("enter the num 3\n ");
scanf("%d",&num3);
printf("enter the  num 4\n ");
scanf("%d",&num4);
printf("enter the num 5\n ");
scanf("%d",&num5);
clrscr();


if (num1 > num2)

{ max = num1;}
else {
  max = num2;
    }

  if ( num3 > max  )

   { max = num3;
   }
    if (num4 > max)

     { max =num4;


     }
    if(num5>max)

     { max = num5;

      }

     


if (num1 <  num2)
{
  min=num1;
}

else {

  min = num2;}

  if ( num3 < min  )

   { min =num3;

   }
    if (num4 < min)

     { min =num4;


     }

     if (num5 < min)

     { min = num5;}









 printf("the max is %d \n",max);
 printf("the min is %d",min);

getch();




return 0;
}