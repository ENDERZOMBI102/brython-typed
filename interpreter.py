"""
This module provides classes to open a Python interactive interpreter in a page.
It is used by the console and the editor of the site brython.info.
"""
from typing import Optional, Dict, Any

from browser import DOMNode


class Interpreter:
	"""
	The interactive interpreter class.
	"""
	def __init__(
			self,
			element: Optional[DOMNode] = None,
			title: Optional[str] = 'Interactive Interpreter',
			globals: Optional[ Dict[str, Any] ] = None,
			locals: Optional[ Dict[str, Any] ] = None,
			rows: Optional[int] = 30,
			cols: Optional[int] = 84,
			default_css: Optional[bool] = True
		):
		"""
		\t
		:param element: If None, the interpreter is opened in a new dialog box.
		:param title: if element is None, this is the title of the dialog box.
		:param globals: See locals.
		:param locals: Dictionaries globals and locals are the environment where the interpreter
			commands are executed (by default, empty dictionaries).
		:param rows: See cols.
		:param cols: rows and cols are the TEXTAREA dimensions.
		:param default_css: Specifies if the CSS stylesheet provided by the module should be used.
			If the value is False, the styles defined in the HTML page are used
		"""


class Inspector:
	"""
	Opens a dialog box with an interactive interpreter running in the program execution frames.
	This can be used for debugging purposes.
	Note that opening an inspector does not block program execution, but the namespaces used in the inspector represent
	the state of the frames when it was opened.
	"""

	def __init__(
			self,
			title="Frames inspector",
			rows=30,
			cols=84,
			default_css=True
		):
		"""
		\t
		:param title: This is the title of the dialog box.
		:param rows: See cols.
		:param cols: rows and cols are the TEXTAREA dimensions.
		:param default_css: Specifies if the CSS stylesheet provided by the module should be used.
			If the value is False, the styles defined in the HTML page are used
		"""
