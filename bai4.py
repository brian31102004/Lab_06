import pandas as pd

df = pd.read_csv("diem_sinhvien.csv")

# 1. Tính DiemTB
df["DiemTB"] = 0.4 * df["DiemQT"] + 0.6 * df["DiemThi"]

# 2. Hàm phân loại Xếp loại
def xep_loai(diem):
    if diem >= 8.5: return "Gioi"
    elif diem >= 7.0: return "Kha"
    elif diem >= 5.5: return "Trung binh"
    else: return "Yeu"

df["XepLoai"] = df["DiemTB"].apply(xep_loai)

# 3. Lọc SV có điểm >= 8
print("--- SV có DiemTB >= 8 ---")
print(df[df["DiemTB"] >= 8])

# 4. Đổi tên cột và đặt MaSV làm index
df = df.rename(columns={"HoTen": "TenSinhVien"})
df = df.set_index("MaSV")

print("\n--- DataFrame sau khi định dạng lại ---")
print(df)