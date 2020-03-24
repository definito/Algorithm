#include<iostream>
using namespace std;

class Student{
//public:
    int id;
   // int mark;
public:
      int getid(){cout<<"Enter Student ID:";cin>>id;return id;};

    //void print(){cout<<mark<<"  "<<roll<<endl;}
};

class lab{
      int mark;
  public:
    int getmark(){cout<<"Enter LAB Mark:";cin>>mark;return mark;}

};

class exam: public lab{
     int emark;
   public:
       int getemark(){cout<<"Enter Mark:";cin>>emark;return getmark()+emark;}
;
};
class result: private Student, private exam{
  public:
      int  getResult(){
         int sid = getid();
         int res = getemark();
         cout<<"ID-> "<<sid<<"\n"<<"Result -> "<<res<<endl;
      }


};
int main()
{
    result ob;
    ob.getResult();
  // cout<<rol.mark<<"  "<<rol.roll<<endl;

 return 0;
}
