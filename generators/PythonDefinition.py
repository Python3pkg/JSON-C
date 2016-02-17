def ident(s, nident=1):
	ident = '\t' * nident
	return ident + s.replace('\n', '\n' + ident)

# class PythonGenerator(object):
# 	"""docstring for PythonGenerator"""
# 	def __init__(self, defs):
# 		super(PythonGenerator, self).__init__()
# 		self.defs = defs
		
# 	def Header(self):
# 		return ''

# 	def Assignment (self, var, value):
# 		return '{} = {}'.format(var, value)

# 	def Class(self, decorator=None, name, super="object", content, nident=0):
# 		return '{decorator}\n{ident}{name}({super}:\n{content})'.format(ident=nident*'\t', )


class PythonDefinitions(object):
	"""docstring for PythonDefinitions"""
	def __init__(self, arg):
		super(PythonDefinitions, self).__init__()
		self.arg = arg

	def Header(self):
		return ''

	def Assignment (self, var, value=''):
		return '{} = {}\n'.format(var, value)

	def Property(self, name, default=None, decorator=None):
		return '{default}{getter}\n{setter}'.format(default=self.Assignment('_'+name, default), 
														getter=self.Getter(name, decorator), 
														setter=self.Setter(name))

	def Getter(self, name, decorator=''):
		return self.Function(name, ['self', 'value'], 'return self._'+name, decorator)

	def Setter(self, name):
		content = self.Assignment('self._'+name, 'value')
		return self.Function(name, ['self', 'value'], content, name+'.setter')

	def Args(self, l):
		return ', '.join(l)

	def Function(self, name, args, content, decorator=None):
		return '{decorator}def {name}({args}):\n{content}'.format(decorator=self.Decorator(decorator), 
																	name=name, 
																	args=self.Args(args), 
																	content=ident(content))

	def Class(self, content, name, decorator=None, supercls="object"):
		return '{decorator}class {name}({super}):\n{content}'.format(decorator=self.Decorator(decorator), name=name, super=supercls, content=ident(content))

	def Decorator(self, dec):
		if dec:
			return '@{}\n'.format(dec)
		return ''

		

if __name__ == '__main__':
	d = PythonDefinitions('a')
	print d.Class('pass', "Empty")
	print d.Property('Color', decorator='dimension')