#include<iostream>
using namespace std;
class rectangle{
private:
	float height;      ///encapsulation
	float width;
public:
	int area();
	float change(float hi ,float wi);
    rectangle(float hi);
};

int rectangle::area()  //
{
     return height*width;                    ///prototype declaration
	};
 rectangle::rectangle(float hi)
{
    height =hi ;
    width  = hi;
};

int main()
{
    rectangle obj[5]={1,2,3,4,5};
   //obj[0].change(8,3);
   //cout<<obj[0].area();
   for(int i=0;i<5;i++)
    {
    cout<<i<<"="<<obj[i].area()<<"\n";

   };


	return 0;
}

