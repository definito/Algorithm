#include <iostream>

using namespace std;

int add(int a ,int b)
{
    return a+b;
}


int add(int a ,int b,int c)
{
    return a+b+c;
}

double add(double a ,double b)
{
    return a+b;
}

int main()
{
    cout << add(3,4) <<"\n"<<add(5,6)<< endl;
    return 0;
}
