#include <stdio.h>
#include <conio.h>
#include <math.h>

int main()
{
int a,b,c;
float sol1,sol2,solr,soli;

clrscr();
printf("enter a \n ");
scanf("%d",&a);
printf("enter b \n ");
scanf("%d",&b);
printf("enter c \n ");
scanf("%d",&c);
if (( b*b -4*a*c ) > 0)
{ sol1= (-b + sqrt(b*b-4*a*c )) / (2*a);
 sol2= (-b - sqrt(b*b-4*a*c )) / (2*a);

printf ("the first root is %f and the second root is %f \n",sol1,sol2);
getch();
}
else if (( b*b -4*a*c ) ==  0)
{ sol1= (-b  / (2.0*a));
printf("both the roots are the same and equal to %f\n ",sol1);
getch(); }

else //if (( b*b -4*a*c ) < 0)
{solr = -b/(2.0*a);
 soli = ( sqrt(-(b*b-4*a*c ))) / (2.0*a);
 printf(" the first root is %f + %f i\n ",solr,soli);
 printf(" the second root is %f - %f i\n ",solr,soli);
 getch();
	 }




return 0 ;
}