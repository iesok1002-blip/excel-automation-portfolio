import pandas as pd

input_file = "database.xlsx"
target_subject = "消耗品費"

print(f"--- 処理開始 ---")
print(f"読み込みファイル: {input_file}")

df = pd.read_excel(input_file)

filtered_df = df[df['勘定科目'] == target_subject]

if not filtered_df.empty:
    filtered_df['日付'] = filtered_df['日付'].dt.strftime('%Y/%m/%d')

output_file = "filtered_result.xlsx"
filtered_df.to_excel(output_file, index=False)

print(f"--- 処理完了 ---")
print(f"「{target_subject}」のデータだけを抽出し、'{output_file}' に保存しました。")