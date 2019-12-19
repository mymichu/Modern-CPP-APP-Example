#!/bin/bash
DIRECTORY=`dirname $0`
mkdir $DIRECTORY/build/coverage
lcov --capture --directory $DIRECTORY/build/CMakeFiles/ --output-file $DIRECTORY/build/coverage/coverage.info
genhtml $DIRECTORY/build/coverage/coverage.info --output-directory $DIRECTORY/build/coverage/out