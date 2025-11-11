import pandas as pd

input_file = "database.xlsx"

print(f"--- 処理開始 ---")
print(f"読み込みファイル: {input_file}")

df = pd.read_excel(input_file)

grouped_df = df.groupby('勘定科目')['金額'].sum().reset_index()

output_file = "groupby_result.xlsx"
grouped_df.to_excel(output_file, index=False)

print(f"--- 処理完了 ---")
print(f"勘定科目ごとの合計金額を '{output_file}' に保存しました。")