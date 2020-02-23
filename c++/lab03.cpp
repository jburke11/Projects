#include <iostream>
#include <iomanip>
#include <cmath>
using std::pow;
using std::cin;
using std::cout;
using std::endl;
using std::fixed;
using std::setprecision;


double fn (double x){
    double a=0, result=0;
    a = pow (x, 2);
    result = ((-6 * a) + ( 5 * x ) + 3);
    return result;
}

double integral (double x){
    double first, second, third, result, div1=5, div2=2, div;
    first = pow(x, 3);
    first = first * -2;
    second = pow(x, 2);
    div = div1 / div2;
    second = (second * div);
    third = 3 * x;
    result = first + second + third;
    return result;
}

double trapezoid(double a, double b, long n){
    double sum=0, result=0, x=0,  c=0, h=0, y=0;
    h = (b-a) / n;
    y = b-a;
    for (int i = 1; a <= b; i++){
        if (i == 1){
            sum = sum + fn(a);
            x = a + h;
        }
        else if  (x == b){
            sum = sum + fn(x);
            break;}
        else {
            sum = sum + 2 * fn(x);
            x = x + h;
        }
    }
     result = sum * (y / (2 * n));
     return result;
}

int main (){
    long n=0, i=0;
    double trap=0, a=0, b=0, difference=0, answer=0, high=0, low=0, tolerance=0, diff=0, answer1, answer2;
    cout << "Lower Range:" << endl << "Upper Range:" << endl << "Tolerance:" << endl << "Initial trapezoid count:" << endl;
    cin >> a >> b >> tolerance >> n;
    cout<< fixed;
    cout<< setprecision(4);
    answer1 = integral(a);
    answer2 = integral(b);
    answer = answer2 - answer1;
    low = answer - tolerance;
    high = answer + tolerance;
    trap = trapezoid (a, b, n);
    while ((low > trap) || (trap > high)){
        trap = trapezoid (a, b, n);
        if ((low <= trap) && (trap <= high)){
            cout << "Trap count:" << n << ", estimate:" << trap << ", exact:"<< answer <<", tolerance:" << tolerance << endl;
            break;
        }
        diff = answer - trap;
        cout << "intermediate result:"<< trap <<", traps:" << n << ", diff:" << diff << endl;
        n = n * 2;
    }
}