#include <stdio.h>
#include <conio.h>
int cstr(char a[],char b[]);
int main()
{
 char str1[]="ahmez";
 char str2[]="ahmed";
 clrscr();

 if (cstr(str1,str2) == 1)
 printf("s1 > s2");
 if (cstr(str1,str2) == -1)
 printf("s1 < s2");
 if (cstr(str1,str2) == 0)
 printf("s1 = s2");

    getch();
    return 0;
}

int cstr(char a[],char b[])
{
 int i=0;
 while (a[i] )
 {
  if (a[i] > b[i])
  { return 1;
   }

  if (a[i] < b[i])
  { return -1;
  }

  /*if (a[i] = b[i])
  { return 1;
   }*/
   else
   i++;
 }


 return 1;
}