#include <iostream>
using namespace std;
class Number{
int x,y;
public:
    Number();
    Number(int a, int b);
    void refer(int& a,int& b);
    void setN(int a, int b);
    Number operator +(Number ob);
    void print();
    Number(int a){x=a;y=0;}
};
Number Number::operator + (Number ob)
{
    Number tmp;
    tmp.x= this->x+ob.x;
    tmp.y= this->y+ob.y;

    return tmp;
}
void Number::print()
{
    cout<<x<<" "<<y<<endl;
}

Number::Number()
{
    x=0;
    y=0;
}
Number::Number(int a,int b)
{
    x=a;
    y=b;
}
void Number::refer(int& a, int&b)
{
  a=x;
  b=y;
}
void Number::setN(int a,int b)
{
   x=a;
   y=b;

}
class Number1{
int x,y;
public:
     Number1();
    Number1(int a){x=a;};
    operator Number()
    {   Number tmp(x);
        return tmp;
    }
};

int main()
{
   Number n1,n2,n3;
   n1.setN(2,3);
   n2.setN(4,5);
   n3=n1+n2;
   n3.print();
   int a=5;
   n1=a;
   n1.print();

   ///class-> class

   Number1 x1(5);
   n1=x1;
   n1.print();
   return 0;

}
