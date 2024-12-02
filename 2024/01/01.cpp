#include "../../util.hpp"

int main() {
    auto v = file_to_v();
    const int n = v.size();
    vector<int> left(n), right(n);
    for (int i=0; i<n; i++) {
        auto l = split(v[i]);
        left[i] = stoi(l[0]);
        right[i] = stoi(l[1]);
    }
    sort(left.begin(), left.end());
    sort(right.begin(), right.end());
    int out1 = 0, out2 = 0;
    map<int, int> c1, c2;
    for (int i=0; i<n; i++) {
        out1 += abs(left[i]-right[i]);
        ++c1[left[i]];
        ++c2[right[i]];
    }
    for (auto& [key, val] : c1) out2 += key*val*c2[key];
    cout << out1 << "\n" << out2 << endl;
    return 0;
}