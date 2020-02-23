#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    // Write Your Code Here
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
    } else if(n < 10){
        cout<<"nine";
    } else {
        cout<<"Greater than 9";
    }

    return 0;
}