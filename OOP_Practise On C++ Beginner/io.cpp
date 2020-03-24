#include<iostream>
using namespace std;

int main()
{
   ios::fmtflags f;
   f= ios::showpos | ios:: showpoint;
   cout.flags(f);
   cout<<100.1<<endl;
   cout.width(20);
   cout.fill('.');
   cout.setf(ios::left|ios::adjustfield);
   cout<<"debwashis";
   cout<<"------"<<endl;
   cout.unsetf(ios::left|ios::adjustfield|ios::showpos | ios:: showpoint);
   bool a;
   cout.setf(ios::boolalpha);
   cin>>a;
   cout<<a;

 return 0;
}
