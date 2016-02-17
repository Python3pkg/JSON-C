import json

JSON = '''
	{
		"Class1": {
			"Decorator": "ClassDecorator",
			"Superclass": "object",
			"Properties": {
				"Prop1": {
					"Decorator": "PropertyDecorator",
					"Type": "Int",
					"Default": 0
				},
				"Prop2": {
					"Decorator": "PropertyDecorator",
					"Type": "String",
					"Default": "Foo"
				}
			}
		},
		"Class2": {
			"Decorator": "ClassDecorator",
			"Superclass": "object",
			"Properties": {
				"Prop3": {
					"Decorator": "PropertyDecorator",
					"Type": "Int",
					"Default": 0
				},
				"Prop4": {
					"Decorator": "PropertyDecorator",
					"Type": "String",
					"Default": "Bar "
				}
			}
		}
	}
'''

cls_format = '''class {cls_name}({superclass}):
{defs}'''

decorator_format = '''@{dec}
{defs}'''

prop_format = '''
\t{dft}
\t@{dec}
\tdef {name}(self):
\t\treturn self._{name}

\t@{name}.setter
\tdef {name}(self, value):
\t\tself._{name} = value

'''

def GenerateClass(cls_name, cls_def, decorate=True):
	if decorate:
		return Decorate(cls_def, GenerateClass(cls_name, cls_def, False))
 	return cls_format.format(cls_name=cls_name, superclass=cls_def['Superclass'], defs=GenerateProperties(cls_def['Properties']))

def GenerateProperties(prop_defs):
	props = ''
	for prop_name in prop_defs:
		props = props + GenerateProperty(prop_name, prop_defs[prop_name])
	return props

def GenerateProperty(prop_name, prop_def, decorate=True):
	return prop_format.format(name=prop_name, dec=prop_def['Decorator'], dft=Default(prop_name, prop_def['Default'], prop_def['Type']))

def Default(prop_name, value, type):
	f = '_{name} = {value}'
	if type == "String":
		value = '\'{}\''.format(value)

	return f.format(name=prop_name, value=value)

def Decorate(def_dict, defs):
	if 'Decorator' in def_dict:
		return decorator_format.format(dec=def_dict['Decorator'], defs=defs)
	return defs


if __name__ == '__main__':
	cls_defs = json.loads(JSON)
	for cls_name in cls_defs:
		print GenerateClass(cls_name, cls_defs[cls_name])