# DICOM-ID-EDITOR
This is a simple tool for editing the ID and Name in DICOM data.

DICOMのIDと名前のみを編集するシンプルなツールです。研究用途の匿名加工処理に使用できるように作成しました。
類似のツールは沢山ありますが、余計な機能を排除した使い易さを目的としています。


## 機能

- **読み込み**: `読み込み`ボタンをクリックすることで、DICOMファイルから患者情報（ID、名前、撮像時期）を読み込みます。
- **編集**: 読み込んだIDと名前を直接編集できます。
- **更新**: `更新`ボタンを押すと、編集内容がDICOMファイルに反映されます。

## 使用方法

1. `読み込み`ボタンをクリックし、DICOMファイルを選択します。
2. 表示された患者情報（ID、名前、撮像時期）を確認し、必要に応じて編集します。
3. `更新`ボタンを押し、変更を保存したいディレクトリを指定します。
4. 指定したディレクトリに更新されたDICOMファイルが保存されます。

<img width="262" alt="IDeditor" src="https://github.com/nyk3151/DICOM-ID-EDITOR/assets/63529023/f1724066-192b-4457-94b1-1b377bcb6e29">


上記の画像は、DICOM ID EDITORのユーザーインターフェイスです。ID、名前を簡単に編集できます。　

## 注意
- `読み込み`と`更新`の際にはDICOMファイルが含まれている直上のフォルダのパスを指定してください。
- データサイズが大きいと`読み込み`と`更新`は一定の時間（30秒～50秒程度）かかる場合があります。
- 完了する前に、何らかの操作をするとエラーが出現する可能性があります。　


