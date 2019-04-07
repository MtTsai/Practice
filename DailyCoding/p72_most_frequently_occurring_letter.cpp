#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    // string s = "ABACA";
    // vector<vector<int>> edge = {{0, 1}, {0, 2}, {2, 3}, {3, 4}};
    string s = "A";
    vector<vector<int>> edge = {{0, 0}};

    int n   = s.size();
    int ans = 1;
    for (int i = 0; i < n; i++) {
        vector<int> dp(n, 0);
        dp[i] = 1;

        for (int j = 0; j < n - 1; j++) {
            bool is_update = false;
            for (auto e: edge) {
                int src = e[0], dst = e[1];

                if (dp[src] == 0) continue;

                int tmp = dp[src] + (s[dst] == s[i]);

                if (tmp > dp[dst]) {
                    dp[dst]   = tmp;
                    is_update = true;
                    ans = max(ans, dp[dst]);
                }
            }
            if (!is_update) break;
        }

        /* check if there is cycle existed */
        for (auto e: edge) {
            int src = e[0], dst = e[1];

            if (dp[src] == 0) continue;

            int tmp = dp[src] + (s[dst] == s[i]);

            if (tmp > dp[dst]) {
                ans = 0;
                break;
            }
        }
        if (ans == 0) break;
    }

    cout << ans << endl;

    return 0;
}
