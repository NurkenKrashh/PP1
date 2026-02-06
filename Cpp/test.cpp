#include <iostream>
#include <string>
using namespace std;
int main(){
int a;
cin>>a;

char hex;
if(a<10){
    hex=a+'0';
    
}
else{
    hex=(a-10) +'A';
}
cout<<hex;
}