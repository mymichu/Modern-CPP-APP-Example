#!/bin/bash
conan remove "*" -f
#conan search "*"
conan create . user/testing
#conan search "*"
