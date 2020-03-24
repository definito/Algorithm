#include<iostream>
using namespace std;
class rectangle{
private:
	float height;      ///encapsulation
	float width;
public:
	int area();
	float change(float hi ,float wi);

};

int rectangle::area()  //
{
     return height*width;                    ///prototype declaration
	};
inline float rectangle::change(float hi, float wi)
{
    height =hi ;
    width  = wi;
}

int main()
{
   rectangle obj[5];
   //obj[0].change(8,3);
   //cout<<obj[0].area();
   for(int i=0;i<5;i++)
    {
    obj[i].change(i,i+1);
    cout<<i<<" " " "<<obj[i].area()<<"\n";

   };


	return 0;
}

