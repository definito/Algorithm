#include<iostream>
#include<fstream>
#include<windows.h>
using namespace std;

int main()
{
    ifstream in;
    in.open("pdf.pdf");
    if(!in) cout<<"Can't open file";
    else {
        char str[100];
        in>>str;
        cout<<str;
        in.close();
    }


   return 0;
}
