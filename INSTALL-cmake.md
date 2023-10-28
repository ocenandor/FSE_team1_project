# COMPILATION AND INSTALLATION PROCEDURE

## Build with CMake
The following text assumes some familiarity with CMake and focuses on using
the command line tool cmake and what settings are supported for building.

### Getting started

- First, in a new directory using either the command-line utility (cmake)
or the text-mode UI utility ccmake or the graphical utility cmake-gui,
generate a build environment. E.g., one can use the command-line version of
the CMake with no customization as,
   ```bash
   cd on-lattice-core        # change to repository directory
   mkdir build               # create a build directory
   cd build
   cmake ..                  # configuration
   ```
   This process generates build-files for the default build command. During the
   configuration step, CMake will try to detect whether support for MPI and BLAS
   are available and enable the corresponding configuration settings.

- Second step is compiling the code, and linking of objects, libraries, and
executables.
   ```bash
   make                     # compilation
   ```
   The make command launches the compilation, and, if successful, will ultimately
   produce a binary `on-lattice`

   You can speed this process by a parallel compilation with `make -j N` (with `N`
   being the number of concurrently executed tasks when your machine has multiple
   CPU cores). For example,
   ```bash
   make -j4                 # compilation
   ```

   Later the following will be possible:
   After compilation, you may optionally install the  executable and created
   libraries into your system with:
   ```bash
   make install             # optional, copy files into installation location
   ```
