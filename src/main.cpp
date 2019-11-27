#include "utils/calculator.hpp"
#include <iostream>

int main(int argc, char *argv[])
{
    Utils::Calculator calc;

    std::cout<<"------ VALUE ------"<<std::endl;
    std::cout<<calc.addition(10,15)<<std::endl;
    return 0;
}