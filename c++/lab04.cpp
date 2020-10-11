#include <string>
#include <limits>
#include <cctype>
#include<typeinfo>
#include <iostream>
#include <iomanip>
#include <cmath>
using std::pow;
using std::cin;
using std::cout;
using std::endl;
using std::fixed;
using std::setprecision;
using std::string;
using std::max;
using std::numeric_limits;
using std::streamsize;

long loc_to_dec( string loc){
    string alphabet="abcdefghijklmnopqrstuvwxyz";
    int power=0;
    long sum=0;
    for (auto letter : loc){
        power = alphabet.find(letter);
        sum = sum + pow(2, power);
    }
    return sum;
}

int find_dup(string loc){
    int index=0, count=0, i=0;
    for (auto letter : loc){
        index = loc.find(letter, 0);
        if (loc.find(letter, 0 + 1) != string::npos){
             count++;}
        else{
            continue;}
    }
    return count;
}
string erase(char letter, string loc){
    string alphabet="abcdefghijklmnopqrstuvwxyz";
    loc.erase(loc.begin() + loc.find(letter));         /* https://www.geeksforgeeks.org/stdstringerase-in-cpp/ */
    loc.erase(loc.begin() + loc.find(letter));
    int alpha = alphabet.find(letter);
    char new1 = alphabet[alpha + 1];
    loc.push_back(new1);
    
    return loc;
}
string abbreviate( string loc){
string alphabet="abcdefghijklmnopqrstuvwxyz";
    int index=0, sum=0, i =0;
    for (auto letter : loc){
        if (loc.find(letter, index + 1) != string::npos){
            loc = erase(letter, loc);
            cout << loc << endl;
        }
        else{
            cout << loc << endl;
            continue;
        }
    }
    return loc;
}

string dec_to_loc(int dec){
    std::string str (dec, 'a');
    str = abbreviate(str);
    return str;
}

long add_loc (string loc1, string loc2){
    string loc = loc1 + loc2;
    loc = abbreviate(loc);
    long result = loc_to_dec(loc);
    return result;
}

int main (){
    string loc;
    long dec;
    cout << abbreviate("aabbccdd") << endl;
    cout << "Give me a location string:" << endl; cin >> loc;
    cout << "Give me an integer:" << endl; cin >> dec;
    cout << loc<< " to " << "dec: " << loc_to_dec(loc) << endl;
    cout << "abbreviated : " << abbreviate(loc) << endl; 
    cout <<dec << " to loc: " << dec_to_loc(dec) << endl;
    cout << "Give me two more location strings:" << endl;
    string loc1, loc2;
    cin >> loc1, loc2;
    cout << "Sum of " << loc1 << " and " << loc2 << "is: " << add_loc(loc1, loc2); 

}