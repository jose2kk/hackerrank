#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a;
    int b;

    cin >> a;
    cin >> b;

    for (int n = a; n <= b; n++) {
        if (n > 0 && n < 10) {
            if (n < 2) {
                cout<<"one";
            } else if(n < 3){
                cout<<"two";
            } else if(n < 4){
                cout<<"three";
            } else if(n < 5){
                cout<<"four";
            } else if(n < 6){
                cout<<"five";
            } else if(n < 7){
                cout<<"six";
            } else if(n < 8){
                cout<<"seven";
            } else if(n < 9){
                cout<<"eight";
            } else {
                cout<<"nine";
            }
        }
        else {
            if (n % 2 == 0) {
                cout<<"even";
            } else {
                cout<<"odd";
            }
        }
        cout<<endl;
    }
    return 0;
}

