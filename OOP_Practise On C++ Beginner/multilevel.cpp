#include<iostream>
using namespace std;

class Student{
//public:
    int id ;
   // int mark;
public:
    void getid(){cin>>id;cout<<id<<endl;};
    //void print(){cout<<mark<<"  "<<roll<<endl;}


};

class result:public Student{
int mark;
public:
    void getmark(){cin>>mark;cout<<mark<<endl;}


};


class view:private result{
public:
void print(){getid();getmark();}
};

int main()
{
    view ob;
    ob.print();

  // cout<<rol.mark<<"  "<<rol.roll<<endl;

 return 0;
}
