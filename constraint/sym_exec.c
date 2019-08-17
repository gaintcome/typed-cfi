#include <stdio.h>

int j;
int i =12;
void f4()
{
	printf("This is f4\n");
}
void f3()
{
	printf("This is f3\n");
	if (j==1000)
		f4();
}
void f2()
{
	printf("This is f2\n");
	f3();
}
void f1()
{
	if(i==13)
		f2();
	else
		f3();
}
int main()
{
	f1();
}
