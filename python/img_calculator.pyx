from cython.operator cimport dereference as deref
from libcpp.memory cimport shared_ptr, make_shared

cimport img_decl as c

cdef class Calculator:

    cdef c.p_Calculator p

    def __cinit__(self, *args, **kwargs):
        self.p = c.p_Calculator()

    def sum(self, a, b):
        return (<c.p_Calculator>self.p).sum(a, b)

    def substract(self, a, b):
        return (<c.p_Calculator>self.p).substract(a, b)