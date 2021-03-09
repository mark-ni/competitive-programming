/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>
#include <array>

using namespace std;

char theNext;
char theLast;

char getOther(char x, char y) {
    if (x == 'a') {
        if (y != 'b') {
            return 'b';
        }
        else {
            return 'c';
        }
    }
    else if (x == 'b') {
        if (y != 'a') {
            return 'a';
        }
        else {
            return 'c';
        }
    }
    if (y != 'a') {
        return 'a';
    }
    return 'b';
}

void getAns(string s) {
    char curr = 'q';
    for (int i = 0; i < s.length(); i++) {
        if (s.at(i) == curr && s.at(i) != '?') {
            cout << -1;
            return;
        }
        curr = s.at(i);
    }
    
    if (s.length() == 1) {
        if (s.at(0) == '?') {
            cout << 'a';
            return;
        } else {
            cout << s.at(0);
            return;
        }
    }
    
    if (s.at(0) == '?') {
        if (s.at(1) != 'a') {
            cout << 'a';
            theLast = 'a';
        } else {
            cout << 'b';
            theLast = 'b';
        }
    } else {
        cout << s.at(0);
        theLast = s.at(0);
    }
    
    for (int x = 1; x < s.length() - 1; x++) {
        if (s.at(x) == '?') {
            theNext = s.at(x+1);
            if (theNext == '?') {
                if (theLast == 'a') {
                    cout << 'b';
                    theLast = 'b';
                } else {
                    cout << 'a';
                    theLast = 'a';
                }
            }
            else {
                cout << getOther(s.at(x + 1), theLast);
                theLast = getOther(s.at(x + 1), theLast);
            }
        }
        else {
            cout << s.at(x);
            theLast = s.at(x);
        }
    }
    
    if (s.at(s.length() - 1) == '?') {
        if (s.at(s.length() - 2) == 'a') {
            cout << 'b';
        } else {
            cout << 'a';
        }
    } else {
        cout << s.at(s.length() - 1);
    }
}

int main()
{
    int n; cin >> n;
    string f;
    for (int i = 0; i < n; i++) {
        cin >> f;
        getAns(f);
        cout << endl;
    }

    return 0;
}