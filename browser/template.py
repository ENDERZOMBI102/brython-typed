"""
The module template allows to dynamically generate some elements in a page,
by including Python code blocks or expressions inside the HTML code.
"""
from typing import Union, List, Callable, Dict, Any

from browser import DOMNode, DOMEvent


TEMPLATE_CALLBACK = Callable[ [ DOMEvent, DOMNode ], None ]


class Template:

	callbacks: List[ TEMPLATE_CALLBACK ]
	element: DOMNode
	indent: int
	line_mapping: Dict[int, Any]
	line_num: int
	python: str

	def __init__( self, element: Union[str, DOMNode], callbacks: List[ TEMPLATE_CALLBACK ] ):
		pass

	def render( self, **kwargs ) -> None:
		pass
