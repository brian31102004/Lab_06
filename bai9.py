import pandas as pd

data_kh = {
    "MaKH": ["KH01","KH02","KH03","KH04","KH05","KH06","KH07","KH08"],
    "TenKH": ["Lan","Minh","Hung","Ha","Phuong","Toan","Ngoc","Tuan"],
    "SoDonHang": [12, 5, 8, 15, 4, 10, 6, 3],
    "TongChiTieu": [25000000, 7200000, 12500000, 31000000, 4300000, 9800000, 15000000, 2800000]
}
df_kh = pd.DataFrame(data_kh)

def xep_loai_kh(tien):
    if tien >= 20000000: return "VIP"
    elif tien >= 10000000: return "Than thiet"
    elif tien >= 5000000: return "Tiem nang"
    else: return "Thuong"

df_kh["XepLoaiKH"] = df_kh["TongChiTieu"].apply(xep_loai_kh)

print("--- Khách hàng VIP & Thân thiết ---")
print(df_kh[df_kh["XepLoaiKH"].isin(["VIP", "Than thiet"])])
print("\nChi tiêu trung bình:", df_kh["TongChiTieu"].mean())