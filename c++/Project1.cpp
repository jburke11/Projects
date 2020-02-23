#include <iostream>
#include <iomanip>
#include <cmath>
using std::cin;
using std::cout;
using std::endl;
using std::fixed;
using std::setprecision;
using std::noskipws; 
using std::setw;
using std::abs;
using std::pow;

int count_numbers(int number){  // count digit function from lab 2
    int count1, sum, count;
    if (number == 0){ // 1 digit even though it is zero
        return 1;
    }
    for (count=0; number > 0; count++){ // counts individual digits in a number with modulus math
         sum = sum + (number % 10);
        number = number / 10;}
    return count;
} 

int convert_other_base_to_decimal(int num, int base){
    int count_num = count_numbers(num);
    int  s=0, temp_count = count_num;       // I learned the basics of arrays from the c++ docs
    int array [count_num];                  //http://www.cplusplus.com/doc/tutorial/arrays/
    for (int count=0; num > 0; count++){    //this takes each individual digit and makes an array
        array [count] = {num % 10};     // this assigns each index as the digit 
        num = num / 10;} 
    for (int count=count_num - 1; count >= 0 ; count--){  //this loop builds the resulting number by iterating through the array
           int power=0;                                   // and doing the math to create the new number
           temp_count = temp_count - 1;
           power = pow(base, temp_count);
           s = s + (array[count] * power);
        }
    return s;
}

int convert_decimal_to_other_base(int decimal, int base){ 
    int div=0, power=0, count=0, count_power=0, result_final=0;
    float result=0, remain=0;
    while (decimal != 0){   // this section builds the new number by creating a temporary floating point number
    div = decimal / base;   // by doing the math, shifting the current number over, and adding in the new number
    remain = decimal % base;
    count = count_numbers(remain);
    power = pow(10, count);
    remain = remain / power;
    result = result / power;
    result = result + remain;
    count_power++;  
    if (div == 0){ // if the divider == 0 stop
        break;
    }
        decimal = div;
    }
    
    result = result * pow(10, count_power);     //this part converts the result from float to int to create the result
    result_final = static_cast<int> (result);   // discovered how to use static cast from https://stackoverflow.com/questions/2544394/c-floating-point-to-integer-type-conversions
    return result_final;                        // this number will always be an int so static cast won't do anything weird
}

int math_in_other_base(int num1, int num2, int base, int method){
    int result=0;
    if (base != 10){
        num1 = convert_other_base_to_decimal(num1, base);   //if the numbers aren't base 10 convert them
        num2 = convert_other_base_to_decimal(num2, base);
    }
    switch(method){ //switch statement for all possible types of math, does base 10 int math
        case '+':{
            result = num1 + num2;
            break;
        } 
        case '-':{
            result = num1 - num2;
            break;
        }
        case '/':{
            result = num1 / num2;
            break;
        }
        case '%':{
            result = num1 % num2;
            break;
        }
        case '*':{
            result = num1 * num2;
            break;
        }
    }
    if (base == 10){
        return result;  // if the base is 10 return the result
    }
    else {  //otherwise convert the result back to the original base
        result = convert_decimal_to_other_base(result, base);
        return result;
    }
    return result;
}

int main(){
    int num1, num2, result, base;
    char method;
    cin >> num1 >> num2 >> base >> method;
    result = math_in_other_base(num1, num2, base, method);
    cout << result << endl;
}