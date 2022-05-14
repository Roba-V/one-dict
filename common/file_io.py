from typing import List

from common.exceptions import ODFileIOError
from common import Language


class FileIO:
    """
    ファイル入出力管理クラス。
    """

    @staticmethod
    def read_file_by_line(file_name: str) -> List[str]:
        """
        ファイルを読み込む、「\n」で区切ってリストで返す。

        :param file_name:   読み込むファイル名
        :return:            ファイル内容を行区切りでリストに格納し返却する。
        """

        try:
            with open(file_name, 'r') as f:
                return f.read().strip().split('\n')
        except Exception:
            raise ODFileIOError(Language.get('fileReadErr').format(file_name))

    @staticmethod
    def write_file_by_line(file_name: str, content: str) -> None:
        """
        ファイルに書き出し、「\n」で終わる。

        :param file_name:   書き出し先のファイル名
        :param content:     書き出す内容
        :return:            None
        """

        try:
            with open(file_name, 'a') as f:
                f.write(content + '\n')
        except Exception:
            raise ODFileIOError(Language.get('fileWriteErr').format(file_name))
