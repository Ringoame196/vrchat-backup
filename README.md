# VRChat Photo Auto-Sync Tool

VRChatのスクリーンショット（PNG）を、NASや外部ストレージへ自動バックアップするPythonスクリプトです。

## 特徴
- 当月および前月分のフォルダのみを対象にして高速処理
- NAS側に変換済み（WebP等）の同名ファイルが存在する場合、自動で重複をスキップ
- Windows環境の絶対パスに対応

## 使用技術
- Python 3.x (pathlib, shutil, datetime)
