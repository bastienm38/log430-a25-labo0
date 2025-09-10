# LOG430 - Labo 00

Bastien Mallet

1. En exécutant la commande pytest, les tests qui ont échoués sont affichés dans le terminal comme ci-dessous : 

```
===================================================================== FAILURES =====================================================================
________________________________________________________________ test_addition_fail ________________________________________________________________

    def test_addition_fail():
        my_calculator = Calculator()
>       assert my_calculator.addition(5, 3) == 38
E       assert 8 == 38
E        +  where 8 = addition(5, 3)
E        +    where addition = <calculator.Calculator object at 0x7f5a08673390>.addition

src/tests/test_calculator.py:21: AssertionError
============================================================= short test summary info ==============================================================
FAILED src/tests/test_calculator.py::test_addition_fail - assert 8 == 38
```

La ligne où le test échoue est indiquée avec l'erreur pour laquelle le test a échoué.

Ici, le test `addition_fail()` échoue volontairement car la fonction `addition(5,3)` renvoie 8 alors que le résultat 
attendu, qui est volontairement erroné, est de 38.



