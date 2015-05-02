# testing_python_book

Code from "Testing Python" book

## To run tests

Via unittest:
```bash
python3 -m unittest test/unit/calculator_app/calculate_test.py
```

Via nose:
```bash
nosetests
```

All tests via nose:
```bash
nosetests test/unit/calculator_app/calculate_test.py
```

`nosetests` does not run executable files by default, so one should make them non-executable by `chmod -x *.py` or
explicitly tell nosetests to run executable files by `--exe`. chmod can not make files at ntfs/fat32 partitions
executable.

Use `--rednose` to color test results (same name package required).

Via py.test:
```bash
py.test
```

## To debug

PDB:
```bash
nosetests --pdb
py.test --pdb
```

## To check test coverage

Package `nose-cov` required:
```bash
nosetests --with-coverage
```

Package `pytest-cov`:
```bash
py.test --cov-report term-missing --cov calculator_app/ test/
```

Generate report:
```bash
nosetests --with-coverage --cover-html
py.test --cov-report html --cov calculator_app/ test/
```

Coverage threshold:
```bash
nosetests --with-coverage --cov-min-percentage=95
```

To uncover some code:
```python
def func():  #pragma: no cover
```

## To run doctests

```bash
py.test --doctest-modules calculator_app/ test/unit/calculator_app/
nosetests --with-doctest
```

## To run acceptance tests

I use `behave` as an alternative to `lettuce`:
```bash
behave bank/test/bdd/features/
```

Specific test by tag:
```bash
behave --tags=customer_balance bank/test/bdd/features/
```

Robotframwork:
```bash
pybot bank/test/bdd/robot/
```

## Profiling

```bash
python -m cProfile -s time run_bank_app.py
```

Visualization:
```bash
pycallgraph graphviz -- run_bank_app.py
```

## Code validation

```bash
pylint calculator_app/calculate.py
```