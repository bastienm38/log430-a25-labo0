"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

def test_app():
    my_calculator = Calculator()
    assert my_calculator.get_hello_message() == "== Calculatrice v1.0 =="

# TODO: ajoutez les tests
def test_addition():
    my_calculator = Calculator()
    assert my_calculator.addition(2, 3) == 5

#Ce test est censé échouer
def test_addition_fail():
    my_calculator = Calculator()
    assert my_calculator.addition(5, 3) == 38