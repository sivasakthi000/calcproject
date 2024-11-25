#include <iostream>
int sum(int a,int b){
    return a+b;
}
using namespace std;
int main(){
    int a,b,c;
    cin>>a>>b;
    c=sum(a,b);
    cout<<c;
    return 0;

}