#ifndef __LIB_CYTHON__
#define __LIB_CYTHON__

class Calculator;

namespace img::lib_cython 
{
  class p_Calculator
  {
  public:
      std::shared_ptr <Calculator> p;
      p_Calculator();
      int sum(int a, int b);
      int substract(int a, int b);
  };
}

#endif
