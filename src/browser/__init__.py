from typing import Any, List, Union

from ._BaseClasses import DOMNode, DOMEvent, BaseDialog


def alert(message: str) -> None:
	"""
	A function that shows a message in a pop-up window
	\t
	:param message: Message to show
	:returns: None
	"""


def bind(target: Union[str, BaseDialog], event: str):
	""" A function used as a decorator for event binding. """


def confirm(message: str) -> bool:
	"""
	A function that prints the message in a window, and two buttons (ok/cancel)
	Returns True if ok, False if cancel
	"""


class _Console:

	def log(self, msg: Any) -> None:
		pass


console: _Console
"""
	An object with methods to interact with the browser console.
	Its interface is browser-specific.
	It exposes at least the method log(msg), which prints the message msg in the console
"""


class _Query:

	def getfirst(self, key: str, default: Any = None) -> Any:
		"""
		Returns the first value for key.
		If no value is associated with the key, returns default if provided, else returns None.
		"""

	def getlist(self, key: str) -> List[Any]:
		"""
		Returns the list of values associated with key (the empty list if there is no value for the key).
		"""

	def getvalue( self, key: str, default: Any = None ) -> Any:
		"""
		Same as document.query[key], but returns default or None if there is no value for the key.
		"""

	def __getitem__(self, item: str) -> Any:
		"""
		Returns the value associated with key.
		If a key has more than one value (which might be the case for SELECT tags with the attribute MULTIPLE set, or for <INPUT type="checkbox"> tags), returns a list of the values.
		Raises KeyError if there is no value for the key.
		"""


class _Document(DOMNode):

	body: DOMNode

	def getElementById(self, elt_id: str) -> DOMNode:
		pass

	def createElement(self, tagName) -> DOMNode:
		"""
		Creates and return a new element.
		\t
		:param tagName: Type of the element to create
		"""

	def appendChild(self, elt: DOMNode) -> None:
		"""
		Appends an element to the document.
		\t
		:param elt: The element to append
		"""

	query: _Query

	def __getitem__(self, item: str):
		pass

	def __setitem__(self, key: str, value: DOMNode):
		pass


document: _Document
""" An object that represents the HTML document currently displayed in the browser window. """


def load(script_url: str) -> None:
	"""
	Load the Javascript library at address script_url.
	This function uses a blocking Ajax call.
	It must be used when one can't load the Javascript library in the html page by <script src="prog.js"></script>.
	The names inserted by the library inside the global Javascript namespace are available in the Brython script as
	attributes of the window object.
	\t
	:param script_url: the url of the js file to load
	"""


def prompt(message: str, default: str = '') -> str:
	"""
	A function that prints the message in a window, and an entry field.
	Returns the entered value; if no value was entered, return default if defined, else the empty string
	\t
	:param message: the message the prompt will display
	:param default: default value, used if the user didn't input anything
	"""


def run_script(src: str, name: str = '') -> None:
	"""
	This function executes the Python source code in src with an optional name.
	It can be used as an alternative to exec(), with the benefit that the indexedDB cache is used for
	importing modules from the standard library.
	\t
	:param src: python code
	:param name: optional module name (?)
	"""


# noinspection PyPropertyDefinition
class _Window:
	""" An object that represents the browser window """

	document: _Document

	@property
	def innerHeight(self) -> int:
		""" The inner height of the browser window (in pixels). """

	@property
	def innerWidth(self) -> int:
		""" The inner width of the browser window (in pixels). """

	def open(self) -> None:
		""" Open a new window. """

	def close(self) -> None:
		""" Close the current window. """

	def moveTo(self) -> None:
		""" Move the current window. """

	def resizeTo(self) -> None:
		""" Resize the current window. """

	def print( self ) -> None:
		""" To open a print dialog (to a printer). """


window: _Window