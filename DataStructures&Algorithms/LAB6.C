#include <stdio.h>
#include <conio.h>

int main()
{
int size,count,row,col;
clrscr();

printf("please enter a number  ");
scanf("%d",&size);
clrscr();
for(count=1;count <= size*size ;count++)
{
 if(count==1)
 {
 row=1;
 col=(size+1)/2;
 }

 else
 {
 if ((count-1)%size ==0)
 {
 row++;
 if (row>size)
 {
 row=1;
 }

 }
 else
 {
 row--;
 col--;
 if(row==0)
 {row=size;}
 if(col==0)
 {col=size;}
 }


  }


gotoxy(col*4,row*2);
printf("%d",count);

}




getch();
return 0;
}