#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <map>

std::vector<std::string> file_to_v() {
    const std::string filename = "input.txt";
    std::ifstream ifs(filename);
    if (!ifs) throw std::runtime_error("bad file");
    std::vector<std::string> out;
    std::string line;
    while (std::getline(ifs, line)) out.push_back(line);
    return out;
}

std::vector<std::string> split(const std::string& s) {
    std::istringstream iss(s);
    std::string t;
    std::vector<std::string> out;
    while (iss >> t) out.push_back(t);
    return out;
}

using namespace std;
