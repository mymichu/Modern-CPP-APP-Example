#include <gtest/gtest.h>
#include <utils/calculator.hpp>



TEST (Calculator, Addition) {
    Utils::Calculator calc;
    EXPECT_EQ (5, calc.addition(-10,15));
    EXPECT_EQ (-38, calc.addition(-20,-18));
    EXPECT_EQ (25, calc.addition(10,15));
}

TEST (Calculator, Subtraction) {
    Utils::Calculator calc;
    EXPECT_EQ (-25, calc.subtraction(-10,15));
    EXPECT_EQ (-2, calc.subtraction(-20,-18));
    EXPECT_EQ (-5, calc.subtraction(10,15));
}