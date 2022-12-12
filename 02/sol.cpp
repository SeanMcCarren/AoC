#include <fstream>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

enum MOVE {
    ROCK = 0,
    PAPER = 1,
    SCISSORS = 2
};

MOVE read(char c) {
    switch (c) {
        case 'A':
        case 'X':
        return ROCK;
        case 'B':
        case 'Y':
        return PAPER;
        case 'C':
        case 'Z':
        return SCISSORS;
        default:
        ROCK;
    }
    return ROCK;
};

int main() {
    char a = ' ';
    ifstream input;
    input.open("input");
    int total_score = 0;

    int i = 0;
    while (!input.eof()) {
        input >> a;
        MOVE other = read(a);
        input >> a;
        MOVE own = read(a);
        total_score += ((static_cast<int>(own) - static_cast<int>(other) + 4) % 3) * 3 + static_cast<int>(own) + 1;
    }
    input.close();
    cout << total_score << endl;
}