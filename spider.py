import re
import urllib.parse

import requests


class Spider:
    """
    Google 翻訳をクローリングするためのスパイダー
    """

    def __init__(self, keyword: str, lang: str):
        """
        スパイダーの各種初期化処理を行う。
        """

        self.keyword = keyword
        self.url = 'https://translate.google.co.jp/_/TranslateWebserverUi/' \
                   'data/batchexecute'
        self.header = {'Content-Type': 'application/x-www-form-urlencoded'}
        # 翻訳用のフォームデータ
        f_req = f'[[["MkEWBc","[[\\"{keyword}\\",\\"auto\\",' \
                f'\\"{lang}\\",true],[null]]",null,"generic"]]]'
        self.data = urllib.parse.urlencode({'f.req': f_req})

    def translate(self) -> str:
        """
        翻訳を行う。

        :return: 翻訳結果
        """

        response = requests.post(self.url, self.data, headers=self.header)
        m = re.search(rf'{self.keyword}' + r'[^\[]*\[{3}[^\[]*\[{2}\\"(.*?)\\"',
                      response.text)

        return m.groups()[0]
