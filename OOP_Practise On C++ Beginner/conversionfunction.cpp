#include <iostream>

using namespace std;
class abc{
public:
   mutable int x;
    int y;
    abc (){x=4;}
    abc(int a,int b){x=a;y=b;}
    operator int (){return x+y;}
    void change(int a)const {x=a;}
};

class member{
public:
    int x;
    int y;
    //member(){};
   void  set(int a,int b){x=a;y=b;}


};

int main(){
      abc ob(1,2);

      int a =ob;
      cout<<a<<" "<<endl;
      ob.change(12);
      cout<<ob.x<<" "<<endl;
      member mo;
      mo.set(1,2);
      cout<<mo.x<<" "<<mo.y<<endl;
  return 0;
}
