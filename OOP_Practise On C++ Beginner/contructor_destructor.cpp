///constructor ,destructor
#include<iostream>
using namespace std;
class rectangle{
private:
	int height;      ///encapsulation
	int  width;
public:
	int area();
	float sump(float hi ,float wi);
    rectangle(int hi,int wi );
    ~rectangle();
};

int rectangle::area()  //
{
     return height*width;
};
rectangle::rectangle(int hi , int wi)
{

    height =hi ;
    width  = wi;

    cout<<"Constructor"<<area()<<"\n";

};
 rectangle::~rectangle()
{

    cout<<"Destructor"<<area()<<"\n";


};

int main()
{
    rectangle obj(5,6),obj1(1,2);

   //cout<<"Area:"<<obj.area(hi,wi)<<"\nThe sum is:"<<obj.sump(hi,wi)<<endl;
	return 0;
}
