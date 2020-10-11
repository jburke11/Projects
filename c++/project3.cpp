#include <iostream>
#include <iomanip>
#include <cmath>
#include <string>
#include <vector>
#include <stdexcept>
#include <sstream>
#include <unordered_map>
#include <iterator>
#include <algorithm>
#include "project3.hpp"
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

Store::Store(string str){ //converting constructor that turns a string into a struct Store
istringstream iss(str);
getline(iss, name); // get the name and the location of the store and stores it in member variables
getline(iss,location);  
string temp;

while (getline(iss, temp)){ //iterates through the rest of the string to get the items with their quantity and price
    istringstream is1(temp);
    string product;
    vector<string> product_vector;
    while (getline(is1,product,',')){ // when an item is found this extracts the item, quantity and pruce
        product_vector.push_back(product);  // creates a vector of items
    }
    string price;
    std::copy_if(product_vector[2].begin(), product_vector[2].end(), back_inserter<string>(price), [] (char ch){ // takes out the $ and the . to store price as long
        if (ch == '$' || ch == '.'){
            return false; 
        }
        else{
            return true;
        }
    });
    pair<int,long> items(stoi(product_vector[1], nullptr), stol(price, nullptr)); //create pair of quantity and price
    stock[product_vector[0]] = items; // add name, quantity and price to member map stock
}
}
int Store::count_items(){ // counts the number of items a store has
    return stock.size(); 
}

int & Store::get_quant(string item){ // gets the quantity of a specific good and returns a modifiable value
    auto & stock1 = stock;
    int * quant = & stock1[item].first;
    return * quant;
}

float Store::get_price(string item){ // gets the price of a certain item
    return stock[item].second;    
}

PlacesToShop::PlacesToShop(string str){ // a struct that creates and keeps track of stores
    istringstream iss(str);
    string temp;
    ostringstream oss;
    getline(iss, temp); // throw away the header line
    while (getline(iss, temp)){ // iterates through input and creates a "store" any time a empty line is detected
        if (iss.eof()|| temp.empty()){
            Store store(oss.str());
            oss.str("");
            places.push_back(store);
        }
        else {
            oss << temp << endl;
        }
    }
}
void PlacesToShop::consolidate(){ // creates a master map of all items of all stores
    for (auto store : places){
        for (auto [name, price] : store.stock){
                total_items[name] += price.first;
            }
        }
    }


vector<Store> PlacesToShop::find_product(string item){ // finds how many stores have a product and creates a vector of stores
    vector<Store> places_with_item;
    for (auto & store : places){
        if (store.get_quant(item) != 0 ){
            places_with_item.push_back(store);
        }
        else {
            continue;
        }
    }
    return places_with_item;
}

void PlacesToShop::print_info(){ // prints the summary info of places to shop
    cout << "Store Related Information (ordered by in-file order):\n\
There are " << places.size() << " store(s)." << endl;;
    for (auto store : places){
        cout << store.name << " has " << store.count_items() << " distinct items." << endl;
    }
    cout << endl;
    consolidate();
    cout <<"Item Related Information (ordered alphabetically):\n\
There are " << total_items.size() << " distinct item(s) available for purchase." << endl;
    for (auto [name, quant] : total_items){
        cout << "There are " << quant <<" " << name << "(s)." << endl;
    }
}

void PlacesToShop::shopping(string input){ // member function for shopping
    istringstream iss(input);
    string temp;
    float total_price=0.00;
    cout << "Shopping:" << endl;
    while(getline(iss, temp)){ // iterates through input 
        if (iss.eof() || temp.empty()){ // if an empty line is detected stop
            break;
        }
        string item="";
        string quant="";
        std::copy_if(temp.begin(), temp.end(), back_inserter<string>(item), [] (char ch) {return !(isdigit(ch));}); // gets the name of the item
        std::copy_if(temp.begin(), temp.end(), back_inserter<string>(quant), [] (char ch) {return (isdigit(ch));}); // gets the desired quantity of item        
        item.erase(0,1); // gets rid of space in between
        int quantity = stoi(quant); //convert string quantity to an int
        int items_purchased=0;
        float item_price=0;
        vector<std::map<string,pair<string, int>>> prices_vector; // creates a vector of maps to keep track of the order of prices
        cout << "Trying to order " << quantity << " " << item << "(s)." << endl;
        vector<Store> places_with_stock = find_product(item); // creates a vector of stores that have the item
        cout << places_with_stock.size() << " Store(s) sell " << item << "." << endl;
        while (1){ // this determines the cheapest price and "buys" the product
            auto price = std::min_element(places_with_stock.begin(), places_with_stock.end(), [item, places_with_stock] (Store & store1, Store & store2) { 
                if (places_with_stock.size() > 1){ // if the vector is larger than 1 return the smallest price for a given item
                return store1.stock[item].second < store2.stock[item].second;}
                else {
                    return true;
                }
            });
            if (items_purchased < quantity){ // if we have not reached the desired quantity 
                int count = 0;
                while ((*price).stock[item].first != 0 && items_purchased < quantity){ // while the amount that's been purchased is less than what we want
                    (*price).stock[item].first--; // subtract one from the stores stock
                    items_purchased++; // add one to the amount of things we've bought
                    item_price += (*price).stock[item].second; // keeps track of the price for the specific item
                    total_price += (*price).stock[item].second; // keeps track of price for all items
                    count++;
                }
                std::map<string,pair<string, int>> best_prices; // make the map 
                best_prices[(*price).name] = {(*price).location, count }; // add the stores name, location, and however many things we bought
                prices_vector.push_back(best_prices); // add it to the vector
                places_with_stock.erase(price); // erase the store from the vector
            } 
            if (places_with_stock.size() == 0 || items_purchased == quantity){ // once we've got what we need stop
                break;
            }
            }
            cout << fixed << setprecision(2);
            cout << "Total price: $" << item_price * 0.01 << endl;
            for (auto mp : prices_vector){ // iterates through the vector to print what we got
            for (auto [names, prices] : mp){ 
                cout << "Order " << prices.second << " from " << names << " in " << prices.first << endl; 
            }}
            cout << endl;
        }
        cout << "Be sure to bring $" << total_price * 0.01 << " when you leave for the stores.";
    }

int main (){
    string input;
    ostringstream os, os1, os2;
    while (getline(cin, input)){ // takes in input and writes it to an ostringstream
        os2 << input << endl;
    }
    os2 << endl;
    istringstream iss(os2.str()); // creates istringstream with the input 
    while(getline(iss, input)){ // iterates through the input and separates the general info from the shopping list
        auto index = input.find("shopping");
        if (index != string::npos){ // look in the line for the word shopping if its found create the general info and move on to shopping
            PlacesToShop master_list(os.str());
            while (getline(iss, input)){
                if (input.empty() || input == "\n"){ // looks for the eof of the istringstream
                    master_list.print_info();   //once it's found it moves through the shopping list with that string
                    cout << endl;
                    master_list.shopping(os1.str());
                    break;
                }
                else {
                    os1 << input << endl; // adds line to the ostring stream
                }
            }
            break;
        }
        else {
            os << input << endl; // adds line to the ostringstream
        }
    }

}