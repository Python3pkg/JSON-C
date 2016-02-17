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

test_obj = json.loads(JSON)