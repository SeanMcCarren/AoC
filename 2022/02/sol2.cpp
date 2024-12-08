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
    input.open("2024/input");
    int total_score = 0;

    int i = 0;
    while (!input.eof()) {
        input >> a;
        if (input.eof()) break;
        MOVE other = read(a);
        int other_ = static_cast<int>(other);
        input >> a;
        MOVE own = read(a);
        int own_ = (static_cast<int>(own) - 1 + other_ + 3) % 3;
        total_score += ((own_ - other_ + 4) % 3) * 3 + own_ + 1;
        cout << other_ << " " << own_ << " " << total_score << endl;
    }
    input.close();
    cout << total_score << endl;
}