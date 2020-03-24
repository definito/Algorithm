#include<iostream>
using namespace std;

class Student{
//public:
    int id ;
    int mark;
   // int mark;
public:
    void getid(){cin>>id;cout<<id<<endl;};
    void getmark(){cin>>mark;cout<<mark<<endl;};
    //void print(){cout<<mark<<"  "<<roll<<endl;}
};

class result:private Student{
public:
    void print(){getmark();}
};




class view:private Student{
public:
void print(){getid();}
};

int main()
{
    view ob;
    result rob;
    ob.print();
    rob.print();


  // cout<<rol.mark<<"  "<<rol.roll<<endl;

 return 0;
}
