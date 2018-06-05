import re
import unittest


from metamodel.generators.pythongen import cli
from tests.test_scripts.clicktestcase import ClickTestCase

# This has to occur post ClickTestCase
import click

update_test_files = False

def date_filter(s: str) -> str:
    return re.sub(r'# Generation date: .*\n', '', s, re.MULTILINE)

class GenPythonTestCase(ClickTestCase):
    testdir = "genpython"
    click_ep = cli
    prog_name = "gen-py-classes"

    def test_help(self):
        self.do_test("--help", 'help', update_test_file=update_test_files)
        self.assertFalse(update_test_files, "Updating test files")

    def test_meta(self):
        self.maxDiff=None
        self.do_test(self.metamodel_file, 'meta.py', update_test_file=update_test_files, filtr=date_filter)
        self.do_test(self.metamodel_file + ' -f py', 'meta.py', update_test_file=update_test_files, filtr=date_filter)
        self.do_test(self.metamodel_file + ' -f xsv', 'meta_error', update_test_file=update_test_files,
                     error=click.exceptions.BadParameter)
        self.assertFalse(update_test_files, "Updating test files")

    def test_biolink(self):
        self.maxDiff=None
        self.do_test(self.biolink_file, "biolink-model.py", update_test_file=update_test_files, filtr=date_filter)
        self.assertFalse(update_test_files, "Updating test files")


if __name__ == '__main__':
    unittest.main()
