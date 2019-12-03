from conans import ConanFile, CMake

class Calculator(ConanFile):
    name = "Calculator"
    version = "0.1"
    url = "Basic-Calculator"
    description = "<Description of Hello here>"
    settings = "os", "compiler", "build_type", "arch"
    requires = "gtest/1.8.1@bincrafters/stable" # comma-separated list of requirements
    generators = "cmake", "gcc", "txt"
    exports_sources = "src/*", "test/*", "CMakeLists.txt"

    def configure_cmake(self):
        cmake = CMake(self)

        # put definitions here so that they are re-used in cmake between
        # build() and package()
        cmake.definitions["BUILD_UTEST"] = "ON"
        cmake.definitions["USE_COVERAGE"] = "ON"
        cmake.definitions["CMAKE_BUILD_TYPE"]="Debug"

        cmake.configure()
        return cmake

    def build(self):
        cmake = CMake(self)
        cmake = self.configure_cmake()
        cmake.build()
        cmake.test()
        self.run("../show_coverage.sh")

    def package(self):
        self.copy("*.hpp", dst="include", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["Calculator"]