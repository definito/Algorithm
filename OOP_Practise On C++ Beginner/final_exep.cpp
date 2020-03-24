///final exception Handling
#include<iostream>
#include<stdio.h>
using namespace std;
void divide(double numerator  ,double denumerator)
 {
     try{
         if(denumerator==0)  throw 0;
        cout<<"Result: "<<numerator/denumerator<<endl;
     }
     catch(int e){
         cout<<"Can't divide something 0"<<endl ;
     }
 }
int main()
{
    double num ,dnum;

      do {
          cout<<endl;
          cout<<"Enter a number(O to stop)"<<endl;
          cin>>num;
          cout<<"Enter denumerator"<<endl;
          cin>>dnum;
          divide(num,dnum);
      }while(num) ;
}
