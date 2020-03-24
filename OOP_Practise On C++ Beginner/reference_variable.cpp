#include<iostream>
using namespace std;

int& test(int a)
{
    return a;
}

int main()
{
    int i;
    i=5;
    int *p;
    p= &i;
    cout<<*p<<endl;
    int& r=i;
    cout<<r;
    int a=1;
    test(a);
    cout<<"\n"<<test(a);
    return 0;

}
