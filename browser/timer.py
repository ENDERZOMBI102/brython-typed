"""
Implements methods to allow differed or repetitive execution of functions
"""
from typing import Callable


class _Timer:
	pass


def set_timeout(function: Callable, ms: int, *args) -> _Timer:
	"""
	uns function(*args) after ms milliseconds.
	Returns an object usable in the function clear_timeout()
	\t
	:param function: Function to call.
	:param ms: Milliseconds before the function is called.
	"""


def clear_timeout(timer: _Timer) -> None:
	"""
	cancels the execution of the function defined by set_timeout().
	It receives an argument, the id value returned by the set_timeout() call.
	\t
	:param timer: _Timer object returned by set_timeout().
	"""


class _Interval:
	pass


def set_interval(function: Callable, ms: int, *args) -> _Interval:
	"""
	Launches repeated execution of function(*args) every ms milliseconds and returns an object usable in function
	clear_interval described below.
	It is a wrapper of the setInterval function in javascript. Official docs can be found here.
	When possible, you should avoid the use of this function and use request_animation_frame (see below) as
	an alternative.
	\t
	:param function: Function to call.
	:param ms: Milliseconds before the function is called.
	"""


def clear_interval(timer: _Interval) -> None:
	"""
	Stops the repeated execution of the function defined by set_interval().
	\t
	:param timer: _Interval object returned by set_interval().
	"""


class _ReqAnimFrame:
	pass


def request_animation_frame(function: Callable) -> _ReqAnimFrame:
	"""
	Runs the function repeatedly letting the browser be in charge to update the browser.
	function uses a fake argument
	"""


def cancel_animation_frame(id: _ReqAnimFrame) -> None:
	"""
	Cancels the repeated execution of the function defined by request_animation_frame() and uses the value returned
	by request_animation_frame() as id.
	\t
	:param id: Object returned by request_animation_frame().
	"""