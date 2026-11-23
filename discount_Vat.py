import streamlit as st
st.title("📄 แอปคำนวณส่วนลดและ VAT 7%")

price = st.number_input("กรอกราคาเต็มของสินค้า (บาท):", min_value=0.0, value=0.0)
B_discount = st.number_input("กรอกส่วนลด (%):", min_value=0.0, value=0.0)

A_discount = price * (B_discount / 100)      
A_price = price - A_discount                 
vat = A_price * 0.07                         

st.divider()

st.markdown(f"• ส่วนลด ({B_discount:.0f}%): -{A_discount:,.2f} บาท")
st.markdown(f"• ราคาหลังหักส่วนลด: {A_price:,.2f} บาท")
st.markdown(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): +{vat:,.2f} บาท")
st.markdown(f"### • ราคาสุทธิที่ต้องจ่าย: {net_price:,.2f} บาท")

st.divider()

st.write("นางสาวดีใจ ยิ้มแย้ม เลขที่ 5 ม.4/5")
