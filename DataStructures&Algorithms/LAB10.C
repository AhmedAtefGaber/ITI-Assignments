#include <stdio.h>
#include <conio.h>
#include <ctype.h>


int main()
{
 char str[20]={0},ch=1;
 int pos=1,len=1;

clrscr();


while(ch!=27)
{
 ch=getch();
 if(isprint(ch))
       {
       if(len<=19)
	 {
	 str[len-1]=ch;
	 pos=pos+1;
	 len=len+1;
	 gotoxy(len,1);
	 printf("%c", ch);
	 }
        }

 if(ch==0)//extended
    {
	ch=getch();
	if(ch==71)//home
	{
	pos = 1;
	gotoxy(pos,1);
	}
	if(ch==79)//end
	{
	pos = len;
	gotoxy(pos,1);
	}
	if(ch==77)//right
	{
	pos = pos+1;
	gotoxy(pos,1);
	}
	if(ch==75)//left
	{
	 pos = pos-1;
	 gotoxy(pos,1);
	}

	if(ch==27)
	  {
           str[0]=0;
	   return 0;
	  }

    }

 if(ch==13)
   {
    gotoxy(5,5);
    printf("%s",str);
    }


}



// getch();

return 0;
}