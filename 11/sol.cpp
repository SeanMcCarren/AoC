#include <regex>
#include <iostream>
#include <sstream>
#include <string>
#include <deque>
#include <vector>
#include <fstream>
#include <sstream>

using namespace std;


class Monkey {
    public:
    Monkey(smatch match) {
        nr = stoi(match[1]);
        string segment;
        stringstream strm(match[2]);
        while (getline(strm, segment, ',')) {
            items.push_back(stoi(segment));
        }
        op_is_plus = match[3] == '+';
        op_is_mul = match[3] == '*';
        right_is_num = isdigit(string(match[4])[1]);
        if (right_is_num) {
            right_num = stoi(match[4]);
        }
        div_test = stoi(match[5]);
        true_throw = stoi(match[6]);
        false_throw = stoi(match[7]);
        inspected = 0;
    };
    
    void play_turn(vector<Monkey> &monkeys) {
        while (items.size() > 0) {
            inspected++;
            int item = items[0];
            items.pop_front();
            if (right_is_num) {
                if (op_is_plus) {
                    item = item + right_num;
                } else if (op_is_mul) {
                    item = item * right_num;
                }
            } else {
                if (op_is_plus) {
                    item = item + item;
                } else if (op_is_mul) {
                    item = item * item;
                }
            }
            item = item / 3;
            if (item % div_test == 0) {
                monkeys[true_throw].items.push_back(item);
            } else {
                monkeys[false_throw].items.push_back(item);
            }
        }
    };
    
    int nr;
    deque<int> items;
    bool op_is_plus;
    bool op_is_mul;
    bool right_is_num;
    int right_num;
    int div_test;
    int true_throw;
    int false_throw;
    int inspected;
};


string inp = R""""(Monkey 0:
  Starting items: 93, 54, 69, 66, 71
  Operation: new = old * 3
  Test: divisible by 7
    If true: throw to monkey 7
    If false: throw to monkey 1

Monkey 1:
  Starting items: 89, 51, 80, 66
  Operation: new = old * 17
  Test: divisible by 19
    If true: throw to monkey 5
    If false: throw to monkey 7

Monkey 2:
  Starting items: 90, 92, 63, 91, 96, 63, 64
  Operation: new = old + 1
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 3

Monkey 3:
  Starting items: 65, 77
  Operation: new = old + 2
  Test: divisible by 3
    If true: throw to monkey 4
    If false: throw to monkey 6

Monkey 4:
  Starting items: 76, 68, 94
  Operation: new = old * old
  Test: divisible by 2
    If true: throw to monkey 0
    If false: throw to monkey 6

Monkey 5:
  Starting items: 86, 65, 66, 97, 73, 83
  Operation: new = old + 8
  Test: divisible by 11
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 6:
  Starting items: 78
  Operation: new = old + 6
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1

Monkey 7:
  Starting items: 89, 57, 59, 61, 87, 55, 55, 88
  Operation: new = old + 7
  Test: divisible by 5
    If true: throw to monkey 2
    If false: throw to monkey 5
)"""";

int main() {
    string str(inp);
    regex reg (
        "\\s*Monkey (\\d+):\\s*" \
        "Starting items: ([\\d, ]+)\\s*" \
        "Operation: new = old ([+|*]) ([\\d+|old])\\s*" \
        "Test: divisible by (\\d+)\\s*" \
        "If true: throw to monkey (\\d+)\\s*" \
        "If false: throw to monkey (\\d+)" \
    );
    smatch monkey_match;

    vector<Monkey> monkeys = {};
    while(regex_search(str, monkey_match, reg)) {
        monkeys.push_back(Monkey(monkey_match));
        str = monkey_match.suffix();
    }
    
    cout << monkeys.size() << endl;
    
    for (int round = 1; round <= 20; round++) {
        for (int m = 0; m < monkeys.size(); m++) {
            monkeys[m].play_turn(monkeys);
        }
    }
    
    for (int m = 0; m < monkeys.size(); m++) {
        cout << monkeys[m].inspected << endl;
    }
}