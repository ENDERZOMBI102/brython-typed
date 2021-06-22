from typing import Final, TypeVar, Union, Callable, Dict, Any, Literal, List, Type

from browser import DOMEvent, html

T = TypeVar('T')

ENUM_ELEMENT = Final[T]
EVENT_CALLBACK = Union[ Callable[ [], None ], Callable[ [DOMEvent], None ] ]
HTTP_HEADERS = Dict[ str, Union[str, int] ]
HTTP_DATA = Union[ str, Dict[ str, Any ] ]
RESPONSE_FORMAT = Literal['text', 'binary', 'dataURL']


class MessageEvent(DOMEvent):
	isTrusted: bool
	data: str
	origin: str
	lastEventId: str
	source: object
	ports: list
	userActivation: object
	type: str


# noinspection PyPropertyDefinition
class MouseEvent(DOMEvent):

	@property
	def button( self ) -> html.BUTTON:
		""" Indicates which button was pressed on the mouse to trigger the event. """

	@property
	def buttons( self ) -> int:
		"""
		Indicates which buttons were pressed on the mouse to trigger the event.
		Each button that can be pressed is represented by a given number (1 : Left button, 2 : Right button, 4 : Wheel button).
		If more than one button is pressed, the value of the buttons is combined to produce a new number.
		For example, if the right button (2) and the wheel button (4) are pressed, the value is equal to 2|4, which is 6
		"""

	@property
	def x( self ) -> int:
		"""	Position of the mouse relatively to the left border of the window (in pixels). """

	@property
	def y( self ) -> int:
		""" Position of the mouse relatively to the upper border of the window (in pixels). """

	@property
	def clientX( self ) -> int:
		""" The X coordinate of the mouse pointer in local (DOM content) coordinates. """

	@property
	def clientY( self ) -> int:
		""" The Y coordinate of the mouse pointer in local (DOM content) coordinates. """

	@property
	def screenX( self ) -> int:
		""" The X coordinate of the mouse pointer in global (screen) coordinates. """

	@property
	def screenY( self ) -> int:
		""" The Y coordinate of the mouse pointer in global (screen) coordinates. """


# noinspection PyPropertyDefinition
class KeyboardEvent(DOMEvent):

	@property
	def altKey( self ) -> bool:
		"""
		True if the Alt (or Option, on Mac) key was active when the key event was generated.
		\n
		This attribute is not set for the input event.
		\n
		It is usually used with keypress, to be able to test if Alt+<key> was entered, or just <key>.
		"""

	@property
	def charCode( self ) -> int:
		"""
		The Unicode reference number of the key
		\n
		This attribute is used only by the keypress event.
		\n
		It is set to a different value if the Shift key is pressed or not.
		"""

	@property
	def ctrlKey(self):
		"""
		True if the Control key was active when the key event was generated.
		\n
		This attribute is not set for the input event.
		\n
		It is usually used with keypress, to be able to test if Ctrl+<key> was entered, or just <key>.
		"""

	@property
	def keyCode(self) -> int:
		"""
		A system and implementation dependent numerical code identifying the unmodified value of the pressed key.
		\n
		The value doesn't change if the keys Alt, Ctrl or Shift are pressed.
		\n
		Note that the result is not the same depending on the handled events keydown, keyup or keypress.
		"""

	@property
	def shiftKey(self) -> bool:
		"""
		True if the Shift key was active when the key event was generated.
		\n
		This attribute is not set for the input event.
		\n
		It is usually used with keypress, to be able to test if Shift+<key> was entered, or just <key>.
		"""

	@property
	def which( self ) -> int:
		"""
		A system and implementation dependent numeric code identifying the unmodified value of the pressed key.
		\n
		Note that the result is not the same depending on the handled events keydown, keyup or keypress.
		"""


class FocusEvent(DOMEvent):
	pass


# noinspection PyPropertyDefinition
class _DataStore:

	@property
	def dropEffect( self ) -> Literal['copy', 'move', 'link', 'none']:
		"""
		A string representing the actual effect that will be used, and should always be one of the possible values of effectAllowed.
		For the dragenter and dragover events, the dropEffect will be initialized based on what action the user is requesting.
		How this is determined is platform specific, but typically the user can press modifier keys to adjust which action is desired.
		Within an event handler for the dragenter and dragover events, the dropEffect should be modified if the action the user is requesting is not the one that is desired.
		For dragstart, drag, and dragleave events, the dropEffect is initialized to "none".
		Any value assigned to the dropEffect will be set, but the value isn't used for anything.
		For the drop and dragend events, the dropEffect will be initialized to the action that was desired, which will be the value that the dropEffect had after the last dragenter or dragover event.
		\n
		Possible values:
		- "copy" : A copy of the source item is made at the new location.
		- "move" : An item is moved to a new location.
		- "link" : A link is established to the source at the new location.
		- "none" : The item may not be dropped.
		Assigning any other value has no effect and retains the old value.
		"""

	@dropEffect.setter
	def dropEffect( self, value: Literal['copy', 'move', 'link', 'none'] ):
		pass

	@property
	def effectAllowed( self ) -> str:
		"""
		A string that specifies the effects that are allowed for this drag.
		You may set this in the dragstart event to set the desired effects for the source, and within the dragenter and
		dragover events to set the desired effects for the target.
		\n
		The value is not used for other events.
		"""

	@property
	def files( self ) -> List:
		"""
		Contains a list of all the local files available on the data transfer.
		If the drag operation doesn't involve dragging files, this property is an empty list.
		An invalid index access on the file list specified by this property will return None.
		"""

	def getData( self, type: Type[T] ) -> T:
		"""
		Retrieves the data for a given type, or an empty string if data for that type does not
		exist or the data transfer contains no data.
		"""

	def setData( self, type: Type[T], value: T) -> None:
		"""
		Set the data for a given type.
		If data for the type does not exist, it is added at the end, such that the last item in the types list will be the new format.
		If data for the type already exists, the existing data is replaced in the same position.
		That is, the order of the types list is not changed when replacing data of the same type.
		"""

	@property
	def types( self ) -> List[type]:
		"""
		Holds a list of the format types of the data that is stored for the first item, in the same order the data was added.
		An empty list will be returned if no data was added.
		"""


class DragEvent:
	dataTransfer: _DataStore
