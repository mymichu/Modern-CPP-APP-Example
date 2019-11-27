#!/bin/bash
conan install . --install-folder build
conan build . --build-folder build