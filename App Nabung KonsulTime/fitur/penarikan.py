import streamlit as st

st.title("Halaman Penarikan")

# Form Menabung
with st.form("Penarikan"):
    nama = st.text_input("Nama Anda ")
    jumlah = st.number_input("Jumlah (Rp.) ")
    tanggal = st.date_input("Tanggal Penarikan ")  
    waktu = st.time_input("Waktu Penarikan ")
    button = st.form_submit_button(label="Penarikan")
    if button and jumlah >= 50000:
        st.session_state["total_semua"].append(
            {
            "Tipe": "Penarikan",
            "Jumlah": jumlah,
            }
        )
        st.success(f"Terima kasih {nama} telah menarik sebesar Rp. {jumlah}")
    else:
        st.error("Jumlah Nominal penarikan minimal Rp. 50.000")