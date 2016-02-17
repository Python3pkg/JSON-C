class Class(object):
	"""docstring for Class"""
	def __init__(self, name, Decorator=None, Superclass='object', Properties={}):
		super(Class, self).__init__()
		self.name = name
		self.decorator = Decorator
		self.superclass = Superclass
		self.properties = []
		for name, prop in Properties.items():
			p = Property(name, **prop)
			self.properties.append(p)

class Property(object):
	"""docstring for Property"""
	def __init__(self, name, Type, Default=None, Decorator=None):
		super(Property, self).__init__()
		self.name = name
		self.t = Type
		self.default = Default
		self.decorator = Decorator
		
		