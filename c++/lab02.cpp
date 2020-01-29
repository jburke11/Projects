#include <iostream>
#include <iomanip>
using std::cin;
using std::cout;
using std::endl;
using std::fixed;
using std::setprecision;
using std::setw;

int main(){

while (true){
    long in=0, sum=0, count=0, count1=0;
    cin>>in;
    if (in < 0){
        cout<<"Error"<<endl;
        break;
    }
    if (in < 10){
        cout<<"0  "<< in << endl;
        break;}
    else{
        for (count1 = 0; in > 9; count1++){
            sum=0;
            for (count=0; in > 0; count++){
                sum = sum + (in % 10);
                in = in / 10;}
        in = sum;
        }
        
        }   
cout<<count1<<setw(2)<<sum<<endl;
break;
}

}
