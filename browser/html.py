import re
from typing import Dict, Union, Iterable, Any

if __name__ != '__main__':
	from browser import DOMNode
	POSSIBLE_TAG_CHILD = Union[str, int, float, DOMNode]


def maketag(name: str) -> type:
	"""
	Creates a new class for a tag with the specified name.
	The class can be used like those associated with standard HTML tags :
	"""


tags: Dict[str, type]
"""
Dictionary mapping tag names to the matching class.
If new classes are added by function maketag(), they are also added to this dictionary.
"""


def attribute_mapper(attr: str) -> str:
	"""
	For all the classes defined in the module, this function is called to transform the keyword arguments into HTML tag attributes.
	By default, the function replaces underscores (_) by hyphens (-).
	"""
	return re.sub('^v_(.*)_(.*)$', r'v-\1:\2', attr)


# html element classes


class BASEFONT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <basefont> tag """


class LI(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <li> tag """


class HTML(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <html> tag """


class PARAM(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <param> tag """


class TEXTAREA(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <textarea> tag """


class DD(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <dd> tag """


class KEYGEN(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <keygen> tag """


class U(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <u> tag """


class SOURCE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <source> tag """


class INS(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <ins> tag """


class H3(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <h3> tag """


class ASIDE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <aside> tag """


class DL(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <dl> tag """


class MARK(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <mark> tag """


class BR(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <br> tag """


class META(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <meta> tag """


class TR(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <tr> tag """


class SPAN(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <span> tag """


class CENTER(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <center> tag """


class H2(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <h2> tag """


class KBD(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <kbd> tag """


class BODY(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <body> tag """


class COL(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <col> tag """


class RB(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <rb> tag """


class VAR(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <var> tag """


class STRONG(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <strong> tag """


class H1(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <h1> tag """


class TH(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <th> tag """


class MATH(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <math> tag """


class DIV(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <div> tag """


class SUP(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <sup> tag """


class FOOTER(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <footer> tag """


class CODE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <code> tag """


class SECTION(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <section> tag """


class FONT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <font> tag """


class DFN(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <dfn> tag """


class CAPTION(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <caption> tag """


class PRE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <pre> tag """


class METER(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <meter> tag """


class DEL(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <del> tag """


class PROGRESS(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <progress> tag """


class SAMP(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <samp> tag """


class DATA(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <data> tag """


class BDI(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <bdi> tag """


class ISINDEX(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <isindex> tag """


class HR(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <hr> tag """


class TEMPLATE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <template> tag """


class RTC(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <rtc> tag """


class DIALOG(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <dialog> tag """


class B(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <b> tag """


class RP(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <rp> tag """


class FIGURE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <figure> tag """


class TBODY(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <tbody> tag """


class SELECT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <select> tag """


class MAP(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <map> tag """


class DATALIST(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <datalist> tag """


class BLOCKQUOTE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <blockquote> tag """


class IFRAME(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <iframe> tag """


class MENU(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <menu> tag """


class NAV(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <nav> tag """


class TABLE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <table> tag """


class SVG(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <svg> tag """


class TD(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <td> tag """


class LEGEND(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <legend> tag """


class WBR(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <wbr> tag """


class OPTGROUP(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <optgroup> tag """


class LINK(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <link> tag """


class CANVAS(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <canvas> tag """


class TFOOT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <tfoot> tag """


class ACRONYM(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <acronym> tag """


class SUB(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <sub> tag """


class NOSCRIPT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <noscript> tag """


class EMBED(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <embed> tag """


class H4(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <h4> tag """


class A(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <a> tag """


class BDO(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <bdo> tag """


class FORM(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <form> tag """


class FRAMESET(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <frameset> tag """


class MAIN(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <main> tag """


class ABBR(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <abbr> tag """


class FIELDSET(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <fieldset> tag """


class STYLE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <style> tag """


class FIGCAPTION(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <figcaption> tag """


class ADDRESS(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <address> tag """


class COMMAND(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <command> tag """


class OPTION(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <option> tag """


class STRIKE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <strike> tag """


class TRACK(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <track> tag """


class APPLET(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <applet> tag """


class CITE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <cite> tag """


class THEAD(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <thead> tag """


class HEADER(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <header> tag """


class OBJECT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <object> tag """


class TIME(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <time> tag """


class DETAILS(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <details> tag """


class H6(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <h6> tag """


class BASE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <base> tag """


class AUDIO(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <audio> tag """


class I(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <i> tag """


class ARTICLE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <article> tag """


class PICTURE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <picture> tag """


class HEAD(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <head> tag """


class OL(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <ol> tag """


class SUMMARY(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <summary> tag """


class LABEL(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <label> tag """


class NOFRAMES(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <noframes> tag """


class TT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <tt> tag """


class VIDEO(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <video> tag """


class TITLE(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <title> tag """


class RUBY(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <ruby> tag """


class EM(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <em> tag """


class IMG(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <img> tag """


class MENUITEM(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <menuitem> tag """


class H5(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <h5> tag """


class P(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <p> tag """


class SMALL(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <small> tag """


class RT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <rt> tag """


class UL(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <ul> tag """


class INPUT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <input> tag """


class DIR(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <dir> tag """


class SCRIPT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <script> tag """


class FRAME(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <frame> tag """


class OUTPUT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <output> tag """


class AREA(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <area> tag """


class BUTTON(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <button> tag """


class BIG(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <big> tag """


class Q(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <q> tag """


class S(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <s> tag """


class COLGROUP(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <colgroup> tag """


class DT(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		""" Represents the <dt> tag """
