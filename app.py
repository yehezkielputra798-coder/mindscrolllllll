import streamlit as st
import pandas as pd
import os 


st.set_page_config(
    page_title="MindScroll",
    layout="centered"
)


st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#e0e7ff,#dbeafe,#fce7f3);
}

.card{
background:white;
padding:25px;
border-radius:25px;
box-shadow:0 10px 30px rgba(0,0,0,.15);
margin-bottom:20px;
}

.logo{
width:100px;
height:100px;
background:linear-gradient(135deg,#2563eb,#9333ea);
border-radius:50%;
display:flex;
align-items:center;
justify-content:center;
margin:auto;
font-size:50px;
font-weight:bold;
color:white;
}

.title{
text-align:center;
font-size:45px;
font-weight:900;
background:linear-gradient(90deg,#2563eb,#9333ea);
-webkit-background-clip:text;
color:transparent;
}

.section{
background:linear-gradient(90deg,#2563eb,#9333ea);
padding:15px;
border-radius:15px;
color:white;
font-size:22px;
font-weight:bold;
}

</style>
""", unsafe_allow_html=True)



st.markdown("""
<div class="card">

<div class="logo">M</div>

<div class="title">
MINDSCROLL
</div>

<p style="text-align:center">
Digital Behavior Analysis
</p>

</div>
""", unsafe_allow_html=True)



st.markdown("""
<div class="card">

MindScroll membantu memahami kebiasaan penggunaan media sosial,
kontrol diri digital, pengaruh terhadap emosi,
dan aktivitas sehari-hari.

</div>
""", unsafe_allow_html=True)



nama = st.text_input(
"Masukkan nama kamu"
)



st.markdown("""
<div class="section">
Evaluasi Kebiasaan Digital Kamu
</div>
""", unsafe_allow_html=True)



durasi = st.selectbox(
"Berapa lama kamu menggunakan media sosial dalam sehari?",
[
"Kurang dari 1 jam",
"1 - 3 jam",
"3 - 5 jam",
"5 - 8 jam",
"Lebih dari 8 jam"
]
)



pertanyaan = [

"Seberapa sering kamu membuka media sosial tanpa tujuan jelas?",

"Apakah kamu sering melewati waktu yang sudah direncanakan saat scrolling?",

"Apakah kamu sulit berhenti menggunakan media sosial?",

"Apakah media sosial membuat kamu menunda kegiatan penting?",

"Apakah kamu membuka media sosial saat stres atau bosan?",

"Apakah jumlah suka atau komentar memengaruhi perasaan kamu?",

"Apakah waktu kamu lebih banyak habis di media sosial?",

"Apakah kamu sulit menikmati waktu tanpa media sosial?"

]



jawaban=[]

for p in pertanyaan:

    jawaban.append(
        st.selectbox(
            p,
            [
            "Tidak pernah",
            "Kadang",
            "Sering",
            "Sangat sering"
            ]
        )
    )


if st.button("Mulai Analisis"):

    if nama.strip() == "":
        nama = "Kamu"


    skor = 0
    analisis_jawaban = []


    for i in range(len(pertanyaan)):

        soal = pertanyaan[i]
        jawab = jawaban[i]


        if jawab == "Tidak pernah":
            skor += 1
        elif jawab == "Kadang":
            skor += 2
        elif jawab == "Sering":
            skor += 3
        else:
            skor += 4



        # Analisis berdasarkan pertanyaan

        if soal == "Seberapa sering kamu membuka media sosial tanpa tujuan jelas?":

            hasil = f"""
Analisis Kebiasaan Membuka Media Sosial:

{nama}, berdasarkan jawaban kamu terlihat bahwa kamu memiliki kebiasaan membuka media sosial yang cukup terarah.

Kamu mampu menggunakan aplikasi ketika memang membutuhkan sesuatu dan tidak mudah mengikuti kebiasaan scrolling tanpa tujuan.

Hal ini menunjukkan bahwa kamu memiliki kesadaran digital yang baik dalam mengatur waktu dan fokus.

Pertahankan kebiasaan ini agar media sosial tetap menjadi alat yang membantu aktivitas kamu.
""" if jawab == "Tidak pernah" else f"""
Analisis Kebiasaan Membuka Media Sosial:

{nama}, jawaban kamu menunjukkan bahwa kebiasaan membuka media sosial mulai perlu diperhatikan.

Terkadang membuka aplikasi tanpa tujuan dapat membuat waktu berjalan tanpa terasa.

Cobalah membiasakan diri menentukan tujuan sebelum membuka media sosial agar penggunaan tetap lebih terkontrol.
""" if jawab == "Kadang" else f"""
Analisis Kebiasaan Membuka Media Sosial:

{nama}, kamu menunjukkan bahwa media sosial mulai cukup sering menarik perhatian kamu.

Kebiasaan membuka aplikasi tanpa tujuan dapat mengurangi fokus dan membuat waktu banyak terpakai.

Mulailah membuat batas penggunaan agar kamu tetap menjadi pengendali teknologi.
""" if jawab == "Sering" else f"""
Analisis Kebiasaan Membuka Media Sosial:

{nama}, jawaban kamu menunjukkan bahwa membuka media sosial tanpa tujuan sudah menjadi kebiasaan yang cukup kuat.

Hal ini dapat membuat kamu lebih mudah terdistraksi.

Cobalah mengatur waktu khusus menggunakan media sosial agar aktivitas lain tetap berjalan.
"""



        elif soal == "Apakah kamu sering melewati waktu yang sudah direncanakan saat scrolling?":

            hasil = f"""
Analisis Pengaturan Waktu:

{nama}, kamu terlihat mampu mengatur waktu scrolling dengan sangat baik.

Kamu dapat berhenti sesuai batas yang sudah dibuat sehingga kegiatan lain tetap berjalan.

Pertahankan kemampuan mengatur waktu digital ini.
""" if jawab == "Tidak pernah" else f"""
Analisis Pengaturan Waktu:

{nama}, terkadang penggunaan media sosial membuat waktu sedikit melewati rencana.

Hal ini masih bisa diperbaiki dengan meningkatkan kesadaran saat menggunakan aplikasi.

Cobalah memakai pengingat waktu agar durasi tetap seimbang.
""" if jawab == "Kadang" else f"""
Analisis Pengaturan Waktu:

{nama}, kamu mulai mengalami kesulitan dalam membatasi waktu scrolling.

Kondisi ini dapat membuat kegiatan penting tertunda.

Mulailah membuat aturan waktu penggunaan agar aktivitas utama tetap menjadi prioritas.
""" if jawab == "Sering" else f"""
Analisis Pengaturan Waktu:

{nama}, penggunaan media sosial terlihat cukup sulit dikendalikan.

Waktu scrolling dapat mengambil banyak waktu yang seharusnya digunakan untuk kegiatan lain.

Lakukan perubahan secara bertahap dengan mengurangi durasi penggunaan.
"""



        elif soal == "Apakah kamu sulit berhenti menggunakan media sosial?":

            hasil = f"""
Analisis Kontrol Diri:

{nama}, kamu memiliki kemampuan mengontrol penggunaan media sosial dengan baik.

Kamu mampu berhenti ketika diperlukan dan tidak mudah bergantung pada aplikasi.

Pertahankan kontrol diri positif ini.
""" if jawab == "Tidak pernah" else f"""
Analisis Kontrol Diri:

{nama}, terkadang kamu masih ingin menggunakan media sosial lebih lama.

Hal ini menunjukkan adanya kebiasaan yang perlu diperhatikan.

Cobalah memberi jeda setelah menggunakan media sosial.
""" if jawab == "Kadang" else f"""
Analisis Kontrol Diri:

{nama}, kamu mulai mengalami tantangan dalam menghentikan penggunaan media sosial.

Buat batas waktu agar penggunaan tidak mengganggu kegiatan lain.
""" if jawab == "Sering" else f"""
Analisis Kontrol Diri:

{nama}, media sosial terlihat cukup kuat memengaruhi kebiasaan kamu.

Mulailah melatih kontrol diri dengan mengurangi penggunaan secara perlahan.
"""



        elif soal == "Apakah media sosial membuat kamu menunda kegiatan penting?":

            hasil = f"""
Analisis Produktivitas:

{nama}, kamu mampu menjaga keseimbangan antara media sosial dan tanggung jawab.

Media sosial tidak banyak mengganggu kegiatan penting kamu.

Pertahankan kebiasaan baik ini.
""" if jawab == "Tidak pernah" else f"""
Analisis Produktivitas:

{nama}, terkadang media sosial membuat beberapa aktivitas sedikit tertunda.

Cobalah menyelesaikan hal penting terlebih dahulu sebelum membuka aplikasi.
""" if jawab == "Kadang" else f"""
Analisis Produktivitas:

{nama}, media sosial mulai memberikan pengaruh terhadap produktivitas kamu.

Atur prioritas agar waktu lebih efektif.
""" if jawab == "Sering" else f"""
Analisis Produktivitas:

{nama}, media sosial cukup sering membuat kegiatan penting tertunda.

Mulailah mengatur jadwal dan membatasi penggunaan agar aktivitas utama tetap berjalan.
"""



        else:

            hasil = f"""
Analisis Kebiasaan Digital:

{nama}, jawaban kamu sudah dianalisis.

Terus gunakan media sosial secara sadar dan seimbangkan dengan kegiatan lain agar teknologi tetap memberikan manfaat.
"""


        analisis_jawaban.append(hasil)



    st.write("## Analisis Detail Kebiasaan Media Sosial Kamu")


    for hasil in analisis_jawaban:

        st.info(hasil)



    # Kesimpulan akhir

    if skor <= 15:

        st.success(
        f"{nama}, kondisi digital kamu sangat terkontrol."
        )

        st.write("""
Hasil menunjukkan bahwa kamu mampu menggunakan media sosial dengan bijak.

Kamu masih memiliki kendali terhadap waktu, fokus, dan kebiasaan digital.
Pertahankan pola penggunaan positif ini.
""")


    elif skor <= 28:

        st.warning(
        f"{nama}, kondisi digital kamu mulai membutuhkan perhatian."
        )

        st.write("""
Media sosial mulai memberikan pengaruh pada beberapa kebiasaan.

Kamu masih mampu mengontrol penggunaan, tetapi perlu mulai mengatur waktu dan tujuan penggunaan.
""")


    else:

        st.error(
        f"{nama}, kondisi digital kamu memerlukan perubahan."
        )

        st.write("""
Media sosial sudah cukup memengaruhi kebiasaan sehari-hari.

Mulailah mengurangi penggunaan secara bertahap dan buat keseimbangan dengan aktivitas lain.
""")


    st.caption(
    "MindScroll | Digital Behavior Analysis"
    )