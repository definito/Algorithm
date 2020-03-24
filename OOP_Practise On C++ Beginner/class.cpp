#include<iostream>
using namespace std;
class rectangle{
private:
	float height;      ///encapsulation
	float width;
public:
	int area(int a,int b);
	float sump(float hi ,float wi);

};

int rectangle::area(int a, int b)  //
{
     int c;
     c=a*b;
     return c;                    ///prototype declaration
	};
inline float rectangle::sump(float hi, float wi)
{
    float d;
    height =hi ;
    width  = wi;
    d=height+width;
    return d ;        ///Inline used for better timing
};


int main()
{
    float hi,wi;
    rectangle obj;
    cout<<"Type height and width:";
    cin>>hi>>wi;



    cout<<"Area:"<<obj.area(hi,wi)<<"\nThe sum is:"<<obj.sump(hi,wi)<<endl;
	return 0;
}
