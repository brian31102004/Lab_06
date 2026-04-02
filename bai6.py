import pandas as pd

from bai4 import xep_loai

df_tonghop = pd.read_csv("diem_sinhvien.csv")
df_tonghop["DiemTB"] = 0.4 * df_tonghop["DiemQT"] + 0.6 * df_tonghop["DiemThi"]
df_tonghop["XepLoai"] = df_tonghop["DiemTB"].apply(xep_loai) # Dùng lại hàm xep_loai ở Bài 4

# Lọc Khá trở lên và Sắp xếp giảm dần
ket_qua = df_tonghop[df_tonghop["XepLoai"].isin(["Gioi", "Kha"])]
ket_qua = ket_qua.sort_values(by="DiemTB", ascending=False)

# Lưu kết quả
ket_qua.to_csv("ketqua_xuly.csv", index=False, encoding="utf-8-sig")
print("--- Danh sách SV đạt loại Khá trở lên ---")
print(ket_qua)