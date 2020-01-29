#include <iostream>
#include <iomanip>
using std::cin;
using std::cout;
using std::endl;
using std::fixed;
using std::setprecision;

int main()
{
    int user_input;
    double distance_km, distance_m, km_per_day, m_per_day, m_per_hour, radio_time;
    cin >> user_input;
    cout << fixed;
    cout << setprecision(2);
    km_per_day = (14.33 * 60 * 60 * 24);
    distance_km = (km_per_day * user_input) + (149598000 * 37.33);
    m_per_day = (8.90 * 60 * 60 * 24);
    distance_m = (m_per_day * user_input) + (92955800 * 37.33);
    double m_per_s=299792458;
    m_per_hour = m_per_s * 60 * 60;
    radio_time = ((distance_km * 2 * 1000) / (m_per_hour));
    cout << fixed;
    cout << setprecision(2);
    cout <<  distance_km << endl;
    cout <<  distance_m << endl;
    cout <<  radio_time << endl;
}