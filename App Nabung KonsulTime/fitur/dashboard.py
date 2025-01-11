import streamlit as st

st.title("Dashboard")

def total():
    total_nabung = sum(t["Jumlah"]
                       for t in st.session_state ["total_semua"]
                       if t ["Tipe"] == "Menghitung")
    total_tarik = sum(t["Jumlah"]
                       for t in st.session_state ["total_semua"]
                       if t ["Tipe"] == "Penarikan")
    return total_nabung - total_tarik

total_semua = st.session_state["total_semua"]
total_nabung = total()
total_tarik = sum(t["Jumlah"] for t in st.session_state ["total_semua"] if t ["Tipe"] == "Menarik")

st.metric("Total Total Anda", f"Rp.{total_nabung:,}")