#include<iostream>
using namespace std;

class base1{
public:
    int a;
    base1(int x){a=x;}
};
class base2{
public:
    int c;
    base2(int z){c=z;}
};

class derive: public base1,public base2{
public :
        int b;
        derive(int x,int y,int z):base1(0),base2(0){
        a=x;
        b=y;
        c=z;}

};

int main()
{
    derive ob(5,6,7);
    cout<<ob.a<<endl;
    cout<<ob.b<<endl;
    cout<<ob.c<<endl;
  // cout<<rol.mark<<"  "<<rol.roll<<endl;

 return 0;
}
