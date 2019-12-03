#include "utils/calculator.hpp"
#include <iostream>

int main(int argc, char *argv[])
{
    Utils::Calculator calc;

    std::cout<<"------ VALUE ------"<<std::endl;
    for(int i=0; i<10; i++){
        std::cout<<calc.addition(i,15)<<std::endl;
    }
    return 0;
}