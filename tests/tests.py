import sys
print sys.path

import unittest
from testjson import test_obj
from jsonc.generators import PythonDefinitions


class TestDefinitions(unittest.TestCase):
	def test_assignment_definition(self):
		definitions = PythonDefinitions()
		self.assertEqual(definitions.Assignment('foo', 'bar'), 'foo = bar\n')		

	def test_property_definition(self):
		pass

	def test_getter_definition(self):
		pass

	def test_setter_definition(self):
		pass

	def test_args_definition(self):
		pass

	def test_function_definition(self):
		pass


class TestGenerators(unittest.TestCase):
	def test_class_generation(self):
		pass

if __name__ == '__main__':
    unittest.main()