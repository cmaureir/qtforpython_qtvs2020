#include "test.hpp"

TestClass::TestClass(const std::string &name) : m_name(name) {}

TestClass::~TestClass(){}

std::string TestClass::say_hello() {
    std::string msg = "Hello, my name is " + m_name;
    return msg;
}

std::vector<std::string> TestClass::glob(const std::string &directory, bool recursive) {
    std::vector<std::string> tmp;
    if (recursive) {
        for (const auto &entry : std::filesystem::recursive_directory_iterator(directory))
            tmp.push_back(entry.path());
    }
    else {
        for (const auto &entry : std::filesystem::directory_iterator(directory))
            tmp.push_back(entry.path());
    }
    return tmp;
}
