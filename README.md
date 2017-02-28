# python3-unittest-runner

This is a Python3 runner that executes tests based on the `unittest` module.

## How to Use it

In order to use this runner for your project, edit the `codingame.yml` file and add the following lines to your project:

    runner:
      name: codingame/python3-unittest-runner
      version: 3.6

## Example

In this example, the user is asked to write a method `to_upper` (file `uppercase.py`):

```python
def to_upper(string):
    return string.upper()
```

In order to test the answer, the following unit test is created (file `string_tests.py`):

```python
import unittest


class StringTests(unittest.TestCase):
    def test_to_upper(self):
        import uppercase
        self.assertEqual(uppercase.to_upper('foo'), 'FOO', "Wrong uppercase value for foo")
        self.assertEqual(uppercase.to_upper('Bar'), 'BAR')
```

In the markdown file, the unit test can be called using:

`@[Test unittest: uppercase]({"stubs":["uppercase.py"], "command":"string_tests.StringTests.test_to_upper"})`


## Compatibility

If a Virtualenv is detected, the runner will use it to execute the project.
