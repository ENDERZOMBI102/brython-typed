"""
The module javascript allows interaction with the objects defined in Javascript programs and
libraries present in the same page as the Brython program.
\n
The module also allows using objects defined by the Javascript language.
Please refer to the documentation of these objects.
"""
from typing import Union


def py2js(src: str) -> str:
	""" Returns the Javascript code generated by Brython from the Python source code src. """


def this():
	"""
	Returns the Brython object matching the value of the Javascript object this.
	It may be useful when using Javascript frameworks, eg when a callback function uses the value of this.
	"""


class JSON:
	""" Object to convert to and from JSON objects. """

	@staticmethod
	def stringify(obj: object) -> str:
		""" Serialize simple objects (dictionaries, lists, tuples, integers, reals, strings). """

	@staticmethod
	def parse(obj: str) -> object:
		""" Conversion of a JSON-formatted string into a simple object. """


class Math:
	""" Object for mathematical functions and constants. """


class NULL:
	""" The Javascript object null. Can be used to test if a Javascript object is null. """


class Number:
	""" Constructor for objects of type "number". """

	@staticmethod
	def new( self, number: Union[ str, int, float ] ) -> 'Number':
		pass

class RegExp:
	"""
	Constructor of "regular expression" objects, using the Javascript-specific syntax,
	which doesn't fully match that of Python.
	"""

	@staticmethod
	def new( self, regexp: str ) -> 'RegExp':
		pass


class String:
	"""
	Constructor of Javascript objects of type "string".
	Must be used to call methods that accept Javascript regular expressions as parameters
	"""

	@staticmethod
	def new( self, string: str ) -> 'String':
		pass


class UNDEFINED:
	""" The Javascript object undefined. Can be used to test if a Javascript object is undefined. """