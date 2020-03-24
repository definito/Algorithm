#include <stdio.h>
#include <math.h>

int main()
{
int number_entered, x, y,x1,y1;

printf("Please enter a number.\n");
scanf("%d", &number_entered);
x = y = 5 * number_entered*number_entered + 4;        /*Test if 5N^2 + 4 is a square number.*/
x = sqrt(x);
x = x*x;
x1 = y1 = 5 * number_entered*number_entered - 4;        /*Test if 5N^2 - 4 is a square number.*/
x1 = sqrt(x1);
x1 = x1*x1;
if (x == y||x1==y1){
        printf("That number is in the Fibonacci sequence.\n");
    }

else
{
    printf("That number isn't in the Fibonacci sequence.\n");
}
return 0;
}
