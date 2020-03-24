#include<iostream>
using namespace std;
class rectangle{
private:
	float height;      ///encapsulation
	float width;
public:
	int area();
	float sump(float hi ,float wi);

};

int rectangle::area()  //
{
    return height*width        ;            ///prototype declaration
};
inline float rectangle::sump(float height,float width)
{

   this-> height =height ;
   this-> width  = width;
   cout<<this->height<<"\n\n";
                  ///Inline used for better timing
};
rectangle scan(){
 float height,width;
 cin>>height>>width;
 rectangle ob;
 ob.sump(height,width);
 return ob;
}

void print(rectangle ab){
 cout<<ab.area()<<endl;

};
int main()
{

    rectangle obj;
    cout<<"Type height and width:";

    obj=scan();
     print(obj);

   // cout<<"Area:"<<obj.area(hi,wi)<<"\nThe sum is:"<<obj.sump(hi,wi)<<endl;
	return 0;
}
