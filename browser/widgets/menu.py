""" This module is made to build a menu, made of an horizontal navigation bar and drop-down submenus. """
from typing import Callable

from browser import document, DOMNode, DOMEvent, html


class Item:
	pass


class Menu:
	def __init__(
			self,
			container: DOMNode = document.body,
			default_css: bool = True
		):
		"""
		\t
		:param container: The element the navigation bar is inserted into.
		:param default_css: Specifies if the default style sheet provided by the module should be used.
		"""

	def add_item(self, label: str, callback: Callable[ [DOMEvent], None ] = None) -> Item:
		"""
		Add an item to the menu and returns it.
		\t
		:param label: The element text.
		:param callback: if callback is provided, it is the function called when the item is clicked on.
			This function takes a single argument, an object of type event
		"""

	def add_link(self, label: str, href: str) -> html.A:
		"""
		Add a link (HTML tag <A>) to the menu and return this element.
		\t
		:param label: The link text.
		:param href: The address associated with the link.
		"""

	def add_menu(self, label: str) -> 'Menu':
		"""
		Add a submenu to the current menu and returns it; the submenu is also an instance of the class Menu,
		so that other items and submenus can be added with the same methods.
		\t
		:param label: The name of the submenu, printed in the current menu.
		"""