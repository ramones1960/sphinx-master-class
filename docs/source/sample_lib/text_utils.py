"""テキスト処理モジュール。

autodoc と Napoleon ドキュメンテーションスタイルの実習用サンプル。
NumPy スタイルの docstring で記述している。

使用例::

    >>> from sample_lib.text_utils import TextProcessor
    >>> tp = TextProcessor()
    >>> tp.word_count("hello world")
    2
    >>> tp.to_title_case("hello world")
    'Hello World'
"""

from __future__ import annotations


class TextProcessor:
    """シンプルなテキスト処理クラス。

    文字列の分析・変換メソッドをまとめたユーティリティ。
    NumPy スタイルの docstring で記述している。

    Attributes
    ----------
    strip_whitespace : bool
        各メソッドの実行前に前後の空白を除去するかどうか（デフォルトは True）。

    Examples
    --------
    >>> tp = TextProcessor()
    >>> tp.word_count("Sphinx は強力なドキュメントツール")
    5
    """

    def __init__(self, strip_whitespace: bool = True) -> None:
        """TextProcessor を初期化する。

        Parameters
        ----------
        strip_whitespace : bool, optional
            処理前に前後の空白を除去するかどうか。デフォルトは True。
        """
        self.strip_whitespace = strip_whitespace

    def _prepare(self, text: str) -> str:
        """入力テキストを前処理する（内部ヘルパー）。"""
        return text.strip() if self.strip_whitespace else text

    def word_count(self, text: str) -> int:
        """テキスト中の単語数を返す。

        空白文字（スペース・タブ・改行）で分割してカウントする。

        Parameters
        ----------
        text : str
            カウント対象の文字列。

        Returns
        -------
        int
            単語数。空文字列の場合は 0。

        Examples
        --------
        >>> TextProcessor().word_count("hello world")
        2
        >>> TextProcessor().word_count("  spaces  ")
        1
        >>> TextProcessor().word_count("")
        0
        """
        return len(self._prepare(text).split()) if self._prepare(text) else 0

    def char_count(self, text: str, include_spaces: bool = True) -> int:
        """テキストの文字数を返す。

        Parameters
        ----------
        text : str
            カウント対象の文字列。
        include_spaces : bool, optional
            空白文字を含めてカウントするかどうか。デフォルトは True。

        Returns
        -------
        int
            文字数。

        Examples
        --------
        >>> TextProcessor().char_count("hello")
        5
        >>> TextProcessor().char_count("hello world", include_spaces=False)
        10
        """
        text = self._prepare(text)
        if not include_spaces:
            text = text.replace(" ", "").replace("\t", "").replace("\n", "")
        return len(text)

    def reverse(self, text: str) -> str:
        """テキストを逆順にして返す。

        Parameters
        ----------
        text : str
            逆順にする文字列。

        Returns
        -------
        str
            逆順にした文字列。

        Examples
        --------
        >>> TextProcessor().reverse("hello")
        'olleh'
        >>> TextProcessor().reverse("Sphinx")
        'xnihpS'
        """
        return self._prepare(text)[::-1]

    def to_title_case(self, text: str) -> str:
        """テキストをタイトルケース（各単語の先頭を大文字）に変換して返す。

        Parameters
        ----------
        text : str
            変換対象の文字列。

        Returns
        -------
        str
            タイトルケースに変換した文字列。

        Examples
        --------
        >>> TextProcessor().to_title_case("hello world")
        'Hello World'
        >>> TextProcessor().to_title_case("sphinx master class")
        'Sphinx Master Class'
        """
        return self._prepare(text).title()

    def truncate(self, text: str, max_length: int, ellipsis: str = "...") -> str:
        """テキストを指定の最大長に切り詰めて返す。

        切り詰めた場合は末尾に省略記号を付加する。

        Parameters
        ----------
        text : str
            切り詰め対象の文字列。
        max_length : int
            最大文字数（省略記号を含む）。0 以上の整数。
        ellipsis : str, optional
            省略記号。デフォルトは ``"..."``。

        Returns
        -------
        str
            最大長以下の文字列。

        Raises
        ------
        ValueError
            ``max_length`` が 0 未満のとき。

        Examples
        --------
        >>> TextProcessor().truncate("Hello, World!", 8)
        'Hello...'
        >>> TextProcessor().truncate("Hi", 10)
        'Hi'
        """
        if max_length < 0:
            raise ValueError(f"max_length must be >= 0, got {max_length}")
        text = self._prepare(text)
        if len(text) <= max_length:
            return text
        cut = max_length - len(ellipsis)
        return text[:max(cut, 0)] + ellipsis
