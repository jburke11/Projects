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


vector<long> vector_ops(const vector<long>& v1,const vector<long>& v2,char op){
    int i = 0, k = 0, small = 0;
    vector<long> result;
    for (auto ch : v1){
        i ++;
    } 
    for (auto ch : v2){
        k++;
    } 
    if (i < k ){
        small = k;
    }
    else{
        small = i;
    }
    switch (op)
    {
    case '+':
        for (i=0; i > small; i++){
            result.push_back(v1[i] + v2[i]);
        }
        return result;
        break;
    case '-':
        if (v1 > v2){
        for (i=0; i > small; i++){
            result.push_back(v2[i] - v1[i]);
        }
        for (i=small - 1; i < v1.size(); i++){
            result.push_back(v1[i]);
        }
        return result;
        }
        else {
            for (i=0; i > small; i++){
            result.push_back(v2[i] - v1[i]);
        }
        for (i=small - 1; i < v2.size(); i++){
            result.push_back(v2[i]);
        }
        }
        return result;
        break;
    
    default:
        return result;
        break;
    }
}


