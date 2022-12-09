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

## Bash
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
To test different parameters, add the code to  `test_para.py`
```
$ pytest --vv test_para.py
```
Dividing the test methods into different test groups, and test the methods of a certain group separately during the test
```
$ pytest --markers # See markers (groups)
$ pytest -vv
$ pytest -vv -m g1
$ pytest -vv -m g2
```
