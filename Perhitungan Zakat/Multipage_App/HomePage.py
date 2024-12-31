import streamlit as st
from typing import List, Dict

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("istiqlal.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    
    [data-testid="stSidebar"] {
        background-color: rgba(0, 128, 0, 0.8); /* Warna hijau dengan transparansi */
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

# Sidebar directory
pages = {
    "Laziz Muhammadiyah": "./pages/lazizmu.py",
    "Laziz Nadhatul Ulama": "./pages/laziznu.py",
    "Badan Zakat Nasional": "./pages/baznas.py",
    "Zakat Fitrah": "./pages/zakatfitrah.py",
    "Zakat Mal": "./pages/zakatmal.py",
    "Zakat Saham": "./pages/zakatsaham.py",
}

# page_selection = st.sidebar.radio("Pilih Halaman", list(pages.keys()))


# pages.st.sidebar.radio

# Mengatur judul dan deskripsi aplikasi
st.title("ZakatGO")
st.write("aplikasi kalkulator zakat online ")

# Define menu options
menu = ["BERANDA", "TENTANG KAMI", "KONTAK KAMI"]

# Create a variable to store the selected option
selected_option = None

# Create columns for each menu option
cols = st.columns(len(menu))

# Create buttons in each column
for i, option in enumerate(menu):
    with cols[i]:
        if st.button(option):
            selected_option = option  # Store the selected option

# Menampilkan konten berdasarkan pilihan menu
if selected_option == "BERANDA":
    st.subheader("Beranda")
    st.write("Selamat datang di halaman beranda aplikasi ZakatGO.aplikasi pembantu perhitungan dan pembayaran zakat online yang mudah dan cepat.")
    
    # Brief Description
    st.write("### Deskripsi Aplikasi")
    st.write("Aplikasi ini dirancang untuk mempermudah anda membayar kewajiban anda sebagai seorang muslim. Dengan aplikasi ini, anda dapat dengan mudah dan cepat dalam menunaikan kewajiban anda secara cepat.")
    
    # Key Features
    st.write("### Fitur Utama ###")
    features = [
        "Fitur 1: [kalkulator penghitung zakat]",
        "Fitur 2: [pembayaran zakat langsung]",
        "Fitur 3: [catatan pengeluaran zakat]",
    ]
    
    for feature in features:
        st.write(f"- {feature}")
    
    # Navigation Tips
    st.write("### Tips Navigasi")
    st.write("Gunakan menu di sisi kiri untuk menjelajahi aplikasi. Anda dapat mengunjungi halaman 'Kontak' untuk menghubungi kami atau 'Tentang Kami' untuk mengetahui lebih lanjut tentang aplikasi ini.")
    
    # Call to Action
    st.write("### Ayo Mulai!")
    st.write("Klik pada menu di atas untuk mulai menggunakan aplikasi ini. Kami harap Anda menemukan aplikasi ini bermanfaat!")
    
elif selected_option == "TENTANG KAMI":
    st.subheader("Tentang Kami")
    st.write("Halaman ini kami buat agar anda mengetahui siapa yg berada dibalik aplikasi ini dengan tujuan transparansi.")
    
    # Background Information
    st.write("### Latar Belakang")
    st.write("Aplikasi ini dikembangkan untuk membantu pengguna dalam membayar zakat. Kami percaya bahwa dengan membuat aplikasi ini kita dapat menyalurkan zakat dengan lebih transparan dan tepat sasaran.")
    
    # Purpose of the Application
    st.write("### Tujuan")
    st.write("Tujuan dari aplikasi ini adalah untuk memastikan zakat anda tersalurkan dengan benar dan transparan. Kami ingin agar masyarakat semakin mudah dalam membayar zakat dan menyalurkan dana zakat dengan lebih baik dan transparan.")
    
    # Team Information
    st.write("### Tim Kami")
    st.write("Kami adalah tim yang terdiri dari 3 anggota yang memiliki latar belakang di bidang programing dan matematika. Berikut adalah anggota tim kami:")
    
    # Example team members
    team_members = {
        "Muhammad Anfasa Umar": "Chief Executive Officer",  
        "Arief Rachman Apriansyah": "Product Manager",
        "Mirta Alfaluna Kaban": "Staf Pengembangan Aplikasi",
    }
    
    for name, role in team_members.items():
        st.write(f"- **{name}**: {role}")
    
elif selected_option == "KONTAK KAMI":
    st.subheader("Kontak")
    st.write("Halaman ini di buat untuk menampung kritik dan saran anda untuk bahan perbaikan aplikasi di kemudian hari.")
    
    # Contact form
    with st.form(key='contact_form'):
        name = st.text_input("Nama")
        email = st.text_input("Email")
        message = st.text_area("Pesan")
        
        # Submit button
        submit_button = st.form_submit_button("Kirim")
        
        if submit_button:
            # Here you can add code to handle the form submission, e.g., send an email or save to a database
            st.success("Pesan Anda telah dikirim! Terima kasih atas umpan balik Anda.")

# Menambahkan footer
st.write("© 2024 Aplikasi Streamlit Anda. Semua hak cipta dilindungi undang-undang.")
