
import streamlit as st
import math

st.title("Tính diện tích hình tròn")

# Nhập bán kính
r = st.number_input("Nhập bán kính hình tròn", min_value=0.0, format="%.2f")

# Tính diện tích
dien_tich = math.pi * r * r

# Hiển thị kết quả
if r > 0:
    st.success(f"Diện tích hình tròn là: {dien_tich:.2f}")
