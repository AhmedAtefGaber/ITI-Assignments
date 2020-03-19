#include <stdio.h>
#include <conio.h>
#include<alloc.h>
struct Student
{
char name[5];
int id;
int grades[3];
};

struct Student FillStud(void);
void PrintStud(struct Student * s);


int main()
{
struct Student s;
int i;
int n;
struct Student *p;
p = (struct Student *)malloc(n*sizeof(struct Student));
clrscr();
printf("enter the number of Students: ");
scanf("%d",&n);
//s = FillStud();
//PrintStud(s);

for(i=0;i<n;i++)
	{p[i]=FillStud();}
for(i=0;i<n;i++)
	{PrintStud(p+i);}

getch();
return 0;
}

struct Student FillStud(void)
{

struct Student s;
int i;

printf("Enter the name: ");
scanf("%s",s.name);
printf("Enter the ID: ");
scanf("%d",&s.id);

for(i=0;i<3;i++)
	{
	 printf("enter the grade of subject %d .\n",i+1);
	 scanf("%d",&s.grades[i]);
	}

return s;
}

void PrintStud(struct Student * s)
{
int i;
printf("name: %s\n",s->name);
printf("ID: %d\n",s->id);
for (i=0;i<3;i++)
	{
	 printf("grade of subject %d : %d\n",i+1,s->grades[i]);

	}

}
