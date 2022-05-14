"""
アプリの独自の例外を定義する。
"""


class ODLanguageError(Exception):
    """
    言語エラー
    """

    pass


class ODFileIOError(Exception):
    """
    ファイル IO エラー
    """

    pass
