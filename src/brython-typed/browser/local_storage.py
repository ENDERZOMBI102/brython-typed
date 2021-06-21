"""
This module exposes a single object, storage, which gives acces to the local storage.
You can interact with it like a dictionary, however, keep in mind that keys and values are restricted to strings.
"""


from typing import Dict, List, Tuple


class _LocalStorage( Dict[str, str] ):

	def keys(self) -> List[str]:
		pass

	def values(self) -> List[str]:
		pass

	def items(self) -> List[ Tuple[str, str] ]:
		pass


storage: _LocalStorage
