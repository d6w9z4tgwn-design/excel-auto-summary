# Excel Auto Summary

Excelデータを指定したカテゴリで集計し、件数・合計・平均を新しいExcelファイルに書き出すツールです。手作業のピボット集計を、再実行可能なコマンドに置き換えます。

## 主な機能

- カテゴリ列ごとの件数、合計、平均を自動集計
- 金額などの数値列を検証し、不正な値を早期に検出
- 入力ファイルを上書きしない安全な出力設計

## セットアップ
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## 使い方

`python app.py input.xlsx summary.xlsx --group category --value amount` を実行します。`category` と `amount` は入力Excelの列名に置き換えてください。集計結果は、グループ列・`count`・`sum`・`mean` の列を持つ新規ファイルとして保存されます。

Python 3.10+ 推奨。
