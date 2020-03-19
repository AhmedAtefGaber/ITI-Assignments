#include <stdio.h>
#include <conio.h>

int main()
{
int num[5],max,min;
clrscr();
printf("enter the the  num1\n ");
scanf("%d",&num[1]);
printf("enter the num 2\n ");
scanf("%d",&num[2]);
printf("enter the num 3\n ");
scanf("%d",&num[3]);
printf("enter the  num 4\n ");
scanf("%d",&num[4]);
printf("enter the num 5\n ");
scanf("%d",&num[5]);
clrscr();


if (num[1] > num[2])

{ max = num[1];}
else {
  max = num[2];
    }

  if ( num[3] > max  )

   { max = num[3];
   }
    if (num[4] > max)

     { max =num[4];


     }
    if(num[5]>max)

     { max = num[5];

      }




if (num[1] <  num[2])
{
  min=num[1];
}

else {

  min = num[2];}

  if ( num[3] < min  )

   { min =num[3];

   }
    if (num[4] < min)

     { min =num[4];


     }

     if (num[5] < min)

     { min = num[5];}









 printf("the max is %d \n",max);
 printf("the min is %d",min);

getch();




return 0;
}