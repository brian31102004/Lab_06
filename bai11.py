import pandas as pd

data_kho = {
    "MaSP": ["SP01","SP02","SP03","SP04","SP05","SP06"],
    "TenSP": ["Laptop","Chuot","Ban phim","USB","Loa","Webcam"],
    "TonDau": [5, 20, 15, 30, 10, 8],
    "NhapThem": [3, 10, 5, 20, 4, 2],
    "DaBan": [4, 18, 12, 35, 9, 3],
    "DonGia": [14500000,150000,300000,180000,750000,900000]
}
df_kho = pd.DataFrame(data_kho)

df_kho["TonCuoi"] = df_kho["TonDau"] + df_kho["NhapThem"] - df_kho["DaBan"]
df_kho["GiaTriTonCuoi"] = df_kho["TonCuoi"] * df_kho["DonGia"]

print("--- Báo cáo kho hàng ---")
print(df_kho)

# Tìm SP tồn cao nhất bằng idxmax
sp_max_ton = df_kho.loc[df_kho["GiaTriTonCuoi"].idxmax()]
print(f"\nSản phẩm có giá trị tồn cao nhất là: {sp_max_ton['TenSP']} ({sp_max_ton['GiaTriTonCuoi']:,} VND)")