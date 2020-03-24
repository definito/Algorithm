///exeption handling restrict rethrow terminate unexpected

#include<iostream>
using namespace std;
void excep()
{

        throw 1;

   // catch(int a){
   //  cout<<"Function: "<<a<<endl;
    // throw ;
   // }
}
void T(){
cout<<"Terminate"<<endl;

}
void U(){
cout<<"Unexpected"<<endl;

}
int main()
{   set_terminate(T);
    set_unexpected(U);
    try{
       excep();
    }
    catch(double  a )
    {
        cout<<"Main: "<<a<<endl;
    }
    return 0;
}
