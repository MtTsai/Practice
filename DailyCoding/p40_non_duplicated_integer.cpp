#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;

    int one = 0, two = 0;
    for (int i = 0; i < n; i++) {
        int t, zero;
        cin >> t;

        zero = ~(one | two);
        two = (one & t) | (two & ~t);
        one = (zero & t) | (one & ~t);

        cout << one << " " << two << endl;
    }

    cout << one;

    return 0;
}
