#include "singlelink.h"
#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <stdexcept>
#include <sstream>
#include <iterator>
#include <algorithm>
#include <utility>
#include<numeric>
#include <functional>
#include <map>
#include <set>
#include <assert.h>
#include <fstream>
using std::back_inserter;
using std::cin;
using std::copy;
using std::cout;
using std::set;
using std::endl;
using std::find;
using std::fixed;
using std::stoi;
using std::istringstream;
using std::max;
using std::ostream_iterator;
using std::ostringstream;
using std::pow;
using std::reverse_copy;
using std::runtime_error;
using std::setprecision;
using std::string;
using std::to_string;
using std::transform;
using std::vector;
using std::map;
using std::pair;
using std::count_if;
using std::ifstream;
using std::ostream;
using std::sort;
using std::set_intersection;
int main() {
    SingleLink s;
    s.append_back(3);
    s.append_back(4);
    std::cout << "Two Items: " << s << std::endl;

    SingleLink s2(10);
    s2.append_back(3);
    s2.append_back(4);
    std::cout << "Three Items: " << s2 << std::endl;

    s2.del(3);
    std::cout << "Removed 3: " << s2 << std::endl;


    SingleLink s3(56);
    s3.append_back(73);
    s3.append_back(345);
    s3.append_back(1);
    s3.append_back(15);
    std::cout << "Indexing 0: " << s3[0].data_ << std::endl;
    std::cout << "Indexing 1: " << s3[1].data_ << std::endl;
    std::cout << "Indexing 2: " << s3[2].data_ << std::endl;
    std::cout << "Indexing 3: " << s3[3].data_ << std::endl;
    std::cout << "Indexing 4: " << s3[4].data_ << std::endl;
