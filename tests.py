import unittest
import sys
import json
import os
from io import StringIO
import contextlib


@contextlib.contextmanager
def stdIO():
    old, err = sys.stdout, sys.stderr
    sys.stdout, sys.stderr = StringIO(), StringIO()
    yield sys.stdout, sys.stderr
    sys.stdout, sys.stderr = old, err


class CustomTestRunner:
    def run(self, test):
        result = JsonTestResult(self)
        test(result)
        return result


class JsonTestResult(unittest.TestResult):
    """CustomTestRunner to generate a JSON CodinGame-compatible file."""

    def __init__(self, runner):
        unittest.TestResult.__init__(self)
        self.runner = runner
        self.logs = []

    def addError(self, test, err):
        unittest.TestResult.addError(self, test, err)
        self.logs.append({"message": str(err[1])})

    def addFailure(self, test, err):
        unittest.TestResult.addFailure(self, test, err)
        self.logs.append({"message": str(err[1])})

    def getResult(self, s, e):
        out = {
            "success": self.wasSuccessful(),
            "logs": self.logs,
            "programStderr": e.getvalue(),
            "programStdout": s.getvalue()
        }
        return out


os.system("cp -r /project/target/* /project/workspace")
os.system("cp -r /project/answer/* /project/workspace")
sys.path.append("/project/workspace")

executions_result = []

for test in sys.argv[1:]:
    suite = unittest.defaultTestLoader.loadTestsFromName(test)
    with stdIO() as (s, e):
        result = CustomTestRunner().run(suite)
    executions_result.append(result.getResult(s, e))

executions_json = open('/project/results/executions.json', 'w')
executions_json.write(json.dumps(executions_result))
