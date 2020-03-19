#include <stdio.h>
#include <conio.h>
#include <string.h>
void countvowles(char * s,char * v,int * c,int l);
int main()
{char str[]="aaahmeeedoeiu";
int count[5]={0};
char vowels[5]="aieou";
int l = strlen(str);
clrscr();
countvowles(str,vowels,count,l);
printf("\n%d:a  %d:i %d:e %d:o %d:o",count[0],count[1],count[2],count[3],count[4]);
getch();
return 0;
}
void countvowles(char * s,char * v,int * c,int l)
{
int i;

for(i=0;i<l;i++)
    {
if (s[i]== v[0])
   { *(c) +=1;  }

if (s[i]==v[1])
    *(c+1) +=1;
	if (s[i]==v[2])
    *(c+2) +=1;
	if (s[i]==v[3])
    *(c+3) +=1;
	if (s[i]==v[4])
    *(c+4) +=1;
    }
 }