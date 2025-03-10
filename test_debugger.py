import unittest
from build_debugger import get_openai_suggestions, run_mypy, run_pylint, run_flake8

class TestDebugger(unittest.TestCase):

    def test_get_openai_suggestions(self):
        # This is a placeholder test. You would need to mock the OpenAI API call.
        code = "def add(a, b): return a + b"
        suggestions = get_openai_suggestions(code)
        self.assertIsInstance(suggestions, str)

    def test_run_mypy(self):
        # This is a placeholder test. You would need a valid Python file to test.
        result = run_mypy('test_script.py')
        self.assertIsInstance(result, str)

    def test_run_pylint(self):
        # This is a placeholder test. You would need a valid Python file to test.
        result = run_pylint('test_script.py')
        self.assertIsInstance(result, str)

    def test_run_flake8(self):
        # This is a placeholder test. You would need a valid Python file to test.
        result = run_flake8('test_script.py')
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
