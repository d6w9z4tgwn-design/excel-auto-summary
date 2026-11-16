# excel-auto-summary

Excelのカテゴリ別集計を新規ファイルへ出力。

Group and summarize Excel data.

## Setup / 起動
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py --help
python -m unittest -v
```

## Usage / 使用例
`python app.py input.xlsx summary.xlsx --group category --value amount`

Python 3.10+ recommended. AI-generated development assistance was used.
