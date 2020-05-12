#ifndef TESTCLASS_H
#define TESTCLASS_H

#include <string>
#include <vector>
#include <iostream>
#include <filesystem>

class TestClass
{
public:
    TestClass(const std::string &name);
    ~TestClass();
    std::string say_hello();
    std::vector<std::string> glob(const std::string &directory, bool recursive);
private:
    std::string m_name;
};
#endif // TESTCLASS_H
