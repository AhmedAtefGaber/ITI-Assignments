#include <stdio.h>
#include <conio.h>
int main()
{

int ch;
clrscr();
ch = getch();


if( ch )
  {
  printf("this key  %c  is a normal key with ascii code = %d ",ch,ch);
  }
else
  {
  ch=getch();
  printf("this is an extended key with code = %d ",ch);
  }

getch();
return 0;
}