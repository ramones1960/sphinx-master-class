# Napoleon スタイル Docstring

Sphinx 標準の docstring 形式は記述が複雑ですが、
`sphinx.ext.napoleon` 拡張を使うと **Google / NumPy スタイル**で書けます。

## Google スタイル（このプロジェクトで使用）

```python
def divide(a: float, b: float) -> float:
    """ふたつの数の商を返す。

    Args:
        a: 割られる数（被除数）。
        b: 割る数（除数）。ゼロは不可。

    Returns:
        a を b で割った商。

    Raises:
        ZeroDivisionError: b が 0 のとき。

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 0)
        Traceback (most recent call last):
            ...
        ZeroDivisionError: b must not be zero
    """
    if b == 0:
        raise ZeroDivisionError("b must not be zero")
    return a / b
```

## NumPy スタイル

```python
def power(base: float, exp: int) -> float:
    """べき乗を計算する。

    Parameters
    ----------
    base : float
        底の数。
    exp : int
        指数。

    Returns
    -------
    float
        base の exp 乗。
    """
    return base ** exp
```

## クラスの docstring

```python
class Calculator:
    """シンプルな四則演算クラス。

    小数点演算もサポートする。誤差は float の端数指定に依存する。

    Attributes:
        precision (int): 四捨五入の桁数。デフォルトは 10。

    Example:
        >>> calc = Calculator(precision=4)
        >>> calc.add(0.1, 0.2)
        0.3
    """

    def __init__(self, precision: int = 10):
        """Calculator を初期化する。

        Args:
            precision: 四捨五入の桁数。デフォルトは 10。
        """
        self.precision = precision
```

## conf.py の設定

```python
napoleon_google_docstring = True   # Google スタイルを有効化
napoleon_numpy_docstring  = True   # NumPy スタイルを有効化
napoleon_use_param  = True         # :param: 形式で出力
napoleon_use_rtype  = True         # :rtype: 形式で出力
```
