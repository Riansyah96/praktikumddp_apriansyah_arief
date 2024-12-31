import streamlit as st
import datetime


st.markdown(
    """
    <style>
    .stApp{
        # background-color: white;
    }
    
    [data-testid="stSidebar"]{
        background-color:green;
        color: white;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
        font-size: 14px;
    
    }
    
    # .stApp{
    # background-image: url("https://unsplash.com/photos/a-large-white-building-with-two-white-domes-on-top-of-it-RnjBHZmSDF4");
    # background-size: cover;
    # }
    
    </style>
    """,
    unsafe_allow_html = True 
)

class ZakatFitrah:
    def __init__(self):
        # Inisialisasi variabel kelas
        self.daftar_muzakki = []
        self.total_zakat = 0
        self.jenis_makanan = {
            "Beras": 36500,  # Harga per kg beras
            "Gandum": 952500,  # Harga per kg gandum
            "Jagung": 15500   # Harga per kg jagung
        }
        self.nama_amil = ""
        self.metode_pembayaran = ""

    def tambah_metode_pembayaran(self, metode_pembayaran):
        self.metode_pembayaran = metode_pembayaran

    def get_metode_pembayaran(self):
        return self.metode_pembayaran

    def tambah_muzakki(self, nama, jumlah_tanggungan, jenis_makanan, metode_pembayaran):
        zakat = self.jenis_makanan[jenis_makanan] * jumlah_tanggungan
        self.daftar_muzakki.append({
            "nama": nama,
            "jumlah_tanggungan": jumlah_tanggungan,
            "jenis_makanan": jenis_makanan,
            "zakat": zakat,
            "metode_pembayaran": metode_pembayaran
        })
        self.total_zakat += zakat
        return True

    def hitung_total_zakat(self):
        return self.total_zakat

    def generate_laporan(self):
        laporan = ""
        for i, muzakki in enumerate(self.daftar_muzakki, start=1):
            laporan += f"\n**Laporan Zakat ke-{i}**\n"
            laporan += f"\nNama Muzakki : {muzakki['nama']}\n"
            laporan += f"\nTanggungan : {muzakki['jumlah_tanggungan']}\n"
            laporan += f"\nJenis Makanan : {muzakki['jenis_makanan']}\n"
            laporan += f"\nZakat : Rp {muzakki['zakat']:,.2f}\n"
            laporan += f"\nMetode Pembayaran : {muzakki['metode_pembayaran']}\n\n"
        return laporan

def validasi_input(nama, jumlah_tanggungan):
    if not nama:
        return False, "Nama tidak boleh kosong"
    if jumlah_tanggungan < 1:
        return False, "Jumlah tanggungan harus lebih dari 0"
    return True, ""

def main():
    # Judul aplikasi
    st.title("KALKULATOR Zakat Fitrah")
    
    # Inisialisasi objek zakat
    if 'zakat' not in st.session_state:
        st.session_state.zakat = ZakatFitrah()

    # Input data muzakki
    st.header("Tambah Data Muzakki")
    
    # Input nama
    nama = st.text_input("Nama Muzakki")
    
    # Input jumlah tanggungan
    jumlah_tanggungan = st.number_input("Jumlah Tanggungan", min_value=1, value=1)

#      # Input daftar harga
    st.header("Daftar Harga Bahan Pokok")
    
    st.write('''
        \nBeras  : Rp. 36.500 /kg
        \nGandum : Rp. 952.500 /kg
        \nJagung : Rp. 15.500 /kg
     ''')

    # Pilih jenis makanan
    jenis_makanan = st.selectbox("Jenis Makanan Pokok", 
        ["Beras", "Gandum", "Jagung"]
    )

    # # Pilih metode pembayaran
    metode_pembayaran = st.selectbox("Metode Pembayaran", 
        ["Cash", "E-Money"]
    )

    # Tombol tambah muzakki
    if st.button("Tambah Muzakki"):
        # Validasi input
        valid, pesan = validasi_input(nama, jumlah_tanggungan)
        
        if valid:
            # Tambah muzakki menggunakan method kelas
            berhasil = st.session_state.zakat.tambah_muzakki(
                nama, jumlah_tanggungan, jenis_makanan, metode_pembayaran
            )
            
            if berhasil:
                st.success(f"Muzakki {nama} berhasil ditambahkan!")
            else:
                st.error("Gagal menambahkan muzakki")
        else:
            st.error(pesan)

    # Tampilkan total zakat
    total_zakat = st.session_state.zakat.hitung_total_zakat()
    st.metric("Total Zakat fitrah yang sudah terkumpul", f"Rp {total_zakat:,.2f}")

    # Tombol generate laporan
    if st.button("Generate Laporan"):
        laporan = st.session_state.zakat.generate_laporan()
        st.markdown(laporan)

# Jalankan aplikasi
if __name__ == "__main__":
    main()

