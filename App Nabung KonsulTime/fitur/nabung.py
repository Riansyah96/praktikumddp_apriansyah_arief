import streamlit as st

st.title("Menabung")

# Form Menabung
with st.form("Menabung"):
    nama = st.text_input("Nama Anda ")
    jumlah = st.number_input("Jumlah (Rp.) ")
    tanggal = st.date_input("Tanggal Menabung ")  
    waktu = st.time_input("Waktu Menabung ")
    button = st.form_submit_button(label="Menabung")
    if button and jumlah >= 50000:
        st.session_state["total_semua"].append(
            {
            "Tipe": "Menghitung",
            "Jumlah": jumlah,
            }
        )
        st.success(f"Terima kasih {nama} telah menabung sebesar Rp. {jumlah}")
    else:
        st.error("Jumlah Nominal menabung minimal Rp. 50.000")