# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import triangle as module_0


def test_case_0():
    none_type_0 = None
    bool_0 = True
    str_0 = module_0.triangle(none_type_0, none_type_0, bool_0)
    assert str_0 == "Isosceles triangle"


def test_case_1():
    int_0 = -62
    dict_0 = {int_0: int_0, int_0: int_0}
    int_1 = -3557
    str_0 = module_0.triangle(dict_0, int_0, int_1)
    assert str_0 == "Scalene triangle"


def test_case_2():
    int_0 = -1729
    none_type_0 = None
    str_0 = module_0.triangle(int_0, none_type_0, int_0)
    assert str_0 == "Isosceles triangle"
    int_1 = -2501
    str_1 = module_0.triangle(int_1, int_1, int_1)
    assert str_1 == "Equilateral triangle"


def test_case_3():
    bool_0 = False
    bool_1 = True
    str_0 = module_0.triangle(bool_0, bool_1, bool_1)
    assert str_0 == "Isosceles triangle"
    int_0 = 885
    bool_2 = True
    str_1 = module_0.triangle(int_0, int_0, bool_2)
    assert str_1 == "Isosceles triangle"
