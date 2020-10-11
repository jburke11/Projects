#ifndef proj3_H
#define proj3_H
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

struct Store{
    string name;
    string location;
    map<string, pair<int,long>> stock;
    Store(string info);
    int count_items();
    int & get_quant(string item);
    float get_price(string item);

};

struct PlacesToShop{
    vector<Store> places;
    map<string, int> total_items;
    PlacesToShop(string);
    string shopping_list(string);
    PlacesToShop() = default;
    void consolidate();
    void shopping (string);
    vector<Store> find_product(string);
    vector<pair<string,double>>get_prices(string);
    void print_info();
};






#endif