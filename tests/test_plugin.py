import unittest
from nose.plugins import PluginTester
from nose_run_line_number.plugin import RunLineNumber


class TestNoseLinePlugin(PluginTester, unittest.TestCase):
    activate = '--line-file'
    plugins = [RunLineNumber()]
    suitepath = 'tests/other_test.py'

    def setUp(self):
        pass

    def _run_test_on_line(self, line):
        self.args = ['',  '--line', str(line), '--match', 'linenumtest.*']
        super(TestNoseLinePlugin, self).setUp()

    def test_run_line_of_method_definition(self):
        self._run_test_on_line(6)
        self.assertIn("Ran 1 test", self.output)
        self.assertIn("OK", self.output)

    def test_run_line_inside_method_definition(self):
        self._run_test_on_line(7)
        self.assertIn("Ran 1 test", self.output)
        self.assertIn("OK", self.output)

    def test_run_line_past_method_definition(self):
        self._run_test_on_line(8)
        self.assertIn("Ran 1 test", self.output)
        self.assertIn("OK", self.output)

    def test_run_line_before_any_method_definitions_skips_test(self):
        self._run_test_on_line(1)
        self.assertIn("Ran 0 tests", self.output)
        self.assertIn("OK", self.output)