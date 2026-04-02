import pandas as pd

df_csv = pd.read_csv("diem_sinhvien.csv")

print("--- 5 dòng đầu ---\n", df_csv.head())
print("\n--- 5 dòng cuối ---\n", df_csv.tail())
print("\n--- Thông tin dữ liệu ---")
df_csv.info()
print("\n--- Thống kê mô tả ---\n", df_csv.describe())
print("\nKích thước dữ liệu:", df_csv.shape)
print("Danh sách cột:", df_csv.columns.tolist())