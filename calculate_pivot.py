import pandas as pd
import numpy as np

input_file = "database.xlsx"

print(f"--- 処理開始 ---")
print(f"読み込みファイル: {input_file}")

df = pd.read_excel(input_file)

pivot_df = pd.pivot_table(df, 
                          index='勘定科目', 
                          columns='支店', 
                          values='金額', 
                          aggfunc='sum',
                          fill_value=0)

output_file = "pivot_result.xlsx"
pivot_df.to_excel(output_file)

print(f"--- 処理完了 ---")
print(f"ピボットテーブルを '{output_file}' に保存しました。")