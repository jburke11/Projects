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


int CloseEnough(const vector<string> & vec, int x){
auto number = std::adjacent_find(vec.begin(), vec.end(), [x] (string str1, string str2) {
  sort(str1.begin(), str1.end());
  sort(str2.begin(), str2.end());
  vector<char> result;
  std::set_difference(str1.begin(), str1.end(), str2.begin(), str2.end(), back_inserter(result));
  if (str1 == "another line in one"){
    for ( char ch : result ){
    cout << ch << endl;
  }
  }
  if (result.size() <= x){
    return true;
  }
  else {
    return false;
  }

});
int res = number - vec.begin();
if (res < vec.size()){
  return res;
}
else {
  return -1;
}
}

int main (){
const std::vector<std::string> more_words {
  "this is a sentence.",
  "this is also words ",
  "another line in one",
  "another LINE_in one",
  "stuff words in open",
  "stuff words in OPEN",
  "whitespace\n\tagain  ",
};
int x = CloseEnough(more_words, 4);
cout << x << endl;
string s = "hi";
}