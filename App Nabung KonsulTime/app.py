import streamlit as st

# Sidebar Dashboard
dashboard = st.Page("./fitur/dashboard.py", title="Dashboard")
nabung = st.Page("./fitur/nabung.py", title="Menabung")
penarikan = st.Page("./fitur/penarikan.py", title="Penarikan")

# Navigasi Menu
pg = st.navigation(
    {
        "Menu Utama": [dashboard],
        "Transaksi": [nabung, penarikan],
    }
)

if "total_semua" not in st.session_state:
    st.session_state["total_semua"] = []

pg.run()