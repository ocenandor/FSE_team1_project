cmake_minimum_required(VERSION 3.10)

# Define main project
project(On-img LANGUAGES CXX C VERSION 0.1)

# Project authors
set(AUTHOR "Garifullin K., Alekseev A., Bexultanova A., Tikhomirov P., Zinkovich V.")
set(DESCRIPTION "Soft for recognising numbers from images")


# Specific C++ compiler
set(CMAKE_CXX_FLAGS "-fpermissive -O3 -std=c++17")

# Module path for CMake
set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH}
                     "${CMAKE_SOURCE_DIR}/make")

# Executable target
add_executable(on-img "")

set_target_properties(on-img
  PROPERTIES
  CXX_STANDARD 17
  )

# Install into the current directory
install(TARGETS on-img
        RUNTIME DESTINATION .)

# Include directories for make
include_directories(.)
include_directories(make)
add_subdirectory(make)
add_subdirectory(python)
