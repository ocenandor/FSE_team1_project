#include <calculator.h>
#include <python/lib_cython.h>
#include <iostream>

int main() 
{
    Calculator p;
    std::cout << p.sum(2, 4) << std::endl;
}