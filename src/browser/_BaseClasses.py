""" PRIVATE MODULE, DO NOT USE """
from typing import Dict, Any, List, Optional, Union


class BaseDialog:
	pass


class DOMEvent:
	""" The class of DOM events """


class DOMNode:
	""" The class of DOM nodes """
	attrs: Dict[ str, Any ]
	innerHTML: str
	# --- brython specific properties ---
	abs_left: int
	""" Position of the element relatively to the document left border (1) """
	abs_top: int
	""" Position of the element relatively to the document top border (1) """
	children: List['DOMNode']
	child_nodes: List['DOMNode']
	class_name: str
	height: int
	""" Element height in pixels (2) """
	html: str
	left: int
	parent: Optional[ 'DOMNode' ]
	""" The element's parent (None for doc) """
	scrolled_left: int
	""" Position of the element relatively to the left border of the visible part of the document (1) """
	scrolled_top: int
	""" Position of the element relatively to the top border of the visible part of the document (1) """
	text: str
	top: int
	width: int
	""" Element width in pixels (2) """

	def bind(self, target: str, event: str):
		pass

	def clear( self ):
		"""  Removes all the descendants of the element. """

	def closest( self, tag_name: str ) -> 'DOMNode':
		"""
		Find the first element with the requested tag name.
		\t
		:param tag_name: tag to search for
		:returns: the first parent element with the requested tag name
		:raises KeyError: if no element is found.
		"""

	def index( self, selector: str = None ) -> int:
		"""
		returns the index (an integer) of the element among its parent's children.
		If selector is specified, only the elements matching the CSS selector are taken into account;
		in this case, if no element matches, the method returns -1.
		"""

	def inside( self, other: 'DOMNode' ) -> bool:
		"""
		Tests if self is contained inside element other
		\t
		:param other: The node to check
		:returns: wether this element is inside other
		"""

	def get( self, name: str = '', selector: str = '' ) -> List[ 'DOMNode' ]:
		""" selects elements """

	def select( self, css_selector: str ) -> List['DOMNode']:
		return self.get( selector=css_selector )

	def select_one( self, css_selector: str ) -> Union[ None, List['DOMNode'] ]:
		""" Returns the elements matching the specified CSS selector, otherwise None """

	def __le__(self, other: 'DOMNode') -> None:
		""" Add a child to this element. """
		pass

	def __iter__(self) -> 'DOMNode':
		pass

	def __next__(self) -> 'DOMNode':
		pass

	def __delitem__(self, key: str) -> None:
		pass