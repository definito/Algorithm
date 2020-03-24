#include <iostream>
#include<iomanip>
using namespace std;

class student{
     int id;
     string name;

   public:
      student(){};
      student(int i,string n){id=i;name=n;}
      friend ostream&  operator  << (ostream &os,student &s);
      friend istream&  operator  >> (istream &is,student &s);
     // friend void operator << (ostream &os, student ob)
     //{
     //   os<<ob.id<<" deb"<<ob.name<<endl;
    //  }

      ///void print(){cout<<id<<" "<<name<<endl;}
};

  ostream& operator << (ostream &os,student &s)
{
    os<<s.name<<" ";
    os<<s.id<<endl;
    return os; ///must return
}
  istream& operator >> (istream &is,student &s)
{
    cout<<"First name: ";
    is>>s.name;
    is>>s.id;
    return is; ///must return
}

int main()
{
    student first;
    student second;
    cin>>first;
    cin>>second;
    cout<<first;
    cout<<second;
    ///second.print();

return 0;
}
