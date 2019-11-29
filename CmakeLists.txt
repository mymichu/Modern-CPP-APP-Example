cmake_minimum_required(VERSION 3.10)

project(calculatorApplication VERSION 1.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 14)

include_directories(src)

add_library(calculator src/utils/calculator.cpp)
add_executable(calculator.exe src/main.cpp src/utils/calculator.cpp)

option(BUILD_UTEST "Build Unit Test" ON)
option(USE_COVERAGE "DO BUILD COVERAGE" OFF)

if(BUILD_UTEST)
    include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
    conan_basic_setup(TARGETS)
    # Code Coverage Configuration
    add_library(test_calc OBJECT src/utils/calculator.cpp)
    add_executable(testCalcAdd test/calculator_test.cpp $<TARGET_OBJECTS:test_calc> ${CONAN_LIBS}) 
    target_link_libraries(testCalcAdd CONAN_PKG::doctest)
    
    if(USE_COVERAGE)
        target_compile_options(testCalcAdd
            PUBLIC
                "-O0"
                "-fprofile-arcs"
                "-ftest-coverage"
        )
        target_link_libraries(testCalcAdd
            gcov
        )
    endif(USE_COVERAGE)

    include(CTest)
    enable_testing()
    add_test(NAME testCalcAdd COMMAND testCalcAdd)
endif(BUILD_TESTS)

