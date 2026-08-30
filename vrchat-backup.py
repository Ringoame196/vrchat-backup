import datetime
from pathlib import Path
import shutil

# 本日の日付を取得
today = datetime.date.today()

# 1. 今月と先月の YYYY-MM を取得
this_month = today.strftime("%Y-%m")
first_day_of_this_month = today.replace(day=1)
last_day_of_last_month = first_day_of_this_month - datetime.timedelta(days=1)
last_month = last_day_of_last_month.strftime("%Y-%m")

# パスの定義
SRC_DIR = Path(r"D:\デフォルトファイル\ピクチャ\VRChat")
BASE_DIR = Path(r"Z:\個人用K\photos\VRChat")

# 対象とする年月のペア（今月と先月）
target_months = [this_month, last_month]

copied_count = 0

for ym in target_months:
    src_month_dir = SRC_DIR / ym
    dst_month_dir = BASE_DIR / ym

    # 転送元の年月フォルダが存在しない場合はスキップ
    if not src_month_dir.exists():
        print(f"[スキップ] 転送元フォルダが存在しません: {src_month_dir}")
        continue

    # 転送先フォルダが存在しなければ作成
    dst_month_dir.mkdir(parents=True, exist_ok=True)

    # 転送元の画像（.png）をスキャン
    for file_path in src_month_dir.glob("*.png"):
        base_name = file_path.stem  # 拡張子を除いたファイル名

        # NAS側に同名ファイル（WebPなどの別拡張子を含む）が存在するかチェック
        matching_files = list(dst_month_dir.glob(f"{base_name}.*"))

        # NASに存在しない場合のみコピーを実行
        if not matching_files:
            shutil.copy2(file_path, dst_month_dir / file_path.name)
            print(f" [転送完了] {file_path.name} -> {ym}")
            copied_count += 1

if copied_count == 0:
    print("[情報] 新しく転送する画像はありませんでした。")
else:
    print(f"[完了] 合計 {copied_count} 件の画像を転送しました。")