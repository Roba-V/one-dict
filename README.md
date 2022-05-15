# One Dict

Python をの基本を覚えるために作成したシンプルな辞書アプリである。

## dmg ファイル作成

```shell
pyinstaller --onefile --windowed main.py -n One-Dict
cd dist
dmgbuild -s ../settings.py -D app=One-Dict.app "My Application" One-Dict.dmg
```
