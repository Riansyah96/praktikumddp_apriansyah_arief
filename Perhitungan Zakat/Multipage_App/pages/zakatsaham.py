import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-image: url('URL_TO_YOUR_IMAGE');
        background-size: cover; /* Adjusts the image to cover the entire background */
        background-position: center; /* Centers the image */
    }
    
    [data-testid="stSidebar"] {
        background-color: green;
        color: white;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
        font-size: 14px;
    }
    
    </style>
    """,
    unsafe_allow_html=True 
)

def hitung_zakat_saham(nilai_pasar, jumlah_saham, persen_zakat=2.5):
    """
    Fungsi untuk menghitung zakat saham.

    Args:
    nilai_pasar (float): Nilai pasar per saham.
    jumlah_saham (int): Jumlah saham yang dimiliki.
    persen_zakat (float): Persentase zakat yang harus dibayarkan.

    Returns:
    float: Jumlah zakat yang harus dibayarkan.
    """
    total_nilai_saham = nilai_pasar * jumlah_saham
    zakat = (persen_zakat / 100) * total_nilai_saham
    return zakat

# Pengaturan dasar
persen_zakat = 2.5  # Persentase zakat saham

# Inisialisasi session state untuk menyimpan data pembayar zakat
if 'pembayar_zakat' not in st.session_state:
    st.session_state.pembayar_zakat = []

# Tampilan antarmuka menggunakan Streamlit
st.title('KALKULATOR Zakat Saham')
st.write('Sistem Perhitungan Zakat Saham Secara Online Untuk Memudahkan Masyarakat Membayar Zakat')

# Input dari pengguna
nama_pembayar = st.text_input('Masukkan Nama Anda')
jenis_zakat = st.text_input('Masukkan Nama Saham yang Ingin Dibayar')
nilai_pasar = st.number_input('Masukkan Nilai Pasar per lembar Saham (Rupiah)', min_value=0.0, format="%.2f")
jumlah_lot = st.number_input('Masukkan Jumlah Lot yang Dimiliki(1 lot = 100 lembar))', min_value=0, format="%d")

# Dropdown untuk memilih metode pembayaran
metode_pembayaran = st.selectbox("Pilih Metode Pembayaran Zakat", ["Transfer Bank", "Tunai", "QRIS","e-wallet"])

# Menghitung jumlah saham dari jumlah lot
jumlah_saham = jumlah_lot * 100

# Tombol untuk menghitung zakat saham
if st.button('Hitung Zakat Saham'):
    if nama_pembayar:  # Pastikan nama pembayar tidak kosong
        # Hitung zakat saham
        zakat = hitung_zakat_saham(nilai_pasar, jumlah_saham, persen_zakat)
        
        # Tampilkan hasil zakat
        st.success(f'{nama_pembayar}, Anda Diwajibkan Untuk membayar Zakat saham Yang Anda Miliki di {jenis_zakat}. Jumlah Zakat Saham yang Harus Dibayarkan: Rp {zakat:.2f}')
        st.write(f'Metode pembayaran yang dipilih: {metode_pembayaran}')
        
        # Menyimpan data pembayar zakat
        st.session_state.pembayar_zakat.append({
            'nama': nama_pembayar,
            'jenis_zakat': jenis_zakat,
            'zakat': zakat,
            'metode_pembayaran': metode_pembayaran  # Menyimpan metode pembayaran
        })
    else:
        st.warning('Silakan masukkan nama Anda sebelum menghitung zakat.')

#menampilkan pilihan pembayaran 

#metode pembayaran transfer
if metode_pembayaran == "Transfer Bank":
    st.header("Pilih Bank Anda")
    bank = st.selectbox("Pilih Bank", ["BCA", "BNI", " BRI","MANDIRI"])
    st.write("Masukan Nama Pemilik Rekening")
    nama_pembayar = st.text_input("Nama Pemilik Rekening")
    st.write("Masukan Nomor Rekening Anda Untuk Validasi Data")
    nomor_rekening = st.text_input("Nomor Rekening", max_chars=16)
    

    # Validasi nomor rekening
    if st.button("Konfirmasi"):
        if len(nomor_rekening) < 4 or len(nomor_rekening) > 16:
            st.error("Nomor rekening harus antara 10 hingga 16 digit.")
        if st.button("Konfirmasi"):
            st.success("Pembayaran di tempat berhasil. Terima kasih!")
        else:
            st.success(f"Pembayaran melalui {bank} berhasil dengan nomor rekening {nomor_rekening}.")

    # Menampilkan deskripsi
    st.subheader("Semua yang tertera pada halaman ini telah ter verifikasi oleh tim profesional kami.")

    # Menambahkan gambar (gunakan URL atau path lokal)
    if metode_pembayaran == "Transfer Bank":
        st.image("rekening_nu.png", caption="Lembaga Zakat Infaq dan Shadaqah Nadhatul Ulama (LAZISNU)")
        st.image("rekening_mu.png", caption="Lembaga Zakat Infaq dan Shadaqah Muhammadiyah (LAZISMU)")

    # Atau, Anda bisa menggunakan gambar dari path lokal
    uploaded_file = st.file_uploader("Upload Bukti Pembayaran Zakat", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
    # Menampilkan gambar yang diunggah
     st.image(uploaded_file, caption="Uggah Gambar Hasil Pembayaran", use_column_width=True)
    st.write("Gambar berhasil diunggah!")

#metode pembayaran e-walet
elif metode_pembayaran == "e-wallet":
    st.header("Pilih E-Wallet Anda")
    e_wallet = st.selectbox("Pilih DOMPET DIGITAL", ["OVO", "Gopay", "DANA","ShoopePay"])
    nama_pembayar = st.text_input("Nama Pemilik DOMPET DIGITAL")
    st.write("Masukan Nomor E-Wallet Anda Untuk Validasi Data")
    nomor_telepon = st.text_input("Nomor Telepon E-Wallet",max_chars=16)

    if st.button("Konfirmasi"):
        if len(nomor_telepon) < 10:
            st.error("Nomor telepon tidak valid.")
        if st.button("Konfirmasi"):
            st.success("Pembayaran di tempat berhasil. Terima kasih!")
        else:
            st.success(f"Pembayaran melalui {e_wallet} berhasil.")
        
    # # Menambahkan gambar (gunakan URL atau path lokal)
    # if metode_pembayaran == "e-walet":
    #     metode_pembayaran = st.selectbox("Pilih Badan Zakat",["LazizMU","LazizNU","Baznas"])
    #     if st.selectbox ("Pilih Badan Zakat") == "LazizMU":
    #         st.image("rekening_mu.png", caption="Lembaga Zakat Infaq dan Shadaqah Muhammadiya")
    #     elif st.selectbox ("pilih badan zakat") == "LazizaNU":
    #         st.image("qrisNU.jpg", caption="Lembaga Zakat Infaq dan Shadaqah Nadhatul Ulama (LAZISNU)")
    #     elif st.selectbox ("Pilih Badan Zakat") == "Baznas":
    #         st.image("qris_baznas.png",caption ="Badan Amal Zakat Negara (Baznas)")

     # Atau, Anda bisa menggunakan gambar dari path lokal
    uploaded_file = st.file_uploader("Upload Bukti Pembayaran Zakat", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
     
    # Menampilkan gambar yang diunggah
     st.image(uploaded_file, caption="Uggah Gambar Hasil Pembayaran")
    st.write("Gambar berhasil diunggah!")


elif metode_pembayaran == "QRIS":
    st.header("Pilih QRIS Anda")
    st.image("qrisMU.png", caption="LazisMU")
    st.image("qrisNU.JPG", caption="LazisNU")
    st.image("qris_baznas.png", caption="Baznas")
    st.write("Pembayaran melalui QRIS berhasil. Terima kasih!")
    uploaded_file = st.file_uploader("Upload Bukti Pembayaran Zakat", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        

    # Atau, Anda bisa menggunakan gambar dari path lokal
        uploaded_file = st.file_uploader("Upload Bukti Pembayaran Zakat", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
    # Menampilkan gambar yang diunggah
     st.image(uploaded_file, caption="Uggah Gambar Hasil Pembayaran", use_column_width=True)
    st.write("Gambar berhasil diunggah!")
                                                                        

# Menampilkan daftar pembayar zakat
    if st.session_state.pembayar_zakat:
            st.subheader("Daftar Pembayar Zakat")
    for pembayar in st.session_state.pembayar_zakat:
        st.write(f"Nama: {pembayar['nama']}, Penghasilan Tahunan: Rp {pembayar['penghasilan_tahunan']:.2f}, Zakat: Rp {pembayar['zakat']:.2f}, Metode Pembayaran: {pembayar['metode_pembayaran']}")


# Menampilkan daftar pembayar zakat
if st.session_state.pembayar_zakat:
    st.subheader("Daftar Pembayar Zakat")
    for pembayar in st.session_state.pembayar_zakat:
        st.write(f"Nama: {pembayar['nama']}, Jenis Zakat: {pembayar['jenis_zakat']}, Zakat: Rp {pembayar['zakat']:.2f}, Metode Pembayaran: {pembayar['metode_pembayaran']}")
