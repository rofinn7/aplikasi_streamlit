import streamlit as st

# Inisialisasi session_state untuk halaman
if "page" not in st.session_state:
    st.session_state.page = "home"

# Fungsi untuk kembali ke halaman awal
def go_home():
    st.session_state.page = "home"

# Halaman utama
if st.session_state.page == "home":
    st.title("Aplikasi Sederhana Streamlit")
    st.write("Aplikasi ini memiliki beberapa fitur yang bisa digunakan. Cukup klik salah satu fitur untuk menggunakannya.")
    st.write("Pilih salah satu fitur:")

    if st.button("Kalkulator Sederhana"):
        st.session_state.page = "kalkulator"
    if st.button("Konversi Suhu (Celcius, Fahrenheit dan Reamur)"):
        st.session_state.page = "konversi"
    if st.button("Perhitungan Fibonacci"):
        st.session_state.page = "fibonacci"

# Halaman kalkulator sederhana
elif st.session_state.page == "kalkulator":
    
    # Tombol redirect ke halaman utama
    if st.button("Kembali"):
        go_home()
    
    st.title("Kalkulator Sederhana")
    
    # Input angka pertama, angka kedua dan operator
    a = st.number_input("Masukkan angka pertama", value=0.0)
    b = st.number_input("Masukkan angka kedua", value=0.0)
    operator = st.selectbox("Pilih operator:", ["+", "-", "*", "/"])

    # Proses perhitungan sesuai operator yang dipilih
    if st.button("Hitung"):
        if operator == "+":
            hasil = a + b
        elif operator == "-":
            hasil = a - b
        elif operator == "*":
            hasil = a * b
        elif operator == "/":
            hasil = a / b if b != 0 else "Error: Tidak bisa dibagi 0!"
        else:
            hasil = "Operator tidak valid!"
            
        # Menampilkan hasil
        st.success(f"Hasil: {hasil}")

# Halaman konversi suhu
elif st.session_state.page == "konversi":
    
    # Tombol redirect ke halaman utama
    if st.button("Kembali"):
        go_home()
    
    st.title("Konversi Suhu (Celcius, Fahrenheit dan Reamur)")
    
    # Input suhu
    nilai = st.number_input("Masukkan nilai suhu:", value=0.0)

    # Pilih satuan
    satuan_asal = st.selectbox(
        "Pilih satuan:",
        ("Celcius", "Reamur", "Fahrenheit")
    )

    # Proses konversi suhu
    if satuan_asal == "Celcius":
        celcius = nilai
        reamur = (4/5) * celcius
        fahrenheit = (9/5) * celcius + 32

    elif satuan_asal == "Reamur":
        reamur = nilai
        celcius = (5/4) * reamur
        fahrenheit = (9/4) * reamur + 32

    elif satuan_asal == "Fahrenheit":
        fahrenheit = nilai
        celcius = (5/9) * (fahrenheit - 32)
        reamur = (4/9) * (fahrenheit - 32)

    # Tampilkan hasil
    st.subheader("Hasil Konversi:")
    st.write(f"Celcius: {celcius:.2f} C")
    st.write(f"Fahrenheit: {fahrenheit:.2f} F")
    st.write(f"Reamur: {reamur:.2f} R")
    
# Halaman Perhitungan Fibonacci
elif st.session_state.page == "fibonacci":
    
    # Tombol redirect ke halaman utama
    if st.button("Kembali"):
        go_home()
        
    st.title("Perhitungan Fibonacci")
    
    # Input nilai n
    n = st.number_input("Masukkan jumlah suku (n):", min_value=1, step=1)

    # Fungsi fibonacci
    def fibonacci(n):
        deret = []
        a, b = 0, 1
        for _ in range(n):
            deret.append(a)
            a, b = b, a + b
        return deret

    if st.button("Generate Deret"):
        hasil = fibonacci(n)
        st.subheader(f"Deret Fibonacci hingga suku ke-{n}:")
        st.write("*Note: Deret fibonacci ini dimulai dari angka 0 dan 1")
        st.write(", ".join(map(str, hasil)))