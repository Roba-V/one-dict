import tkinter as tk
import urllib.request
from urllib import parse
from tkinter import messagebox

import requests

from common.language import Language
from common import constants as cst


class App(tk.Frame):
    """
    アプリ GUI クラス。
    """

    def __init__(self):
        """
        アプリの起動処理。
        GUI ウィンドウ作成・アプリ初期化を行い、各種ウィジットを作成する。
        例外が発生した場合、エラーメッセージを表示し、アプリを終了させる。
        """

        # noinspection PyBroadException
        try:
            self.__init_app()
            self.master = self.__create_window(cst.SETTING_WINDOW_SIZE,
                                               Language.get('appName'))

            super().__init__(self.master)
        except Exception as e:
            # 例外が発生した場合、エラーメッセージを表示し、アプリを終了させる。
            # 主に言語ロード失敗した場合に使われる。
            self.master = self.__create_window()
            super().__init__(self.master)
            messagebox.showerror(cst.ERROR_MSG, str(e))
            self.master.destroy()
        else:
            # キーワード入力欄のリスト
            # <英語>,<日本語>,<中国語>
            self.keyword_txts = [tk.Text(self, width=32, height=10) for _ in
                                 range(3)]
            # 「翻訳」ボタン
            self.translate_btn = tk.Button(
                self, width=7, text=Language.get('translate'),
                command=self.__translate_handle, default="active")
            # 「クリア」ボタン
            self.clear_btn = tk.Button(
                self, width=7, text=Language.get('clear'),
                command=self.__clear_handle)
            # 「検索履歴」ラベル
            self.history_lbl = tk.Label(
                self, width=20, text=Language.get('history'), anchor='w')
            # 「検索履歴」コンテンツ
            self.history_msg = tk.Message(
                self, width=800, text="this\tthat\tinformation")

            self.put_widgets()

    def put_widgets(self) -> None:
        """
        各種のウィジェットをウィンドウ内に配置する。

        :return: None
        """

        self.grid(column=0, row=0)
        # キーワード入力欄を配置する。
        for idx, txt in enumerate(self.keyword_txts):
            txt.grid(column=idx, row=0, rowspan=5)
        # 「翻訳」ボタンを配置する。
        self.translate_btn.grid(column=3, row=0)
        # 「クリア」ボタンを配置する。
        self.clear_btn.grid(column=3, row=1)
        # 「検索履歴」ラベルを配置する。
        self.history_lbl.grid(column=0, row=6)
        # 「検索履歴」コンテンツを配置する。
        self.history_msg.grid(column=0, row=7, columnspan=4)

    def __translate_handle(self):

        # TODO: 別クラスに移動する。
        url = 'https://translate.google.co.jp/_/TranslateWebserverUi/data/batchexecute'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'f.req': '[[["MkEWBc","[[\\"information\\",\\"auto\\",\\"ja\\",true],[null]]",null,"generic"]]]'}
        data = urllib.parse.urlencode(data)
        r = requests.post(url=url, headers=headers, data=data)
        print(r.status_code)
        print(r.text)
        keyword = r.text

        self.keyword_txts[1].delete('1.0', 'end')
        self.keyword_txts[2].delete('1.0', 'end')
        self.keyword_txts[1].insert('1.0', keyword)
        self.keyword_txts[2].insert('1.0', keyword)

    def __clear_handle(self):
        pass

    @staticmethod
    def __init_app() -> None:
        """
        アプリを初期化する。

        :return: None
        """

        Language.config(cst.SETTING_DEFAULT_LANG)

    @staticmethod
    def __create_window(size: str = '', title: str = '') -> tk.Tk:
        """
        GUI ウィンドウインスタンスを作成し、戻り値として返す。
        引数なしの場合に、非表示のウィンドウインスタンスを作成する。

        :param size:    ウィンドウサイズ（<横幅>x<高さ>）
        :param title:   アプリ名称
        :return: Tk インスタンス
        """

        master = tk.Tk()

        if size:
            master.geometry(size)

        if title:
            master.title(title)

        if not size and not title:
            # アプリ名称もウィンドウサイズも設定しない場合に、
            # ウィンドウ自体を非表示にする。
            master.withdraw()

        master.resizable(False, False)

        return master
