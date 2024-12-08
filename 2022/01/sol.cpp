#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main() {
    string line;
    int n;
    ifstream input;
    input.open("2024/input");

    int max_total = 0;
    int total = 0;

    while (getline(input, line)) {
        if (line.empty()) {
            max_total = max(max_total, total);
            total = 0;
        } else {    
            istringstream number(line);
            number >> n;
            total += n;
        }
    }
    max_total = max(max_total, total);
    input.close();
    cout << max_total << endl;
}