"""サンプルライブラリ。

autodoc 実習用の Python パッケージ。
第7章の演習で使用する。
"""

from .calculator import Calculator
from .text_utils import TextProcessor

__version__ = "1.0.0"
__all__ = ["Calculator", "TextProcessor"]
