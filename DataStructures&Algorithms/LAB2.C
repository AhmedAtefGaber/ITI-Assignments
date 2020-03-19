#include <stdio.h>
#include <conio.h>



int main ()

{
int x,y;

clrscr();

printf("\nwelcoom\nenter the first number\n");
scanf("%d", &x);
printf("enter the second number:\n");
scanf("%d",&y);
printf ("the sum of %d and %d is equal to %d",x,y,x+y);

getch();
return 0;
}