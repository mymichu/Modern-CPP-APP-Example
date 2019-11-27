#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN
#include <doctest/doctest.h>
#include <utils/calculator.hpp>

TEST_CASE("Calculator Addition") {
    Utils::Calculator calc;
    int sum = calc.addition(10,15);
    CHECK(sum == 25);
}