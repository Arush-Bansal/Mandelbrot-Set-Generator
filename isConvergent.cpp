#include <iostream>
#include <complex>
using namespace std;


// precompile this code before using it in python
// Command => g++ -shared -o isConvergent.so isConvergent.cpp

extern "C"{
    bool isConvergenet(double real, double imag){
        complex<double> number = complex<double>(real, imag);
        int iterNo = 0;
        complex<double> z = complex<double>(0,0);

        while ((abs(z) < 1000)&&(iterNo < 100)){
            z = z*z + number;
            iterNo++;
        }
        if (abs(z) >= 1000){
            return false;
        }
        else{
            return true;
        }
        
    }
}

// int main()
// {
//     cout << isConvergenet(complex<double>(0,0));    
//     return 0;
// }
