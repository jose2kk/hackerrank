#include <iostream>
#include <cstdio>
using namespace std;

int max_of_four(int a, int b, int c, int d) {
    if (a < b) {
        a = b;
    }
    if (a < c) {
        a = c;
    }
    if (a < d) {
        return d;
    }
    return a;
}

int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    int ans = max_of_four(a, b, c, d);
    cout << ans;
    
    return 0;
}