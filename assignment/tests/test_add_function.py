from assignment.assignment_1.assignment import add
from assignment.tests.tud_test import *



def test_add():
    set_keyboard_input(["3","2"])
    theSum = add()
    output = get_display_output()

    assert output == [
        "Enter a number: ",
        "Enter a number: ",
        "The sum of the numbers is 5"
    ]

    assert theSum == 5