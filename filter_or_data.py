import pandas as pd

input_file = "database.xlsx"
target_subject1 = "交際費"
target_subject2 = "消耗品費"

print(f"--- 処理開始 ---")
print(f"読み込みファイル: {input_file}")

df = pd.read_excel(input_file)

condition1 = (df['勘定科目'] == target_subject1)

condition2 = (df['勘定科目'] == target_subject2)

filtered_df = df[condition1 | condition2]

if not filtered_df.empty:
    filtered_df['日付'] = filtered_df['日付'].dt.strftime('%Y/%m/%d')

output_file = "filtered_or_result.xlsx"
filtered_df.to_excel(output_file, index=False)

print(f"--- 処理完了 ---")
print(f"「{target_subject1}」または「{target_subject2}」のデータを抽出し、'{output_file}' に保存しました。")