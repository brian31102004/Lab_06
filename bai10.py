import pandas as pd

data_nv = {
    "MaHD": ["HD01","HD02","HD03","HD04","HD05","HD06","HD07","HD08","HD09","HD10","HD11","HD12"],
    "NhanVien": ["An","Binh","Chi","An","Dung","Chi","An","Binh","Dung","Chi","An","Binh"],
    "SoLuong": [1,5,2,3,1,4,2,6,1,2,1,3],
    "DonGia": [14500000,150000,2500000,750000,900000,450000,300000,180000,2500000,900000,14500000,300000]
}
df_nv = pd.DataFrame(data_nv)
df_nv["DoanhThu"] = df_nv["SoLuong"] * df_nv["DonGia"]

# Gom nhóm và tính tổng
tong_nv = df_nv.groupby("NhanVien")["DoanhThu"].sum().reset_index()
tong_nv = tong_nv.sort_values(by="DoanhThu", ascending=False)

print("--- Tổng doanh thu theo nhân viên ---")
print(tong_nv)

# Nhận xét:
# Nhân viên An có doanh thu vượt trội (hơn 30 triệu) nhờ bán được các sản phẩm giá trị cao như Laptop.
# Nhân viên Binh có số lượng đơn hàng nhiều nhưng doanh thu thấp do bán các phụ kiện giá rẻ.