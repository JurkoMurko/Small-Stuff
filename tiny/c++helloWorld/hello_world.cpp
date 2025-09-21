#include <iostream>
#include <cmath>
using namespace std;

float test(float x) {
    x = 3.5;

    return x ;
}

int main() {
    float x = 2.5;
    float* y = &x;
    cout<<*y;

    // cout<<test(7)<<endl;
    // cout<<1/sqrt(7);
    return 0;
}
