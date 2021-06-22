""" This module provides dialog boxes. """

from typing import Union, Optional, Tuple, List

from .. import html
from .._BaseClasses import BaseDialog


# noinspection PyPropertyDefinition
class Dialog(BaseDialog):

	@property
	def panel( self ) -> html.DIV:
		""" The DIV element where additional elements can be inserted to build the dialog box. """

	@property
	def ok_button( self ) -> html.BUTTON:
		""" The "Ok" button, if present. An event handler should be defined for the "click" event. """

	def __init__(
			self,
			title,
			*,
			top=None,
			left=None,
			default_css=True,
			ok_cancel: Optional[ Union[ bool, Tuple[str, str], List[ str ] ] ] = False
		):
		"""
		\t
		:param title: The box title.
		:param top: See left.
		:param left: They are the position of the box relatively to the top and left borders of the visible part
			of the document. By default, the box is centered.
		:param default_css: Specifies if the style sheet provided by the module should be used.
			If set to False, the styles defined in the HTML page are used.
		:param ok_cancel: specifies if buttons "Ok" and "Cancel" should be displayed.
			If the value passed is a 2-element list or tuple of strings, these stings will be printed in the buttons;
			if the value is True, strings "Ok" and "Cancel" are printed
		"""

	def close( self ) -> None:
		""" Closes the dialog(?). """


# noinspection PyMissingConstructor
class InfoDialog(Dialog):

	def __init__(
			self,
			title: str,
			message: str,
			*,
			top: Optional[int] = None,
			left: Optional[int] = None,
			default_css: Optional[bool] = True,
			remove_after: Optional[int] = None,
			ok: Optional[ Union[bool, str] ] = False
		):
		"""
		\t
		:param title: The box title.
		:param message: The message to print.
		:param top: See left.
		:param left: They are the position of the box relatively to the top and left borders of the visible part
			of the document. By default, the box is centered.
		:param default_css: Specifies if the style sheet provided by the module should be used.
			If set to False, the styles defined in the HTML page are used.
		:param remove_after: The number of seconds after which the box is automatically closed.
		:param ok: Specifies if an "Ok" button should be present.
			If the value passed is a string, it will be printed in the button; if is is True, the string "Ok" is printed.
		"""


# noinspection PyMissingConstructor
class EntryDialog(Dialog):

	value: str

	def __init__(
			self,
			title: str,
			message: Optional[str] = None,
			*,
			top: Optional[int] = None,
			left: Optional[int] = None,
			default_css: Optional[bool] = True,
			ok: Optional[ Union[bool, str] ] = True
		):
		"""
		\t
		:param title: The box title.
		:param message: The optional prompt message to print at the left of the entry zone.
		:param top: See left.
		:param left: They are the position of the box relatively to the top and left borders of the visible part
			of the document. By default, the box is centered.
		:param default_css: Specifies if the style sheet provided by the module should be used.
			If set to False, the styles defined in the HTML page are used.
		:param ok: Specifies if an "Ok" button should be present.
			If the value passed is a string, it will be printed in the button; if is is True, the string "Ok" is printed.
		"""
