import re
from typing import Dict, Union, Iterable, Any

# to not import browser when generating all the tags
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
	return re.sub("^v_(.*)_(.*)$", r"v-\1:\2", attr)


# html element classes
# {classes}

if __name__ == '__main__':
	from pathlib import Path

	html4_tags = 'A, ABBR, ACRONYM, ADDRESS, APPLET, AREA, B, BASE, BASEFONT, BDO, BIG, BLOCKQUOTE, BODY, BR, BUTTON, CAPTION, CENTER, CITE, CODE, COL, COLGROUP, DD, DEL, DFN, DIR, DIV, DL, DT, EM, FIELDSET, FONT, FORM, FRAME, FRAMESET, H1, H2, H3, H4, H5, H6, HEAD, HR, HTML, I, IFRAME, IMG, INPUT, INS, ISINDEX, KBD, LABEL, LEGEND, LI, LINK, MAP, MENU, META, NOFRAMES, NOSCRIPT, OBJECT, OL, OPTGROUP, OPTION, P, PARAM, PRE, Q, S, SAMP, SCRIPT, SELECT, SMALL, SPAN, STRIKE, STRONG, STYLE, SUB, SUP, SVG, TABLE, TBODY, TD, TEXTAREA, TFOOT, TH, THEAD, TITLE, TR, TT, U, UL, VAR'
	html5_tags = 'ARTICLE, ASIDE, AUDIO, BDI, CANVAS, COMMAND, DATA, DATALIST, EMBED, FIGCAPTION, FIGURE, FOOTER, HEADER, KEYGEN, MAIN, MARK, MATH, METER, NAV, OUTPUT, PROGRESS, RB, RP, RT, RTC, RUBY, SECTION, SOURCE, SUMMARY, TEMPLATE, TIME, TRACK, VIDEO, WBR'
	html51_tags = 'DETAILS, DIALOG, MENUITEM, PICTURE, SUMMARY'
	code = Path(__file__).read_text()
	code = code[: code.index('# {classes}') ]
	tag: str
	for tag in { *html4_tags.split( ', ' ), *html5_tags.split( ', ' ), *html51_tags.split( ', ' ) }:
		code += f"""

class {tag}(DOMNode):
	# noinspection PyDefaultArgument
	def __init__(
			self,
			content: Union[ POSSIBLE_TAG_CHILD, Iterable[POSSIBLE_TAG_CHILD] ],
			attributes: Dict[str, Any] = dict(),
			style: Dict[str, Any] = dict(),
			Class: str = ''
		):
		\""" Represents the <{tag.lower()}> tag \"""
"""

	Path('html.py').write_text(code)
