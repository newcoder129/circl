{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st\n",
    "\n",
    "# Thay đổi màu nền thành màu hồng\n",
    "st.markdown(\n",
    "    \"\"\"\n",
    "    <style>\n",
    "    .stApp {\n",
    "        background-color: pink;\n",
    "    }\n",
    "    </style>\n",
    "    \"\"\",\n",
    "    unsafe_allow_html=True\n",
    ")\n",
    "\n",
    "st.title(\"Game tính diện tích hình tròn 🎯\")\n",
    "\n",
    "r = st.number_input(\"Nhập bán kính hình tròn (cm):\", min_value=0.0)\n",
    "\n",
    "if st.button(\"Tính diện tích\"):\n",
    "    dien_tich = 3.14 * r * r\n",
    "    st.success(f\"Diện tích hình tròn là: {dien_tich:.2f} cm²\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
