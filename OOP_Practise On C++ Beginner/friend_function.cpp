#include<iostream>
using namespace std;

class rectangle;

class cost{
int costRate;
public:
    void setValue(float a){costRate=a;}
     float totalCost(rectangle A);
};

class rectangle{
private:
	float height;      ///encapsulation
	float width;
public:
	int area();
	float sump(float hi ,float wi);
	friend float cost::totalCost(rectangle A);    ///friend class

};

int rectangle::area()  //
{
    return height*width        ;            ///prototype declaration
};
inline float rectangle::sump(float height,float width)
{

   this-> height =height ;
   this-> width  = width;
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
float cost::totalCost(rectangle A ){
  return costRate*A.height*A.width;
}

int main()
{

    rectangle obj;
    cout<<"Type height and width:";

    obj=scan();
    print(obj);
    cost r;
    r.setValue(5);
    cout<<r.totalCost(obj);

   // cout<<"Area:"<<obj.area(hi,wi)<<"\nThe sum is:"<<obj.sump(hi,wi)<<endl;
	return 0;
}
