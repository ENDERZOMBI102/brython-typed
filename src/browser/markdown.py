"""
markdown is a mode of text formatting adapted to publication on Internet, more simple to edit than HTML.
A complete description is available on the mardown site. The module markdown is a slightly adapted version to enrich the rendering options:
the markdown tags _text_ and *text* match two different HTML tags: <I> and <EM>
__text__ and **text** match <B> and <STRONG>
underscores inside a word are left unchanged
Lines that start with ``` followed by a text (eg. ```python) are translated to a <PRE> element with the text as class name (<PRE class="python">)
"""
from typing import Tuple, List


def mark(src: str) -> Tuple[ str, List[str] ]:
	"""
	The function returns a 2-element tuple: html, scripts
		- html is the HTML code generated from the source,
		- scripts is a list of all the source code of scripts found in the page.
	\t
	:param src: A string holding text formatted with the markdown syntax.
	"""