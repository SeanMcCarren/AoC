#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

class TopQueue {
    private:
    vector<int> queue;
    int N;
    public:
    TopQueue(int n) {
        N = n;
        queue.reserve(N);
        for (int i = 0; i < N; i++) {
            queue.emplace_back(0);
        }
    }
    void Add(int x) {
        int i = 0;
        while (i < queue.size() && queue[i] > x) {
            i++;
        }
        if (i < N) {
            //insert at i and move everything back
            for (int j = queue.size()-1; j > i; j--) {
                queue[j] = queue[j-1];
            }
            queue[i] = x;
        }
    }
    int GetSum() {
        int n;
        for (auto v : queue) {
            n += v;
        }
        return n;
    }
};

int main() {
    string line;
    int n;
    ifstream input;
    input.open("input");

    TopQueue MaxK = TopQueue(3);
    int total = 0;

    while (getline(input, line)) {
        if (line.empty()) {
            MaxK.Add(total);
            total = 0;
        } else {
            istringstream number(line);
            number >> n;
            total += n;
        }
    }
    MaxK.Add(total);
    input.close();
    cout << MaxK.GetSum() << endl;
}