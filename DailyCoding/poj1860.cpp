#include <iostream>
#include <vector>

using namespace std;

class Node_T {
public:
    int dst;
    double R, C;
    Node_T (int _d, double _r, double _c) {
        dst = _d;
        R = _r;
        C = _c;
    }
};

void dump(vector<double> &maxM) {
    for (int i = 0; i < maxM.size(); i++) {
        cout << maxM[i] << " ";
    }
    cout << endl;
}
/* 
 * Example:
 * 3
 * 1.0 1.0 0.0
 * 1.0 1.0 1.1
 * 0.0 1.1 1.0
 * 0.0 1.0 0.0
 * 1.0 0.0 1.1
 * 0.0 1.1 0.0
 * */
int main() {
    int n, m, s;
    /* Start money for type s */
    double v;
    cin >> n >> m >> s >> v;
    s--; // change to 0-based

    vector<vector<Node_T>> RC(n);
    /* Get exchange rate */
    for (int i = 0; i < m; i++) {
        int A, B;
        double Rab, Cab, Rba, Cba;
        cin >> A >> B >> Rab >> Cab >> Rba >> Cba;
        A--; B--; // change to 0-based
        RC[A].push_back(Node_T(B, Rab, Cab));
        RC[B].push_back(Node_T(A, Rba, Cba));
    }

    vector<double> maxM(n, 0); // max Money from s to i
    maxM[s] = v;

    bool update;
    for (int i = 0; i < n; i++) { // for |v| round
        update = false;
        for (int j = 0; j < n; j++) { // for each |v|
            for (int l = 0; l < RC[j].size(); l++) {
                int k = RC[j][l].dst;
                double R = RC[j][l].R, C = RC[j][l].C;
                // 0 to k = max(0 to k, 0 to j to k);
                double curM = (maxM[j] - C) * R;
                if (curM > maxM[k]) {
                    maxM[k] = curM;
                    update = true;
                }
            }
            // dump(maxM);
        }
        // cout << "========" << endl;
        if (!update) {
            break;
        }
    }
    if (update) {
        cout << "YES" << endl;
    }
    else {
        cout << "NO" << endl;
    }

    return 0;
}
