#include "pch.h"
#include "lib_cython.h"
#include <calculator.h>

namespace img::lib_cython {

    p_Calculator::p_Calculator()
    {
        p = std::make_shared<Calculator>();
    }

    int p_Calculator::sum(int a, int b)
    {
        return p->sum(a, b);
    }

    int p_Calculator::substract(int a, int b)
    {
        return p->substract(a, b);
    }
}
