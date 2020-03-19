#include <stdio.h>
#include <stdlib.h>
#include <conio.h>
struct Student{
		int id;
		char name[10];
		int grades;
		};

struct Node{
	     struct Node * pNext;
	     struct Student std;

		};

struct Node * pHead;
struct Student FillStud(void);
void PrintStud(struct Student s);
struct Node * CreateNod(struct Student s);
int Push_Stack(struct Student std);
struct Node * Pop_Stack(void);

int main()
{
 int f;
 struct Node * ptr;
 clrscr();
 do
 {printf("1-push.\n2-pop.\n3-Exit.");
  scanf("%d",&f);
  if (f == 1)
	{
	 if (Push_Stack(FillStud()))
		{
		 printf("student is add to the stack\n");
		}
	 else
		{
		printf("Stack over flow");
		}
	}
  if (f ==2)
	{
	 ptr = Pop_Stack();
	 if (ptr)
		{
		 PrintStud(ptr -> std);
		}
	 else
		{
                printf("not Existed");
		}
	}

 }while( f != 3);


return 0;
}

struct Student FillStud(void)
{

struct Student s;

printf("Enter the name: ");
scanf("%s",s.name);
printf("Enter the ID: ");
scanf("%d",&s.id);
printf("enter the grade of subject .\n");
scanf("%d",&s.grades);

return s;
}

void PrintStud(struct Student s)
{

printf("name: %s\n",s.name);
printf("ID: %d\n",s.id);
printf("grade of subject %d .\n",s.grades);

}

struct Node * CreateNode(struct Student s)
{
 struct Node * ptr ;
 ptr = (struct Node *)malloc(sizeof(struct Node));
 if (ptr)
	{
	 ptr -> std = s;
	 ptr -> pNext = NULL;

	}

 return ptr;
}

int Push_Stack(struct Student std)
{
 int retval = 0;
 struct Node * ptr;
 ptr = CreateNode(std);
 if(ptr)
	{
	 if(pHead == NULL)//there is no nodes yet
		{
		 pHead = ptr;
		 pHead -> pNext = NULL;
		}
	 else             // there is at least one node
		{
		 ptr -> pNext = pHead;
		 pHead = ptr;
		}
	 retval = 1;
	}
 return retval;
}

struct Node * Pop_Stack(void)
{
 struct Node * ptr ;
 ptr = pHead ;
 if (ptr)   //there is a stack
	{
	 if (ptr -> pNext ) //more than one node
		{
		 pHead = pHead -> pNext;
		}
	 else //there is one node
		{
		 pHead = NULL;
		}
	}
 return ptr;
}












