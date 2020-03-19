#include <stdio.h>
#include <conio.h>
#include<alloc.h>
struct Student
{
		char name[15];
		int id;
		int grades;
};

struct Node{
		struct Student student;
		struct Node * pPrev;
		struct Node * pNext;

		};

struct Node * pHead;
struct Node * pTail;

struct Student FillStud(void);
void PrintStud(struct Student s);


struct Node *  CreateNode(struct Student s);
int AddNode(struct Student s);
int InsertNode(int loc, struct Student s);
struct Node * SearchNode(int ID);
void FreeList(void);
int DeleteNode(int loc);
void Print(void);

int main()
{
int f;
int id,loc;
int delnode;
struct Node * std;
clrscr();
do{printf("\n\n1-Add Node: \n2-Insert Node: \n3-Search Node: \n4-Print Node: \n5-Delete: \n6-Free List: \n7-Exit: ");
   scanf("%d",&f);
   clrscr();
   if (f == 1 ) // add
	{
	if ( AddNode( FillStud() ) )

		{
		 printf("the Student is added");
		}
	}

  if ( f== 2 )  //insert
	{
	 printf("Enter the location you want to insert to: ");
	 scanf("%d",&loc);
	 if ( InsertNode(loc, FillStud()))
		{
		printf("the student is inserted.");
		}
	}
  if (f == 3)
	{
	 printf("enter the id: ");
	 scanf("%d",&id);
	 std = SearchNode(id);
	 if (std)
		{
		 printf("name: %s.\n",(std->student).name);
		 printf("the grade: %d\n",(std->student).grades);
		}
	 else
	 {printf("there is no student wit the ID = %d.\n",id);}
	}
  if ( f == 4 )
	{
	 Print();
	}

  if ( f == 5 )
	{
	 printf("enter the location of you want to delete: ");
	 scanf("%d",&loc);
	 if (DeleteNode(loc))
		{
		 printf("node %d is deleted.\n",loc);
		}
	 else
		{
		printf("there is no node %d.\n",loc);
		}

	}


  if (f == 6 )
	{
	 FreeList();
	}
  }while(f != 7);



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
	 ptr -> student = s;
	 ptr -> pNext = ptr -> pPrev = NULL;

	}

 return ptr;
}



int AddNode(struct Student s)
{
 int retval = 0;
 struct Node * ptr;
 ptr = CreateNode(s);
 if (ptr)
	{

	 if (pHead == NULL)
		{
		 pHead = pTail = ptr;

		}
	 else
		{
		 pTail -> pNext = ptr;
		 ptr -> pPrev = pTail;
		 pTail = ptr;
		}
	retval = 1;
	 }
	  PrintStud(s);

 return retval;
}


int InsertNode(int loc, struct Student s)

{
int retval = 0;
int i;
struct Node * ptr ;
struct Node  * temp;
ptr = CreateNode(s);
if (ptr)
	{
	 if (loc == 0) //insert at first
		{
		 if (pHead == NULL)  //there is no nodes
			{
			 pHead = pTail =ptr;
			}
		 else //there is at least on node in the list
			{
			 pHead -> pPrev = ptr;
			 ptr -> pNext = pHead;
			 pHead = ptr;
			}
		 }
	 else

		{
		 temp = pHead;
		 for (i=0;i<loc-1&&temp; i++)
			{
			 temp = temp -> pNext;
			}
		 if (temp == pTail || temp == NULL)
			{
			 pTail -> pNext = ptr;
			 ptr -> pPrev =pTail;
			 pTail = ptr;
			}
		 else
			{
			 temp -> pNext -> pPrev = ptr;
			 ptr -> pNext = temp -> pNext;
			 ptr -> pPrev = temp;
			 temp -> pNext = ptr;
			}

		}
	}

	retval = 1;
	PrintStud(s);

 return retval;
}


struct Node * SearchNode(int ID)
{
 struct Node * ptr;
 ptr = pHead;
 while ( (ptr -> student).id != ID && ptr )
	{
	 ptr = ptr -> pNext ;

	}


 return ptr;
}

void FreeList(void)
{
struct Node * ptr;
ptr=pHead;
while(pHead)
	{
	pHead = ptr -> pNext;
	free(ptr);
	ptr = pHead;
	}
pTail = NULL;
}

int DeleteNode(int loc)
{
 int retval = 0,i;
 struct Node * ptr ;
 ptr = pHead;

 if ( ptr )//there is a list
	{
	 if ( loc ==0 )
		{
		 if ( pHead ==  pTail )
			{
			 pHead = pTail = NULL;
			 free(ptr);
			}
		 else
			{
			 pHead = pHead -> pNext;
			 pHead -> pPrev = NULL;
			 free(ptr);
			}
		 retval = 1;
		}
	 else
		{
		 for(i=0;i<loc&&ptr;i++)
			{
			ptr = ptr -> pNext;
			}
		 if ( ptr ) //location to delete is less than num of nodes
			{
			 if ( ptr == pTail ) //deleting the last node
				{
				 pTail = ptr -> pPrev;
				 pTail -> pNext = NULL;
				}
			 else
				{
				 ptr -> pNext -> pPrev = ptr -> pPrev;
				 ptr -> pPrev -> pNext = ptr -> pNext;

				}
			 free(ptr);
			 retval = 1;
			}

		}
	}
 return retval;
}
void Print(void)
{
 struct Node * ptr;
 ptr = pHead;
 if(!pHead)//there is no list
	{
	 printf("there is no list to print");
	}
 else
	{
 	while(ptr)
		{
                printf("\n\t===============\n");
		PrintStud(ptr -> student);
		 ptr = ptr -> pNext;
		}
	}
}


