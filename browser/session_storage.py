"""
This module also exposes the object storage, which provides access to the session storage.
It is otherwise the same as the local_storage.
Use session_storage when you do not wish data to be shared across browser sessions or tabs.
A typical use case is a log-in token.
"""


from typing import Dict, List, Tuple


class _SessionStorage( Dict[str, str] ):

	def keys(self) -> List[str]:
		pass

	def values(self) -> List[str]:
		pass

	def items(self) -> List[ Tuple[str, str] ]:
		pass


storage: _SessionStorage
