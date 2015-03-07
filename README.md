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