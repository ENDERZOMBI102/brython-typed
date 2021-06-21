"""
This module extends local_storage and session_storage by allowing keys and values to be Python objects, not just strings.
To achieve this, the object is serialised; currently only JSON serializable objects are supported, such as as a list or dict.
Also note that objects become immutable once they are stored, so ObjecStorage()['foo'].update({"bar": "zoo"}) won't actually do anything.
"""
from typing import Union, Any

from browser.local_storage import _LocalStorage
from browser.session_storage import _SessionStorage


class ObjectStorage:

	def __init__(self, storage: Union[_SessionStorage, _LocalStorage] ):
		pass

	def __getitem__(self, item: Any) -> Union[dict, list]:
		""" RETURNED VALUES ARE IMMUTABLE """

	def __setitem__( self, key: Any, value: Union[dict, list] ) -> None:
		pass