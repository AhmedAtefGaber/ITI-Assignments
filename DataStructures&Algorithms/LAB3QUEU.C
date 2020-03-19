#include <stdio.h>
#include <conio.h>

int ar[10];
int pushf;
int add(int d);
int ret(void);

int main()
{
 int d;
 int f;
 clrscr();
 do
 {printf("\n\n1-add.\n2-retreive.\n3-Exit.\n\n");
  scanf("%d",&f);
  if (f == 1)
	{printf("enter a number: ");
	 scanf("%d",&d);
	 if (add(d))
		{
		 printf("%d add to the queue\n",d);
		}
	 else
		{
		printf("queue over flow");
		}
	}
  if (f ==2)
	{
	 d = ret();
	 if (d != -1)
		{
		 printf("%d is retreived\n",d);
		}
	 else
		{
		printf("not Existed\n");
		}
	}





 }while( f != 3);




 return 0;
}

int add(int d )
{
 int retval = 0;
 if ( pushf < 10)
	{
	 ar[pushf] = d;
	 pushf ++;
	 retval = 1;
	}
return retval ;
}

int ret(void)
{
 int i, retval = -1;
 if(pushf)
	{pushf --;
	 retval = ar[0];
	 for(i=0;i<pushf;i++)
		{
                 ar[i] = ar[i+1];
		}
	}
return retval;
}



