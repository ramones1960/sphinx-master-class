"""四則演算モジュール。

autodoc と Napoleon ドキュメンテーションスタイルの実習用サンプル。
Google スタイルの docstring で記述している。

使用例::

    >>> from sample_lib.calculator import Calculator
    >>> calc = Calculator()
    >>> calc.add(1, 2)
    3
    >>> calc.divide(10, 4)
    2.5
"""

from __future__ import annotations


class Calculator:
    """シンプルな四則演算クラス。

    整数および浮動小数点演算に対応する。
    ゼロ除算や負の平方根に対しては適切な例外を発生させる。

    Attributes:
        precision (int): 小数以下の桁数（デフォルトは 10）。

    Example:
        >>> calc = Calculator(precision=4)
        >>> calc.add(1.1, 2.2)
        3.3
    """

    def __init__(self, precision: int = 10) -> None:
        """Calculator を初期化する。

        Args:
            precision: 結果を四捨五入する小数以下の桁数。デフォルトは 10。
        """
        if precision < 0:
            raise ValueError(f"precision must be >= 0, got {precision}")
        self.precision = precision

    def add(self, a: float, b: float) -> float:
        """二つの数の和を返す。

        Args:
            a: 加数。
            b: 加数。

        Returns:
            a + b の値。

        Example:
            >>> Calculator().add(1, 2)
            3
            >>> Calculator().add(0.1, 0.2)  # doctest: +SKIP
            0.3
        """
        return round(a + b, self.precision)

    def subtract(self, a: float, b: float) -> float:
        """二つの数の差を返す。

        Args:
            a: 被減数。
            b: 減数。

        Returns:
            a - b の値。
        """
        return round(a - b, self.precision)

    def multiply(self, a: float, b: float) -> float:
        """二つの数の積を返す。

        Args:
            a: 被乗数。
            b: 乗数。

        Returns:
            a * b の値。
        """
        return round(a * b, self.precision)

    def divide(self, a: float, b: float) -> float:
        """二つの数の商を返す。

        Args:
            a: 被除数。
            b: 除数。ゼロは不可。

        Returns:
            a / b の値。

        Raises:
            ZeroDivisionError: b が 0 のとき。

        Example:
            >>> Calculator().divide(10, 4)
            2.5
            >>> Calculator().divide(1, 0)
            Traceback (most recent call last):
                ...
            ZeroDivisionError: 除数は 0 にできません
        """
        if b == 0:
            raise ZeroDivisionError("除数は 0 にできません")
        return round(a / b, self.precision)

    def power(self, base: float, exp: int) -> float:
        """べき乗を計算する。

        Args:
            base: 底の数。
            exp: 指数。負の値も可。

        Returns:
            base の exp 乗。

        Example:
            >>> Calculator().power(2, 10)
            1024
            >>> Calculator().power(2, -1)
            0.5
        """
        return round(base ** exp, self.precision)

    def sqrt(self, n: float) -> float:
        """平方根を計算する。

        Args:
            n: 平方根を計算する数。0 以上の実数。

        Returns:
            n の平方根。

        Raises:
            ValueError: n が負の数のとき。

        Example:
            >>> Calculator().sqrt(9)
            3.0
            >>> Calculator().sqrt(-1)
            Traceback (most recent call last):
                ...
            ValueError: 負の数の平方根は計算できません
        """
        import math
        if n < 0:
            raise ValueError("負の数の平方根は計算できません")
        return round(math.sqrt(n), self.precision)
