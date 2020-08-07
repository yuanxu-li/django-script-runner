# Django Script Runner

_Django Script Runner is a django-based web application, where you can run and demonstrate your Python script in an interactive way._

It can be used in the following scenarios:
- demo your course/work project
- build a simple web app with a useful python script of your own
- educate yourself or others

## Important links
* Repository: https://github.com/yuanxu-li/django-script-runner
* Issues: https://github.com/yuanxu-li/django-script-runner/issues

## Usage

Assume you want to demonstrate a multiply function of three floats

### Installation
```bash
> git clone git@github.com:yuanxu-li/django-script-runner.git
```

### Upload
```bash
> vi django-script-runner/scripts/scripts.py
```
Or use your favorite IDE to update the `run` function in `django-script-runner/scripts/scripts.py`.

The original file is
```python
def run(a, b):
    return int(a) + int(b)
```

Let's update it to
```python
def run(mul_1, mul_2, mul_3):
    return float(mul_1) * float(mul_2) * float(mul_3)
```

### Run
```bash
> python manage.py runserver
```
The prompt will tell where to find the web app. Usually it is http://127.0.0.1:8000/
Then you can type in three variables in the form, and click "Submit" to get your result back, as seen ![here](https://github.com/yuanxu-li/django-script-runner/blob/master/demo.png)

## Team

* [@yuanxu-li](https://github.com/yuanxu-li)

## Errors / Bugs

If something is not working correctly, or if you have any suggestion on improvements, [report it here](https://github.com/yuanxu-li/django-script-runner/issues)

## Copyright

Copyright (c) 2020 Justin Li. Released under the [MIT License](https://github.com/yuanxu-li/html-table-extractor/blob/master/README.md)

Third-party copyright in this distribution is noted where applicable.