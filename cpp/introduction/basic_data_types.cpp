#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a;
    long b;
    char c;
    float d;
    double e;

    cin >> a >> b >> c >> d >> e;
    cout << a << "\n" << b << "\n" << c << endl; 
    cout.precision(3);
    cout<<fixed<<d<<endl;
    cout.precision(9);
    cout<<fixed<<e<<endl;
    return 0;
}