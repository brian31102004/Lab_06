import pandas as pd

data_sp = {
    "MaSP": ["SP01", "SP02", "SP03", "SP04", "SP05", "SP06", "SP07", "SP08"],
    "TenSP": ["Chuot", "Ban phim", "Man hinh", "USB", "Laptop", "Loa", "Tai nghe", "Webcam"],
    "LoaiHang": ["Phu kien", "Phu kien", "Thiet bi", "Phu kien", "Thiet bi", "Thiet bi", "Phu kien", "Thiet bi"],
    "DonGia": [150000, 300000, 2500000, 180000, 14500000, 750000, 450000, 900000],
    "SoLuongTon": [25, 18, 7, 40, 5, 12, 20, 8]
}
df_sp = pd.DataFrame(data_sp)

# Tính giá trị tồn kho
df_sp["GiaTriTonKho"] = df_sp["DonGia"] * df_sp["SoLuongTon"]

print("--- Sản phẩm đơn giá > 500,000 ---")
print(df_sp[df_sp["DonGia"] > 500000])

print("\n--- Sắp xếp theo giá trị tồn kho giảm dần ---")
print(df_sp.sort_values(by="GiaTriTonKho", ascending=False))

print("\n--- Sản phẩm sắp hết hàng (SL < 10) ---")
print(df_sp[df_sp["SoLuongTon"] < 10])