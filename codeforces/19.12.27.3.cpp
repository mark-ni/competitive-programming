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

int main() {
  
  ios::sync_with_stdio(false);
  cin.tie(0);
  cout.tie(0);
  
  int q; cin >> q;
  int n; int m;
  int moves; int currPop;
  int k;
  
  for (int w = 0; w < q; w++) {
    cin >> n; cin >> m;
    int a[n]; int b[m];
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }
    
    moves = 0;
    currPop = 0;
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            if (a[j] == b[i]) {
                k = j;
                break;
            }
        }
        if (k < currPop) moves++;
        else {
            k -= currPop;
            currPop = k + currPop + 1;
            moves += 2 * k + 1;
        }
    }
    cout << moves << endl;
  }
  
  return 0;
}