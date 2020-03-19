#include <stdio.h>
#include <conio.h>

struct Student
	{
	 char name[10];
	 int id;
	 int grades;
	};

struct Student std[5];

struct Student FillStud(void);
void PrintStud(struct Student s);
void Merge_Sort(int low , int high);
void Merge(int low , int mid , int high );
int BinarySrch(int low , int high , int id );

int main()
{
 int i,id,loc;
 clrscr();

 for( i=0 ; i<5 ; i++ )
	{
	 std[i]=FillStud();
	}


 clrscr();
 Merge_Sort(0,4);

 for ( i=0 ; i<5 ; i++)
	{
	 printf("\n=============\n");
	 PrintStud(std[i]);
	 printf("\n=============\n");
	}
 printf("\n\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*\n\n");
 printf("Enter ID: ");
 scanf("%d",&id);
 loc=BinarySrch(0,4,id);
 if (loc == -1 )
	{
	 printf("ID %d not found.",id);
	}
 else
	{
	printf("id ==> %d found in location: %d \n",id,loc);
	PrintStud(std[loc]);
	}
 getch();






return 0;
}





struct Student FillStud(void)
{

struct Student s;

printf("Enter the name: ");
scanf("%s",s.name);
printf("Enter the ID: ");
scanf("%d",&s.id);
printf("enter the grade of subject \n");
scanf("%d",&s.grades);
return s;
}

void PrintStud(struct Student s)
{
int i;
printf("name: %s\n",s.name);
printf("ID: %d\n",s.id);
printf("grade of subject %d : %d\n",i+1,s.grades);
}


void Merge_Sort(int low , int high )
{
 int mid;
 if ( low < high )
	{
	 mid = ( low + high ) / 2 ;
	 Merge_Sort( low , mid );
	 Merge_Sort( mid + 1 , high );
	 Merge( low , mid , high );
	}
}

void Merge ( int low , int mid , int high )
{
 struct Student temp[10];
 int list1 = low;
 int list2 = mid + 1 ;
 int i = low ;
 while ( list1 <= mid && list2 <= high )
	{
	 if ( std[list1].id < std[list2].id )
		{
		 temp[i] = std[list1];
		 i ++;
		 list1 ++;
		}
	 else
		{
		 temp[i] = std[list2];
		 i++;
		 list2++;
		}
	}

 while ( list1 <= mid )
	{
	 temp[i] = std[list1];
	 list1 ++;
	 i++;
	}

 while ( list2 <= high)
	{
	 temp[i] = std[list2];
	 list2 ++;
	 i++;
	}
 for ( i=low ; i<=high ; i++ )
	{
	 std[i] = temp[i];
	}


}

int BinarySrch(int low , int high , int id )
{
 int loc = -1 , mid ;
 if ( low <= high )
	{
	 mid = ( low + high ) / 2 ;
	 if ( std[mid].id == id )
		{
		 loc = mid ;
		}
	 else
		{
		 if (std[mid].id > id)
			{
			 loc = BinarySrch( low , mid - 1 , id );
			}
		 else
			{
			 loc = BinarySrch (  mid + 1 , high , id );
			}
		}
	}
return loc;
}










