#pragma once
#include "pch.h"

class Calculator
{
public:

    Calculator() {
        std::cout << "Element Created" << std::endl;
    }

    ~Calculator() noexcept = default;

public:

    int sum(int a, int b)
    {
        return a + b;
    }

    int substract(int a, int b)
    {
        return a - b;
    }

};