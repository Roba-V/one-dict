import tkinter as tk


class App(tk.Frame):
    """
    アプリ GUI クラス。
    """

    def __init__(self, title: str, size: str):
        """
        GUI ウィンドウを作成し、アプリクラスを初期化し、
        各種ウィジットを作成する。

        :param title:   アプリ名称
        :param size:    ウィンドウサイズ（<横幅>x<高さ>）
        """

        self.master = self.__create_window(title, size)

        super().__init__(self.master)

        self.create_widgets()

    @staticmethod
    def __create_window(title: str, size: str) -> tk.Tk:
        """
        GUI ウィンドウを作成し、そのインスタンスを戻り値として返す。

        :param title:   アプリ名称
        :param size:    ウィンドウサイズ（<横幅>x<高さ>）
        :return: Tk インスタンス
        """

        master = tk.Tk()
        master.title(title)
        master.geometry(size)

        return master

    def create_widgets(self) -> None:
        pass
