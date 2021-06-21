"""
The module browser.webcomponent is used to create custom HTML tags, using the standard DOM WebComponent technology.
"""
from typing import Literal, List, Dict

from browser import DOMNode


SHADOW_ROOT_MODE = Literal[ 'open', 'closed' ]



# TODO: implement those, but i have no fucking clue what those are
class CSSStyleSheet:
	pass


class Animation:
	pass


class Selection:
	pass


# noinspection PyPropertyDefinition
class _ShadowRoot:

	@property
	def activeElement( self ) -> DOMNode:
		""" Returns the DOMNode within the shadow tree that has focus. """

	@property
	def delegatesFocus( self ) -> bool:
		""" Returns a boolean that indicates whether delegatesFocus was set when the shadow was attached. """

	@property
	def fullscreenElement( self ) -> DOMNode:
		""" The element that's currently in full screen mode for this shadow tree. """

	@property
	def host( self ) -> DOMNode:
		""" Returns a reference to the DOM element the ShadowRoot is attached to. """

	@property
	def innerHTML( self ) -> DOMNode:
		""" Sets or returns a reference to the DOM tree inside the ShadowRoot. """

	@innerHTML.setter
	def innerHTML( self, element: DOMNode ) -> None:
		""" Sets or returns a reference to the DOM tree inside the ShadowRoot. """

	@property
	def mode( self ) -> SHADOW_ROOT_MODE:
		"""
		The mode of the ShadowRoot — either open or closed.
		This defines whether or not the shadow root's internal features are accessible from Python/JS.
		"""

	@property
	def pictureInPictureElement( self ) -> DOMNode:
		""" Returns the Element within the shadow tree that is currently being presented in picture-in-picture mode. """

	@property
	def pointerLockElement( self ) -> DOMNode:
		"""
		Returns the Element set as the target for mouse events while the pointer is locked.
		null if lock is pending, pointer is unlocked, or if the target is in another tree.
		"""

	@property
	def styleSheets( self ) -> List[CSSStyleSheet]:
		"""
		Returns a StyleSheetList of CSSStyleSheet objects for stylesheets explicitly linked into, or embedded in a shadow tree.
		"""

	def getAnimations(self) -> List[Animation]:
		"""
		Returns an array of all Animation objects currently in effect, whose target elements are descendants of the shadow tree.
		"""

	def getSelection(self) -> Selection:
		"""
		Returns a Selection object representing the range of text selected by the user, or the current position of the caret.
		"""

	def elementFromPoint(self) -> DOMNode:
		""" Returns the topmost element at the specified coordinates. """

	def elementsFromPoint(self) -> List[DOMNode]:
		"""	Returns an array of all elements at the specified coordinates. """

	def __le__(self, other):
		""" Insert a value in this ShadowRoot instance """


class CustomTag:

	def attachShadow( self, mode: Dict[ Literal['mode'], SHADOW_ROOT_MODE ] ) -> _ShadowRoot:
		""" Create a shadow root. """

	def connectedCallback(self) -> None:
		""" LifeCycle event, can be overwritten """

	def disconnectedCallback( self ) -> None:
		""" LifeCycle event, can be overwritten """

	def adoptedCallback( self ) -> None:
		""" LifeCycle event, can be overwritten """

	def observedAttribute( self ) -> None:
		""" LifeCycle event, can be overwritten """

	def attributeChangedCallback( self, name, old, new, ns ) -> None:
		""" LifeCycle event, can be overwritten """


def define(tag_name: str, component_class: type) -> None:
	"""
	\t
	:param tag_name: The name of the custom tag name.
		The Web Component specification mandates that the tag name includes a dash (the "-" character).
	:param component_class: The class that defines the component behaviour.
		Its __init__ method is called to create the component; the parameter self references the DOM element for the custom component.
	"""


def get(tag_name) -> type:
	"""
	Returns the class associated to tag_name, or None.
	\t
	:param tag_name: Tag to search the class for.
	"""