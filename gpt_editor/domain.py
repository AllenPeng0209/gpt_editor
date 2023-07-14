from typing import Callable, List, TypeVar

from gpt_editor.ai import AI
from gpt_editor.db import DBs

Step = TypeVar("Step", bound=Callable[[AI, DBs], List[dict]])
