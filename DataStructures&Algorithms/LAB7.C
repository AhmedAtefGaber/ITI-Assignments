#include <stdio.h>
#include <conio.h>

int main()
{

char ch = 1;
int y=1;
clrscr();
printf("File\nEdite\nDisplay\nNew\nExit");
gotoxy(1,1);


while(ch!=27)
{
   ch=getch();

   if(ch==13)
   {
     if(y==1)
       {gotoxy(10,10);
       printf("File is pressed");
       }
     if(y==2)
       {gotoxy(10,10);
       printf("Edit is pressed");
       }
     if(y==3)
       {gotoxy(10,10);
       printf("Display is pressed");
       }
     if(y==4)
       {gotoxy(10,10);
       printf("New is pressed");
       }
     if(y==5)
       {
	return 0;
       }
   }

   if(ch == 0) //Extended
   {
	ch=getch();
	if(ch==80)//down
	{
	y=y+1;
	if(y>5)
	{y=1;}
	gotoxy(1,y);
	}

	if(ch==72)//up
	{y=y-1;
	if(y<1)
	{y=5;}
	gotoxy(1,y);
	}

	if(ch==71)//home
	{
	y = 1;
	gotoxy(1,y);
	}
	if(ch==79)//end
	{
	y = 5;
	gotoxy(1,y);
	}
	if(ch==27)
	{return 0;}


   }
   

}

if(ch==27)
{return 0;}

getch();
return 0;
}