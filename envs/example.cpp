#include <pybind11/pybind11.h>

int add(int x, int y) {
    return x + y;
}

PYBIND11_MODULE(python_example_add, m) {
    m.def("add", &add, "A function which adds two numbers");
}