# LOG430 - Labo 00

Bastien Mallet

1. En exécutant la commande pytest, les tests qui ont échoués sont affichés dans le terminal comme ci-dessous : 

```
===================================================================== FAILURES =====================================================================
_____________________________________________________________________ test_app _____________________________________________________________________

    def test_app():
        my_calculator = Calculator()
>       assert my_calculator.get_hello_message() == "Calculatrice"
E       AssertionError: assert '== Calculatrice v1.0 ==' == 'Calculatrice'
E         
E         - Calculatrice
E         + == Calculatrice v1.0 ==

src/tests/test_calculator.py:11: AssertionError
============================================================= short test summary info ==============================================================
FAILED src/tests/test_calculator.py::test_app - AssertionError: assert '== Calculatrice v1.0 ==' == 'Calculatrice'
```

La ligne où le test échoue est indiquée avec l'erreur pour laquelle le test a échoué.

Ici, le test `test_app()` échoue car la fonction `get_hello_message()` renvoie `== Calculatrice v1.0 ==` et non `Calculatrice`.

