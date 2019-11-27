from conans import ConanFile, CMake

class Calculator(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "doctest/2.3.4@bincrafters/stable" # comma-separated list of requirements
    generators = "cmake", "gcc", "txt"

    def configure_cmake(self):
        cmake = CMake(self)

        # put definitions here so that they are re-used in cmake between
        # build() and package()
        cmake.definitions["BUILD_UTEST"] = "ON"
        cmake.definitions["USE_COVERAGE"] = "ON"

        cmake.configure()
        return cmake

    def build(self):
        cmake = CMake(self)
        cmake = self.configure_cmake()
        cmake.build()
        # run unit tests after the build
        cmake.test()
        self.run("../show_coverage.sh")
        