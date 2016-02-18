from setuptools import setup

setup(name='jsonc',
      version='0.1',
      description='JSON-C is a code generating tool that allows the user to generate class definitions for C# and Python.',
      url='https://github.com/iancarv/JSON-C',
      author='Ian Carvalho',
      author_email='iancarv@gmail.com',
      license='MIT',
      packages=['jsonc', 'tests'],
      install_requires=[],
      test_suite="tests",
      zip_safe=False)