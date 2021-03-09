#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <iostream>
#include <sstream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <deque>
#include <iomanip>
#include <unordered_map>
#include <unordered_set>
#include <fstream>
using namespace std;
typedef long long ll;
typedef pair<int, int> PII;

#define PB push_back
#define MP make_pair
#define AA first
#define BB second
#define SZ size()
#define BG begin()
#define OP begin()
#define ED end()
#define SQ(x) ((x)*(x))
#define cmax(x, y) x = max(x, y)
#define cmin(x, y) x = min(x, y)

int main() 
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int i, j, u, v, w;
    //freopen("", "r", stdin);
    //freopen("", "w", stdout);
    
    int n; cin >> n;
    int tot = 0;
    int amtLeft = 2*n;

    int mins[n];
    int maxs[n];
    int decs = 0;

    int nl; int a; int b;
    int first; int one; int two;
    bool flag;
    
    for (int i = 0; i < n; i++) {
        flag = true;
        cin >> nl;
        cin >> first;
        one = first;
        for (int j = 1; j < nl; j++) {
            cin >> two;
            if (two - one > 0) {
                tot += amtLeft - 1;
                amtLeft -= 2;
                flag = false;
                break;
            }
            one = two;
        }
        if (flag) {
            a = first;
            b = one;
            mins[decs] = b;
            maxs[decs] = a;
            decs++;
            if (a != b) tot++;
        }
    }
    
    for (ll i = 0; i < decs; i++) {
        for (ll j = i + 1; j < decs; j++) {
            if (mins[i] < maxs[j]) tot++;
            if (maxs[i] > mins[j]) tot++;
        }
    }
    cout << tot;

    return 0;
}