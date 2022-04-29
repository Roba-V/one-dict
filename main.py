"""
One Dict 辞書のエントリファイル
"""

from app import App
from common import constants as cst
from common.language import Language

if __name__ == cst.MAIN:
    app = App(Language.get('appName'), cst.SETTING_WINDOW_SIZE)
    app.mainloop()
