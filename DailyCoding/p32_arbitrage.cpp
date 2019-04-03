#include <iostream>
#include <vector>

using namespace std;

int n;

void input_rate(vector<vector<double>> &rate) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> rate[i][j];
        }
    }
}

void input_comm(vector<vector<double>> &comm) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> comm[i][j];
        }
    }
}
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
    cin >> n;

    vector<vector<double>> R(n, vector<double>(n, 0)); /* Rate[i][j]: rate i to j */
    vector<vector<double>> C(n, vector<double>(n, 0)); /* Commission[i][j]: commission i to j */
    // currency exchange => (moneyA - C) * R = moneyB

    /* Get exchange rate */
    input_rate(R);
    /* Simplify the problem, no commission */
    input_comm(C);

    /* Start money for one type */
    double moneyS = 20;

    vector<double> maxM(n, 0); // max Money from 0 to i
    maxM[0] = moneyS;

    bool update;
    for (int i = 0; i < n; i++) { // for |v| round
        update = false;
        for (int j = 0; j < n; j++) { // for each |v|
            for (int k = 0; k < n; k++) {
                // 0 to k = max(0 to k, 0 to j to k);
                double curM = (maxM[j] - C[j][k]) * R[j][k];
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
