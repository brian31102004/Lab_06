import pandas as pd

data_survey = {
    "MaSV": ["SV01","SV02","SV03","SV04","SV05","SV06","SV07","SV08","SV09","SV10"],
    "GioTuHoc": [3, 2, 1, 4, 2.5, 1.5, 3.5, 2, 1, 4],
    "SoBuoiNghi": [1, 2, 4, 0, 1, 3, 0, 2, 5, 1],
    "DiemCC": [9, 8, 6, 10, 8, 6, 9, 8, 5, 10],
    "DiemCuoiKy": [8, 7.5, 6, 9, 8, 6.5, 8.5, 7, 5.5, 9]
}
df_survey = pd.DataFrame(data_survey)
df_survey["DiemTB"] = 0.3 * df_survey["DiemCC"] + 0.7 * df_survey["DiemCuoiKy"]

# Phân nhóm học tập dựa trên nhiều cột (axis=1)
def nhom_hoc_tap(row):
    if row["GioTuHoc"] >= 3 and row["SoBuoiNghi"] <= 1:
        return "Tich cuc"
    elif row["GioTuHoc"] >= 2 and row["SoBuoiNghi"] <= 2:
        return "Binh thuong"
    else:
        return "Can ho tro"

df_survey["NhomHocTap"] = df_survey.apply(nhom_hoc_tap, axis=1)

print("--- Kết quả khảo sát học tập ---")
print(df_survey)

# Lọc SV tự học > 2h và nghỉ <= 2 buổi
print("\n--- Nhóm sinh viên tiềm năng ---")
print(df_survey[(df_survey["GioTuHoc"] > 2) & (df_survey["SoBuoiNghi"] <= 2)])

# NHẬN XÉT:
# 1. Có sự tỷ lệ thuận rõ rệt giữa giờ tự học và điểm số cuối kỳ.
# 2. Những sinh viên thuộc nhóm 'Tich cuc' đều có điểm trung bình từ 8.3 trở lên.
# 3. Việc nghỉ học nhiều (SV03, SV09) ảnh hưởng trực tiếp đến cả điểm chuyên cần và kết quả thi.
# 4. Nhóm 'Can ho tro' chiếm khoảng 30% danh sách, cần có biện pháp nhắc nhở về giờ tự học.