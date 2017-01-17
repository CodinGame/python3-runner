# python3-unittest-runner

This runner works with a Python project or a virtualenv project.

## Example

In this example, the student is asked to write a method `to_upper` (file `uppercase.py`):

```python
def to_upper(string):
    return string.upper()
```

In order to test the answer, the following unit test is created (file `string_tests.py`):

```python
import unittest


class StringTests(unittest.TestCase):
    def test_upper(self):
        import uppercase
        self.assertEqual(uppercase.to_upper('foo'), 'FOO', "Wrong uppercase value for foo")        
        self.assertEqual(uppercase.to_upper('Bar'), 'BAR')
```

In the lesson, the unit test can be called using:

`@[Test unittest: uppercase]({"stubs":["uppercase.py"], "command":"string_tests.StringTests.test_upper"})`
