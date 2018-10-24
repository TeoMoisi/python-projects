from controler import *
from ui import *

def testInit():
    my_list.append([1, 5])
    my_list.append([3, 6])
    my_list.append([6, 4])
    my_list.append([0, 0])
    return(my_list)


def testadd_command():
    testmy_list = testInit()
    test1 = [3, 4]
    test2 = [7, 9]
    ui.add_command(testmy_list, test1)
    ui.add_command(testmy_list, test2)
    assert testmy_list == [[1, 5], [3, 6], [6, 4], [0, 0], [3, 4], [7, 9]]


def test_remove_position():
    testmy_list.append([3,5])
    assert len(testmy_list) == 1
    controler.remove_position(1)
    assert len(testmy_list) == 0

def test_remove_items(testmy_list):
    testmy_list = testInit()
    ui.remove_item_at_poz(testmy_list, 2)
    assert testmy_list == [[1, 5], [3, 6], [0, 0]]


def test_replace():
    testmy_list = testInit()
    ui.replace_item([1, 5], [3, 7])
    assert testmy_list ==  [[3, 7], [3, 6], [6, 4], [0, 0]]

def test_sum_nbs():
    testmy_list = testInit()
    assert ui.return_sume(testmy_list, 1, 3) == complex(10, 15)
    assert ui.return_rume(testmy_lList, 2, 3) == complex(9, 10)


def test_prod():
    testmy_list = testInit()
    assert ui.return_prod(testmy_list, 1, 3) == complex(-6, 48)


def test_filter_real():
    testmy_list = [[1, 5], [3, 6], [6, 4], [11, 0], [4, 5], [-23, 7], [2, 10], [0, 0], [0, -3], [-8, 0]]
    ui.filter_real(testmy_list)
    assert testmy_list == [[11, 0], [0, 0], [-8, 0]]

def test_filter_modulo():
    testmy_list = [[1, 5], [3, 6], [6, 4], [11, 0], [4, 5], [-23, 7], [2, 10], [0, 0], [0, -3], [-8, 0]]
    ui.filter_modulo_numbers(testmy_list, >, 10)
    assert testmy_list == [[11, 0], [-23, 7], [2, 10]]

def test_undo():
    testmy_list = [[1, 5], [3, 6], [6, 4], [11, 0], [4, 5], [-23, 7], [2, 10], [0, 0], [0, -3], [-8, 0]]
    ui.remove_item_at_poz(testmy_list, 4)
    ui.undo(testmy_list)
    assert testmy_list == [[1, 5], [3, 6], [6, 4], [11, 0], [4, 5], [-23, 7], [2, 10], [0, 0], [0, -3], [-8, 0]]


def run_tests():
    testadd_command()
    test_remove_position()
    test_remove_items()
    test_sum_nbs()
    test_prod()
    test_filter_real()
    test_filter_modulo()
