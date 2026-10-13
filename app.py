import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Tiêu đề Web App
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# #1. Tạo frame (Yêu cầu 1)
data = {
    "Ho_ten": ["An", "Bình", "Chi", "Dũng", "Hà", "Lan", "Minh", "Nam", "Phúc", "Trang"],
    "Chuyen_can": [8.5, 9.0, 7.0, 9.5, 8.0, 6.5, 9.0, 7.5, 8.0, 9.5],
    "Giua_ky": [7.5, 8.5, 6.5, 9.0, 7.0, 5.5, 8.5, 6.5, 7.5, 9.0],
    "Cuoi_ky": [8.0, 8.5, 6.5, 9.0, 7.5, 6.0, 8.5, 7.0, 7.5, 9.5]
}
df = pd.DataFrame(data)

# #2. Tính điểm tổng kết (Yêu cầu 2)
ds_tong_ket = []
for i in range(10):
    cc = df["Chuyen_can"][i]
    gk = df["Giua_ky"][i]
    ck = df["Cuoi_ky"][i]
    diem = round(cc * 0.2 + gk * 0.3 + ck * 0.5, 2)
    ds_tong_ket.append(diem)

df["Tong_ket"] = ds_tong_ket

# #3. Xếp loại sinh viên (Yêu cầu 3)
ds_xep_loai = []
for diem in df["Tong_ket"]:
    if diem >= 8.5:
        ds_xep_loai.append("Giỏi")
    elif diem >= 7.0:
        ds_xep_loai.append("Khá")
    elif diem >= 5.0:
        ds_xep_loai.append("Trung bình")
    else:
        ds_xep_loai.append("Yếu")

df["Xep_loai"] = ds_xep_loai

# Hiển thị Bảng điểm lên trang Web
st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(df)

# #4. Thống kê (Yêu cầu 4)
tong_diem = 0
so_sv_dat = 0
max_diem = df["Tong_ket"][0]
min_diem = df["Tong_ket"][0]
ten_max = df["Ho_ten"][0]
ten_min = df["Ho_ten"][0]

for i in range(10):
    diem = df["Tong_ket"][i]
    ten = df["Ho_ten"][i]
    tong_diem = tong_diem + diem
    
    if diem >= 5.0:
        so_sv_dat = so_sv_dat + 1
    if diem > max_diem:
        max_diem = diem
        ten_max = ten
    if diem < min_diem:
        min_diem = diem
        ten_min = ten

dtb_lop = round(tong_diem / 10, 2)

# Hiển thị kết quả Thống kê lên trang Web
st.subheader("Thông tin thống kê")
st.write("1. Điểm tổng kết trung bình của lớp:", dtb_lop)
st.write("2. Sinh viên có điểm cao nhất:", ten_max, "-", max_diem, "điểm")
st.write("3. Sinh viên có điểm thấp nhất:", ten_min, "-", min_diem, "điểm")
st.write("4. Số sinh viên đạt (>= 5.0):", so_sv_dat, "/ 10 sinh viên")

# Tra cứu sinh viên bằng Selectbox
st.subheader("Tra cứu thông tin sinh viên")
ten_chon = st.selectbox("Chọn một sinh viên:", df["Ho_ten"])

for i in range(10):
    if df["Ho_ten"][i] == ten_chon:
        st.write("• Điểm Chuyên cần:", df["Chuyen_can"][i])
        st.write("• Điểm Giữa kỳ:", df["Giua_ky"][i])
        st.write("• Điểm Cuối kỳ:", df["Cuoi_ky"][i])
        st.write("• Điểm Tổng kết:", df["Tong_ket"][i])
        st.write("• Xếp loại:", df["Xep_loai"][i])

# #5. Trực quan hóa (Yêu cầu 5)
st.subheader("Biểu đồ điểm tổng kết")
fig, ax = plt.subplots()
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("BIỂU ĐỒ ĐIỂM TỔNG KẾT CỦA 10 SINH VIÊN")
ax.set_xlabel("Tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
st.pyplot(fig)

# Thông tin người thực hiện ở cuối trang (chữ nhỏ)
st.write("---")
st.markdown("<p style='font-size: 12px; color: gray;'>Họ và tên: [Điền tên của bạn] | MSSV: [Điền MSSV của bạn]</p>", unsafe_allow_html=True)
