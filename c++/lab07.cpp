#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <stdexcept>
#include <sstream>
#include <Iterator>
#include <algorithm>
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
using std::iterator;
using std::sort;
using std::copy;
using std::back_inserter;
using std::stoi;
using std::copy_if;
using std::transform;
using std::find;
using std::setw;

template<typename T>
using matrix_row = vector<T>;

template<typename T>
using matrix = vector<matrix_row<T>>;

/* 
nicely print a matrix. Should have row/column alignment
converts it to a string (doesn't print to cout!!!)
uses width to space elements (setw). Default is 3
*/
template<typename T>
string matrix_to_str(const matrix<T> &m1, size_t width=3){
ostringstream oss;
auto size = m1.size(); 
for (auto i = 0; i < size; i++){
    matrix_row<T> row = m1[i];
    auto row_size = row.size();
    oss << setw(width);
    for (auto j = 0; j < row_size - 1; j++ ){
        T value = row[j];
        oss << value;
        oss << setw(width);
    }
    T last = row[row_size - 1];
    oss << last;
    oss << endl;
}
return oss.str();
}

/*
true if the two matrices have the same shape
false otherwise
*/
template<typename T>
bool same_size(const matrix<T>& m1, const matrix<T>& m2){
int size1 = 0, size2 = 0;
for (auto row : m1){
    for (auto value : row){
        size1 += 1;
    } 
}
for (auto row : m2){
    for (auto value : row){
        size2 += 1;
    }
}
if ( size1 == size2){
    return 1;
}
else {
    return 0;
}
}

/*
matrices must not be empty and must be the same shape:
- if true, return a new matrix that adds m1+m2
- if false, return an empty matrix (no elements)
*/
template<typename T>
matrix<T> add(const matrix<T>& m1, const matrix<T>& m2){
bool shape = same_size(m1, m2);
if (shape && !m1.empty() && !m2.empty()){
    matrix<T> result;
    auto rows = m1.size();
    for (int i = 0; i < rows; i++){
        matrix_row<T> row1 = m1[i];
        matrix_row<T> row2 = m2[i];
        matrix_row<T> new_row;
        auto values = row1.size();
        for (int j = 0; j < values; j++){
            T sum = row1[j] + row2[j];
            new_row.push_back(sum);
        }
        result.push_back(new_row);
    }
    return result;
}
else {
    matrix<T> mat;
    return mat;
}
}

/* 
matrix must not be empty:
- if true, multiply T scalar value by m
- if false, return empty matrix (no elements)
*/
template<typename T>
matrix<T> scalar_multiply(const matrix<T> &m, const T & val){
    if (!m.empty()){
        matrix<T> result;
        for (auto row : m){
            matrix_row<T> new_row;
            for (auto value : row){
                T mult = value * val;
                new_row.push_back(mult);
            }
            result.push_back(new_row);
        }
        return result;
    }
    else {
        matrix<T> mat;
        return mat;
    }
}
    
int main(){
  matrix<long> m1{ {0,1,2}, {3,4,5}, {6,7,8} };
  matrix<long> m2{ {0,1}, {2,3}, {4,5} };
  matrix<long> m3;
  matrix<long> result;
  // case 1
  cout << "Case 1" << endl;
  result = add(m1,m1);
  if (! result.empty() )
    cout << matrix_to_str(result) << endl;
  else
    cout << "could not add" << endl;

  
  // case 2
  cout << "Case 2" << endl;
  result = add(m1, m2);
  if (! result.empty() )
    cout << matrix_to_str(result) << endl;
  else
    cout << "could not add" << endl;

  // case 3
  cout << "Case 3" << endl;
  matrix<double> m_d { {0.3,1.2}, {2,3.4}, {4,-5} };
  double factor = 3.8;
  
  matrix<double> result_d = scalar_multiply(m_d, factor);
   if (! result_d.empty() )
    cout << matrix_to_str(result_d, 8) << endl;
   else
    cout << "could not multiply" << endl;

   // case 4
   cout << "Case 4" << endl;
  result = scalar_multiply(m3,3l);
   if (! result.empty() )
    cout << matrix_to_str(result) << endl;
  else
    cout << "could not multiply" << endl; 
  
}