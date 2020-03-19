#include <stdio.h>
#include <conio.h>
#include <string.h>
void delvow(char s[],char * res);
int main()
{
char s[]="ahmedooccncce";
char res[100];
delvow(s,res);
clrscr();
printf("%s",res);
printf("%d",strlen(res));
printf("%d",res[8]);

getch();
return 0;
}

void delvow(char s[],char * res)
{
int i,j=0;
int l =strlen(s);
char v[5]="aioue";

for (i=0;i<l;i++)
    {
     if(!( s[i]==v[0] || s[i]==v[1] || s[i]==v[2] || s[i]==v[3] ||s[i]==v[4]))
	{
	 res[j]=s[i];
	 j++;
	 }
    }
}
