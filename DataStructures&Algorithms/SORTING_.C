#include <stdio.h>
#include <conio.h>
#include<alloc.h>


struct Node{
		int data;
		struct Node * pPrev;
		struct Node * pNext;

		};

struct Node * pHead;
struct Node * pTail;


struct Node *  CreateNode( int d );
int AddNode( int d);
void Print(void);
int CountNode(void);
void Sort(void);


int main()
{
 int i,count,data;
 clrscr();
 printf("enter the number of elements you will add to the list: ");
 scanf("%d",&count);
 clrscr();
 for (i=0;i<count;i++)
	{
	 printf("\nEnter the data >> integer only << :  ");
	 scanf("%d",&data);
	 if( AddNode( data ) )
		{
		 printf("\n %d is add successfuly to the list. \n ",data);
		}
	 else
		{
		 printf("there is no space");
		}
	}

 clrscr();

 Print();
 Sort();
 printf("\n\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n");
 printf("\t\tafter Sorting\n\n");
 Print();
 getch();








 return 0;
}




struct Node * CreateNode( int d )
{
 struct Node * ptr ;
 ptr = (struct Node *)malloc(sizeof(struct Node));
 if (ptr)
	{
	 ptr -> data = d;
	 ptr -> pNext = ptr -> pPrev = NULL;

	}

 return ptr;
}



int AddNode( int d )
{
 int retval = 0;
 struct Node * ptr;
 ptr = CreateNode(d);
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


 return retval;
}




void Print(void)
{
 struct Node * ptr;
 int indx = 0;
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
		printf("index  %d  in the linked list has element  %d  .",indx,ptr -> data);
		indx ++ ;
		ptr = ptr -> pNext;
		}
	}
}

int CountNode(void)
{
 int len = 1;
 struct Node * ptr ;
 ptr = pHead;

 while ( ptr -> pNext ) // counting number of nodes in the list
	{
	 len ++;
	 ptr = ptr -> pNext;
	}


 return len;
}

void Sort(void)
{
int len = CountNode();
int i , j , temp ;
struct Node * ptr ;
for ( i=0 ; i<len-1 ; i++ )
	{
	 ptr = pHead ;
	 for ( j=0 ; j < len-i-1 ; j++ )
		{
		if ( ptr->pNext->data < ptr->data )
			{
			 temp = ptr->data;
			 ptr->data = ptr->pNext->data;
			 ptr->pNext->data = temp;
			}
		ptr = ptr -> pNext ;
		}
	}




}