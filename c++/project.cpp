#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <stdexcept>
#include <random>
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

class Measurement{
    public:
    string units;
    double values;
    double error;
    string numerator;
    string denominator="";
    Measurement(double, double, string);
    friend ostream& operator<<(ostream& out, Measurement& m);
    friend Measurement & operator+(Measurement&, Measurement &);
    friend Measurement & operator-(Measurement&, Measurement&);
    friend Measurement & operator*(Measurement&, Measurement&);
    friend Measurement & operator/(Measurement&, Measurement&);
    friend Measurement& operator^(Measurement&, int);
};

Measurement::Measurement(double value, double err, string unit){
    values = value;
    error = err;
    units = unit;
}

ostream& operator<<(ostream& out, Measurement& m){
    out << std::scientific << setprecision(2);
    out << m.values << " +- " << m.error << " " << m.units << " ";
    out << fixed << setprecision(3);
    return out;
}

Measurement& operator+(Measurement& m1, Measurement & m2){
    if (m1.units != m2.units){
        throw std::invalid_argument(" ");
    }
        double value = m1.values + m2.values;
        double first= m1.error, second = m2.error;
        first = pow(first, 2);
        second = pow(second, 2);
        double sum = first + second;
        double result_error = sqrt(sum);
        Measurement * result = new Measurement(value, result_error, m1.units);
        return * result; 
}
Measurement & operator-(Measurement& m1, Measurement & m2){
    if (m1.units != m2.units){
        throw std::invalid_argument(" ");
    }
    double value = m1.values - m2.values;
    double first= m1.error, second = m2.error;
        first = pow(first, 2);
        second = pow(second, 2);
        double difference = first + second;
        double result_error = sqrt(difference);
         Measurement * result = new Measurement(value, result_error, m1.units);
        return * result; 
    
}

Measurement & operator*(Measurement &m1, Measurement &m2){
    double value = m1.values * m2.values;
    double first = m1.error, second = m2.error;
    double first_div = first / m1.values;
    double second_div = second / m2.values;
    first = pow(first_div , 2);
    second = pow(second_div, 2);
    double sum = first + second;
    double result_err = sqrt(sum);
    result_err = result_err * value;
    auto index1 = std::find(m1.units.begin(), m1.units.end(), '^');
    auto index2 = std::find(m1.units.begin(), m1.units.end(), '-');
    auto index3 = std::find(m2.units.begin(), m2.units.end(), '^');
    auto index4 = std::find(m2.units.begin(), m2.units.end(), '-');
    string res_units = "";
    if (index2 == m1.units.end() && index4 == m2.units.end()){
    string base_unit_1="", power_1="" , base_unit_2 = "", power_2 = "";
    std::copy(m1.units.begin(), index1, std::back_inserter<string>(base_unit_1));
    std::copy(index1 + 1, m1.units.end(), std::back_inserter<string>(power_1));
     std::copy(m2.units.begin(), index3, std::back_inserter<string>(base_unit_2));
    std::copy(index3 + 1, m2.units.end(), std::back_inserter<string>(power_2));
        if (index1 == m1.units.end() && index3 == m2.units.end()){
            if (m1.units == m2.units){
                res_units = m1.units + "^2"; 
            }
            else {
                res_units = m1.units + " " + m2.units;
            }
        }
        else if (base_unit_1 == base_unit_2){
            string res_base = base_unit_2;
            if (power_1 == ""){
                power_1 = "1";
            }
            else if (power_2 == ""){
                power_2 = "1";
            }
            int res_power = stoi(power_1) + stoi(power_2);
            string result_pow = to_string(res_power);
            res_units = base_unit_2 + "^" + result_pow;
        }
        else{
            if (power_1 == ""){
                res_units = base_unit_1 + " " + base_unit_2 + "^" + power_2;
            }
            else if (power_2 == ""){
                res_units = base_unit_1 + "^" + power_1 + " " + base_unit_2;
            }
            else {
                res_units = base_unit_1 + "^" + power_1 + " " + base_unit_2 + "^" + power_2;
            }
            }      
    }
    else{
         string base_unit_1="", power_1="" , base_unit_2 = "", power_2 = "", denom1 ="", denom2 = "";
     auto sep1 = std::find(m1.units.begin(), m1.units.end(), ' ');
    auto sep2 = std::find(m2.units.begin(), m2.units.end(), ' ');
    std::copy(m1.units.begin(), index1, std::back_inserter<string>(base_unit_1));
    std::copy(index1 + 1, m1.units.end(), std::back_inserter<string>(power_1));
     std::copy(m2.units.begin(), index3, std::back_inserter<string>(base_unit_2));
    std::copy(index3 + 1, m2.units.end(), std::back_inserter<string>(power_2));
    std::copy(sep1 + 1, m1.units.end(), std::back_inserter<string>(denom1));
    std::copy(sep2 + 1, m2.units.end(),std::back_inserter<string> (denom2));
    string denom = "";
    if (index1 == index2 -1){
        power_1 = "";
        base_unit_1 = "";
        std::copy(m1.units.begin(), sep1, std::back_inserter<string>(base_unit_1));
    }
    if (index3 == index4 - 1){
        power_2 = "";
        base_unit_2 = "";
        std::copy(m2.units.begin(), sep2, std::back_inserter<string>(base_unit_2));
    }
    if (denom1=="" || denom2==""){
        denom = denom1+denom2;
    }
    else {
        string base_denom1 = "", base_denom2 = "", denom = "";
        std::copy(sep1 + 1, index2 - 1, std::back_inserter<string>(base_denom1));
        std::copy(sep2 + 1, index4 - 1, std::back_inserter<string>(base_denom2));
        if (base_denom1 != base_denom2){
            denom = denom1 + " " + denom2;
        }
        else {
            string denom_power1="", denom_power2="";
            std::copy(index2 + 1, m1.units.end(), std::back_inserter<string>(denom_power1));
            std::copy(index4 + 1, m2.units.end(), std::back_inserter<string>(denom_power2));
            int power = stoi(denom_power1) + stoi(denom_power2);
            denom = base_unit_1 + "^-" + to_string(power);
            }
        }
    if (power_1 == "" && power_2 == ""){
        if (base_unit_2 == base_unit_1){
                res_units = base_unit_2 + "^2" + " " + denom; 
            }
            else {
                res_units = base_unit_2 + " " + base_unit_2 + denom;
            }
        }
        else if (base_unit_1 == base_unit_2){
            string res_base = base_unit_2;
             if (power_1 == ""){
                power_1 = "1";
            }
            else if (power_2 == ""){
                power_2 = "1";
            }
            int res_power = stoi(power_1) + stoi(power_2);
            string result_pow = to_string(res_power);
            res_units = base_unit_2 + "^" + result_pow + " " + denom;
        }
        else{
            res_units = base_unit_1 + "^" + power_1 + " " + base_unit_2 + "^" + power_2 + " " + denom;
        }   
    }
    Measurement * finally = new Measurement(value, result_err, res_units);
    return * finally;
}

Measurement & operator/(Measurement &m1, Measurement & m2){
   double value = m1.values / m2.values;
    double first = m1.error, second = m2.error;
    double first_div = first / m1.values;
    double second_div = second / m2.values;
    first = pow(first_div , 2);
    second = pow(second_div, 2);
    double sum = first + second;
    double result_err = sqrt(sum);
    result_err = result_err * value;
    string denom="";
    auto index = std::find(m2.units.begin(), m2.units.end(), '^');
    if (index != m2.units.end()){
        std::copy(m1.units.begin(), m1.units.end(), std::back_inserter<string>(denom));
        denom = denom + " ";
        std::copy(m2.units.begin(), index+1, std::back_inserter<string>(denom));
        denom = denom + '-';
        std::copy(index+1, m2.units.end(), std::back_inserter<string>(denom)); 
    }
    else {
        denom = m1.units+ " " + m2.units + "^-1";  
    }
    Measurement * result = new Measurement(value, result_err, denom);
    return * result;
}


Measurement & operator^(Measurement & m1, int power){
int abs_power = abs(power);
double val = pow(m1.values, power);
double exp = pow(m1.values, power - 1);
double result = abs_power * exp * m1.error;
auto index = std::find(m1.units.begin(), m1.units.end(), '^');
string res_units="";
if (index != m1.units.end()){
    string new_unit="";
    std::copy(index+1, m1.units.end(), std::back_inserter<string>(new_unit));
    int unit = stoi(new_unit);
    unit = unit * power;
    std::copy(m1.units.begin(), index, std::back_inserter<string>(res_units));
    res_units = res_units + "^" + to_string(unit);
}
else {
    res_units = m1.units + "^2";
}
Measurement * res = new Measurement(val, result, res_units);
return * res;
}

int main(){
    
std::ostringstream oss;
Measurement m_1(0.20, 0.01, "s");
Measurement m_2 = m_1 ^ 2;
oss << m_2 << std::endl;
Measurement m_3(34, 1, "m");
Measurement m_4(16, 0.9, "m");
Measurement m_x(13.5, 2.1, "m");
Measurement m_5 = (m_3 + m_4 - m_x) * m_2;
oss << m_5 << std::endl;
oss << (m_5 ^ -1) << std::endl;
oss << (m_5 ^ 3) << std::endl;



std::string expected = "4.00e-02 +- 4.00e-03 s^2 \n1.46e+00 +- 1.77e-01 m s^2 \n6.85e-01 +- 8.30e-02 m^-1 s^-2 \n3.11e+00 +- 1.13e+00 m^3 s^6 \n1.46e+00 +- 2.06e-01 a^2 bb^-1 c^-1 d s^2 \n1.34e+01 +- 2.08e+00 eggs \n";
cout << oss.str() << endl;
cout << expected << endl;
}