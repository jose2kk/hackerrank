#include <iostream>

using namespace std;

int power(int num, int power) {
    int val = 1;
    for (int i = 1; i < power + 1; i++) {
        val = val * num;
    }
    return val;
}



int powerSum(int x, int n, int val) {
    if (power(val, n) < x)
        return powerSum(x, n, val+1) + powerSum(x-power(val, n), n, val+1);
    if (power(val, n) == x)
        return 1;
    return 0;
};

int main() {

    // X represents the total
    int X;
    cin >> X;

    // N represents the power
    int N;
    cin >> N;

    int result = powerSum(X, N, 1);

    std::cout << result << std::endl;

    return 0;
};
