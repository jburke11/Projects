#ifndef VECTOR_H
#define VECTOR_H
#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <stdexcept>
#include <sstream>
#include <iterator>
#include <algorithm>
#include "math_vector.h"
#include <utility>
#include<numeric>
#include <functional>
#include <map>
#include <math.h>
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


class TwoOrLess{
  public:
    std::multiset<int> strange_set;
    pair<std::multiset<int>::iterator, bool> insert(int);
    int count(int);
    int size();
};
#endif