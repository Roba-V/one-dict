import tkinter as tk
from tkinter import messagebox

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
            self.grid(column=0, row=0)
            self.create_widgets()

    def create_widgets(self) -> None:
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

        return master
