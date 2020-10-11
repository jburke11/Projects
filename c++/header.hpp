#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <stdexcept>
#include <sstream>
using std::istringstream;
using std::ostringstream;
using std::runtime_error;
using std::pow;
using std::cin;
using std::cout;
using std::endl;
using std::fixed;
using std::setprecision;
using std::string;
using std::max;
using std::vector;
using std::to_string;

#ifndef SPLIT
#define SPLIT
struct SecretKeeper{
    string password;
    string secret;
    string get_secret(string str);
};

#endif