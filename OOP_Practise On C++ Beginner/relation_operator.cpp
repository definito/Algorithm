///relational operator overload
#include <iostream>
using namespace std;
class Number{
int x,y;
public:
    Number();
    Number(int a, int b);
    Number(int a);
    void refer(int& a,int& b);
    void setN(int a, int b);
    Number operator +(Number ob);
    bool   operator >(Number ob);
    void print();
    Number operator ++();
    friend void operator << (ostream &out, Number ob)
    {
        out<<ob.x<<" "<<ob.y<<endl;
    }

};
class Number1{
int x,y;
public:
    Number1();
    Number1(int a, int b);
    void refer(int& a,int& b);
    void setN(int a, int b);
    Number operator +(Number1 ob);
    bool   operator >(Number1 ob);
    void print();
    Number1 operator ++();
    friend void operator << (ostream &out, Number1 ob)
    {
        out<<ob.x<<" "<<ob.y<<endl;
    }

};




Number Number::operator + (Number ob)
{
    Number tmp;
    tmp.x= this->x+ob.x;
    tmp.y= this->y+ob.y;

    return tmp;
}
bool Number::operator > (Number ob )
{
    return (x+y) > (ob.x+ob.y) ;
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
Number::Number(int a)
{
    x=a;
    y=0;
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
Number Number::operator++()
{
    Number tmp;
    x++;y++;
    tmp.x=x+1;
    tmp.y=y+1;
    return tmp;
}

int main()
{
   Number n1,n2,n3;
   n1.setN(2,11);
   n2.setN(4,5);
   n3=n1+n2;
   n3.print();
   n1.print();
    if(n1>n2)
   {
       cout<<"n1"<<endl;
   }
   else{
        cout<<"n2"<<endl;
   }


  ++n1;
  n1.print();

  cout<<n1;
   return 0;

   int a=5 ;
   n1=a;
   cout<<n1<<endl;
}
