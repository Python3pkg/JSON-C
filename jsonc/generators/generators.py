class PythonGenerator(object):
	"""docstring for PythonGenerator"""
	def __init__(self, cls):
		super(PythonGenerator, self).__init__()
		self.cls = cls
		
	def GenerateClass(self):
		defs = PythonDefinitions()
		content = ''
		for i, p in enumerate(self.cls.properties):
			print defs.Property(p.name, self.GenerateDefault(p.default), p.decorator)

	def GenerateDefault(self, value):
		return repr(value)
