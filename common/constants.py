"""
アプリの定数を定義する。
"""

# ウィンドウサイズ（<横幅>x<高さ>）
SETTING_WINDOW_SIZE: str = '800x600'
# デフォルト言語種別
SETTING_DEFAULT_LANG: str = 'ja'

# エントリファイル名称
MAIN: str = '__main__'

# エラーメッセージ
ERROR_MSG: str = 'Error!'

# 言語ファイルパス
LANG_JSON_FILE_PATH: str = '{}/languages/{}.json'
# 言語エラーメッセージ：ロード失敗
LANG_LOAD_ERR_MSG: str = 'Unable to load language Resource!'
# 言語エラーメッセージ：言語設定未実施
LANG_HAS_NOT_CONFIGURED_MSG: str = 'Please configure the language first!'
