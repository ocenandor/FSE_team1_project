from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
from sys import platform

ext_list = ['img_calculator']

include_dirs = ['..']
libs = ["lib_cython"]

if platform == 'win32':
    path_to_obj = "../make/win/x64/DLL/" # with trailing '/'
    extra_compile_args = ["/std:c++17"]
    extra_libs = ["pch"] + libs
    extra_link_args = [path_to_obj + s + '.obj' for s in extra_libs]
else:
    path_to_obj = ""
    extra_compile_args = ["-std=c++17","-fpermissive","-Wno-sign-compare","-Wno-reorder","-Wno-char-subscripts"]
    extra_libs = libs
    extra_link_args = ["-lstdc++"]
    extra_link_args = extra_link_args + ["build/" + s + '.o' for s in extra_libs]

ext_modules = [Extension(e, sources=[e + '.pyx'], include_dirs=include_dirs,
                         extra_compile_args=extra_compile_args, extra_link_args=extra_link_args,
                         language='c++') for e in ext_list]

setup(ext_modules = ext_modules, cmdclass = {'build_ext': build_ext})
