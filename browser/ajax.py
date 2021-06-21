"""
This module allows running Ajax requests.

The standard Web API syntax can be used (see below) but Brython proposes a more concise syntax:
	for each request method (GET, POST, etc.) the module defines a specific function.
"""
from typing import Union, Literal, Dict, Callable, Any
from io import IOBase

from webtypes import HTTP_HEADERS, HTTP_DATA


AJAX_EVENTS = Literal['uninitialized', 'loading', 'loaded', 'interactive', 'complete', 'timeout']
AJAX_RESPONSE_TYPE = Literal['text', 'binary', 'json', 'document']
AJAX_UP_METHODS = Literal[ 'POST', 'PUT', 'PATCH' ]
AJAX_CALLBACKS = Dict[ AJAX_EVENTS, Callable[ [ 'Ajax' ], None ] ]


class _Ajax:
	status: int
	text: Union[str, bytes]
	json: Dict
	xml: Dict[str, Any]

	def read( self ) -> Union[str, bytes, dict]:
		""" Reads the response in the format determined by request mode. """


class Ajax:

	encoding: str
	responseType: AJAX_RESPONSE_TYPE

	def open(self, method, url: str, isasync: bool) -> None:
		"""
		\t
		:param method: The HTTP method used for the request (usually GET or POST).
		:param url: The resource location.
		:param isasync: A boolean that indicates whether the call is asynchronous (the script that started the request
		goes on running without waiting for the response) or not (the script hangs until the response is received).
		"""

	def bind(self, evt: AJAX_EVENTS, function: Callable[ [ _Ajax ], None ]) -> None:
		""" Attaches the function to the event evt. The events are the same as above. """

	def set_header(self, name: str, value: Any) -> None:
		""" Sets the value of the header name. """

	def set_timeout(self, duration, function) -> None:
		"""
		if the query did not return response within duration in seconds, it will cancel the query and execute the function.
		This function cannot have arguments.
		"""

	def send(self, data: HTTP_DATA = None):
		"""
		sends (starts) the request.
		The optional argument data is ignored if the method is not POST, PUT or PATCH; it must be a dictionary,
		or a string representing the url encoding of key-value pairs.

		If you want to send files, you need to pass a dictionary with one of the keys a File object,
		e.g. provided you have an input element of type file and id upload_file you could send the user
		selected file under the key upload by calling `send( { 'upload':doc["upload_file"].elt.files[0] } )`
		\t
		:param data: Optional data to send (ignored if method is not POST, PUT or PATCH)
		"""


def file_upload(
		url: str,
		file: IOBase,
		method: AJAX_UP_METHODS = 'POST',
		field_name: str = 'filetosave',
		**callbacks: AJAX_CALLBACKS
	) -> None:
	"""
	Uploads files to a server.
	\t
	:param file: File to upload
	:param url: URL to upload the file to
	:param method: The method used for the upload call, "POST" by default but can be set to "PUT"
	:param field_name: The name of the field associated with the file to send.
		It will be used on the server side to get the data.
	"""


# noinspection DuplicatedCode
def get(
		url: str,
		blocking: bool = False,
		headers: HTTP_HEADERS = {},
		mode: AJAX_RESPONSE_TYPE = 'text',
		encoding: str = 'utf-8',
		timeout: Union[None, int] = None,
		cache: bool = False,
		data: HTTP_DATA = '',
		**callbacks: AJAX_CALLBACKS
		) -> None:
	pass


# noinspection DuplicatedCode
def head(
		url: str,
		blocking: bool = False,
		headers: HTTP_HEADERS = {},
		mode: AJAX_RESPONSE_TYPE = 'text',
		encoding: str = 'utf-8',
		timeout: Union[None, int] = None,
		cache: bool = False,
		data: HTTP_DATA = '',
		**callbacks: AJAX_CALLBACKS
		) -> None:
	pass


# noinspection DuplicatedCode
def connect(
		url: str,
		blocking: bool = False,
		headers: HTTP_HEADERS = {},
		mode: AJAX_RESPONSE_TYPE = 'text',
		encoding: str = 'utf-8',
		timeout: Union[None, int] = None,
		cache: bool = False,
		data: HTTP_DATA = '',
		**callbacks: AJAX_CALLBACKS
		) -> None:
	pass


# noinspection DuplicatedCode
def options(
		url: str,
		blocking: bool = False,
		headers: HTTP_HEADERS = {},
		mode: AJAX_RESPONSE_TYPE = 'text',
		encoding: str = 'utf-8',
		timeout: Union[None, int] = None,
		cache: bool = False,
		data: HTTP_DATA = '',
		**callbacks: AJAX_CALLBACKS
		) -> None:
	pass


# noinspection DuplicatedCode
def delete(
		url: str,
		blocking: bool = False,
		headers: HTTP_HEADERS = {},
		mode: AJAX_RESPONSE_TYPE = 'text',
		encoding: str = 'utf-8',
		timeout: Union[None, int] = None,
		cache: bool = False,
		data: HTTP_DATA = '',
		**callbacks: AJAX_CALLBACKS
		) -> None:
	pass


# noinspection DuplicatedCode
def patch(
		url: str,
		blocking: bool = False,
		headers: HTTP_HEADERS = {},
		mode: AJAX_RESPONSE_TYPE = 'text',
		encoding: str = 'utf-8',
		timeout: Union[None, int] = None,
		cache: bool = False,
		data: HTTP_DATA = '',
		**callbacks: AJAX_CALLBACKS
		) -> None:
	pass


# noinspection DuplicatedCode
def post(
		url: str,
		blocking: bool = False,
		headers: HTTP_HEADERS = {},
		mode: AJAX_RESPONSE_TYPE = 'text',
		encoding: str = 'utf-8',
		timeout: Union[None, int] = None,
		cache: bool = False,
		data: HTTP_DATA = '',
		**callbacks: AJAX_CALLBACKS
		) -> None:
	pass


# noinspection DuplicatedCode
def put(
		url: str,
		blocking: bool = False,
		headers: HTTP_HEADERS = {},
		mode: AJAX_RESPONSE_TYPE = 'text',
		encoding: str = 'utf-8',
		timeout: Union[None, int] = None,
		cache: bool = False,
		data: HTTP_DATA = '',
		**callbacks: AJAX_CALLBACKS
		) -> None:
	pass


# noinspection DuplicatedCode
def trace(
		url: str,
		blocking: bool = False,
		headers: HTTP_HEADERS = {},
		mode: AJAX_RESPONSE_TYPE = 'text',
		encoding: str = 'utf-8',
		timeout: Union[None, int] = None,
		cache: bool = False,
		data: HTTP_DATA = '',
		**callbacks: AJAX_CALLBACKS
		) -> None:
	pass
