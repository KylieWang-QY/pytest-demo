# pytest demo - test automation
## Install pytest package
```
$ pip install pytest
$ pip list
$ pip show pytest
$ pytest --version
$ pytest --help
```

## pytest demo
Writing an add function, and giving the test strategy

## test_func.py
Run command to see the test result
```
$ pytest --vv test_func.py
```
To calculate execute time for each test
```
$ pytest --durations=0 -vv test_func.py
```
To test error, add the code to `test_func.py`
```
$ pytest -vv 
```