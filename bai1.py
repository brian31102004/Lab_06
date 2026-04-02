import pandas as pd

# Tạo Series điểm của 5 sinh viên
diem = pd.Series(
    [7.5, 8.0, 6.5, 9.0, 8.5],
    index=["SV01", "SV02", "SV03", "SV04", "SV05"]
)

print("--- Toàn bộ Series ---")
print(diem)
print("\nHai phần tử đầu:\n", diem.head(2))
print("\nĐiểm lớn nhất:", diem.max())
print("Điểm trung bình:", diem.mean())
print("\nSinh viên có điểm >= 8:\n", diem[diem >= 8])