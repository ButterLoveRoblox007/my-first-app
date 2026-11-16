import streamlit as st
st.title("🧾 แอปคำนวณส่วนลดและ VAT 7%")
price = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0 , value=0.0)
A = st.number_input("กรอกส่วนลด (%)::", min_value=0.0 , value=0.0)
A_discount = price * ( B_discount / 100)

vat = price * 0.07
st.divider()
st.write(f"• เฉพาะvat: {vat:.2f} บาท")

