#include <iostream>
#include<math.h>
using namespace std;

int main(int argc, char **argv){
    int n;
    cin >> n;
    int temp=n,nod=0;
    while(temp!=0){
        temp/=10;
        nod+=1;
    }
    int div = pow(10,nod-1);
    while(n!=0){
        int q=n/div;
        cout<<q<<endl;
        n=n%div;
        div/=10;
    }
    return 0;
}
