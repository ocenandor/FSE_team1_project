from libcpp.memory cimport shared_ptr, make_shared

cdef extern from "lib_cython.h" namespace "img::lib_cython":
    
    cdef cppclass p_Calculator:
        p_Calculator()
        int sum(int a, int b)
        int substract(int a, int b)

