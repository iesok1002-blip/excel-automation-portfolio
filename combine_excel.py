import pandas as pd
import glob

target_path = "input_files/*.xlsx"

print("--- ファイルの検索開始 ---")
file_list = glob.glob(target_path)
print(f"見つかったファイル: {file_list}")

all_data_frames = []

for file_name in file_list:
    print(f"処理中のファイル: {file_name}")
    
    df = pd.read_excel(file_name)
    
    all_data_frames.append(df)

combined_df = pd.concat(all_data_frames, axis=0)

output_file = "summary_combined.xlsx"
combined_df.to_excel(output_file, index=False)

print("--- 処理完了 ---")
print(f"ファイル '{output_file}' を作成しました。")