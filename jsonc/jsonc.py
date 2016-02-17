import json
from defaults import obj
from generators.models import Class
from generators import PythonGenerator

if __name__ == '__main__':
	cls_defs = obj
	for cls_name, cls_def in cls_defs.items():
		gen = PythonGenerator(Class(cls_name, **cls_def))
		print gen