#include <stdio.h>
#include <conio.h>

int main()
{
int i,j,std[3][4],sum_grad[3]={0};
float avg_sub[4]={0};

clrscr();

for(i=0;i<3;i++)//students
  {
   for(j=0;j<4;j++) //subjects
      {
      printf("enter the grade of subject %d fot student %d \n ",j+1,i+1);
      scanf("%d",&std[i][j]);
      }
  }

for(i=0;i<3;i++)
{
   for(j=0;j<4;j++)
   {
     sum_grad[i]=sum_grad[i]+std[i][j];

   }
   printf("sum of grades for student %d is %d \n",i+1,sum_grad[i]);
}


for(j=0;j<4;j++)
{
  for(i=0;i<3;i++)
   {
    avg_sub[j]=avg_sub[j]+std[i][j];

   }
   avg_sub[j]=avg_sub[j]/3;
   printf("the average of subject %d is %f \n",j+1,avg_sub[j]);
}




getch();
return 0;
}