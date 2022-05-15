import json
import os
import os.path

from common import constants as cst
from common.exceptions import ODLanguageError


class Language:
    """
    言語管理クラス。
    """

    # 言語設定済みかフラグ
    __is_configured: bool = False
    # 言語種類
    __lang: str = ''
    # メッセージ
    __msg: dict = {}

    @classmethod
    def config(cls, lang: str) -> None:
        """
        言語設定及び読み込みを行う。

        :param lang:    言語種類
        :return:        None
        """
        """手動初期化処理.

        Args:
            lang (str): 言語コード

        Raises:
            exception: 言語パッケージファイルが見つからないエラー.
        """
        try:
            cls.__lang = lang
            cls.__read_json()
        except Exception:
            exception = ODLanguageError(cst.LANG_LOAD_ERR_MSG)
            # TODO: ログ処理を追加

            raise exception
        else:
            cls.__is_configured = True

    @classmethod
    def __read_json(cls) -> None:
        """
        言語 JSON ファイルからメッセージを読み込む。

        :return: None
        """

        # TODO: 開発のために、カレントディレクトリ配下をまず見るように
        file_path = cst.LANG_JSON_FILE_PATH.format(
            os.path.expanduser('~'), cls.__lang
        )
        with open(file_path, 'r') as f:
            cls.__msg = json.loads(f.read())

    @classmethod
    def get(cls, code: str) -> str:
        """
        メッセージを取得する。

        :param      code: メッセージコード
        :return:    指定されたメッセージコードに対応したメッセージテキスト
        """

        if not cls.__is_configured:
            # 言語設定未実施の場合
            raise ODLanguageError(cst.LANG_HAS_NOT_CONFIGURED_MSG)
        return cls.__msg.get(code, '')
