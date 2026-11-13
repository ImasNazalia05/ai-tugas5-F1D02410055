# Sistem Pakar: Penentuan Status dan Mitigasi Pencemaran Udara Akibat Karhutla

## 1. Identitas

- **Nama:** Imas Nazalia Rahmawati
- **NIM:** F1D02410055

## 2. Topik & Cara Menjalankan Program

**Topik:** Sistem pakar berbasis aturan (*rule-based system*) untuk menentukan status bahaya kualitas udara serta rekomendasi mitigasi/peringatan dini akibat Kebakaran Hutan dan Lahan (Karhutla). Topik ini berfokus pada status parameter lingkungan, evaluasi jarak pandang, dan tindakan mitigasi bencana.

**Cara menjalankan:**

- **Bahasa:** Python 3
- **Versi:** Python 3.8 atau lebih baru
- **Perintah:** buka terminal di direktori repositori ini, lalu jalankan:

```bash
python main.py
```

Program akan menanyakan sejumlah fakta (jawab `y` atau `t`), kemudian menampilkan kesimpulan beserta batas keberlakuan.

## 3. Daftar Sumber & Tabel Aturan

**Daftar sumber**

| Kode | Judul | Penerbit | URL | Tanggal Akses |
| --- | --- | --- | --- | --- |
| S1 | Kualitas Udara Indonesia | Badan Meteorologi Klimatologi dan Geofisika (BMKG) | https://iklim.bmkg.go.id/id/kualitas-udara-indonesia/ | 13 November 2026 |
| S2 | Peraturan Menteri Lingkungan Hidup dan Kehutanan No. 14 Tahun 2020 tentang Indeks Standar Pencemar Udara (ISPU) | Jaringan Dokumentasi dan Informasi Hukum (JDIH) KLHK | https://peraturan.bpk.go.id/Download/156214/Permen%20LHK%20Nomor%2014%20Tahun%202020.pdf | 13 November 2026 |

**Tabel aturan (IF-THEN)**

| Aturan | IF (Jika) | THEN (Maka) | Sumber |
| --- | --- | --- | --- |
| **R1** | konsentrasi PM2.5 melampaui angka 150 **OR** terlihat kabut asap yang mengganggu pernapasan ringan | kualitas udara kategori sangat tidak sehat | S1 |
| **R2** | konsentrasi PM2.5 melampaui angka 250 **OR** bau asap sisa pembakaran tercium kuat | kualitas udara kategori berbahaya | S1 |
| **R3** | kualitas udara kategori sangat tidak sehat **AND** jarak pandang kurang dari 1 km | terbitkan peringatan dini pembatasan transportasi akibat jarak pandang terbatas | S2 |
| **R4** | kualitas udara kategori sangat tidak sehat **AND** terdapat titik panas (hotspot) di wilayah sekitar | tingkatkan frekuensi patroli lahan dan sematkan status siaga karhutla | S2 |
| **R5** | kualitas udara kategori berbahaya **AND** terdapat titik panas (hotspot) di wilayah sekitar | tetapkan status darurat pencemaran udara dan hentikan semua aktivitas luar ruangan | S2 |

## 4. Metode yang Dipilih dan Alasannya

Sistem ini menggunakan **Forward Chaining (FC)**.

**Alasan:** Kondisi pencemaran udara akibat karhutla bergantung pada fakta-fakta lapangan yang terjadi secara *real-time* (konsentrasi PM2.5, jarak pandang, dan deteksi titik panas). Forward Chaining bersifat *data-driven*: program mengumpulkan fakta yang diketahui dari pengguna terlebih dahulu, mencocokkannya dengan premis aturan, lalu memicu kesimpulan secara berantai (misalnya R1 → R3, atau R2 → R5) hingga mencapai rekomendasi mitigasi akhir.

## 5. Kasus Uji & Screenshot

**Kasus 1 (Positif, menghasilkan kesimpulan)**

- **Fakta awal:** pengguna menjawab `y` pada `konsentrasi PM2.5 melampaui angka 150` dan `jarak pandang kurang dari 1 km`.
- **Hasil:** aturan R1 terpicu, lalu berantai memicu R3. Kesimpulan: **terbitkan peringatan dini pembatasan transportasi akibat jarak pandang terbatas**.

![Kasus 1](screenshot/kasus1.png)

**Kasus 2 (Positif, menghasilkan kesimpulan)**

- **Fakta awal:** pengguna menjawab `y` pada `konsentrasi PM2.5 melampaui angka 250` dan `terdapat titik panas (hotspot) di wilayah sekitar`.
- **Hasil:** aturan R2 terpicu, lalu berantai memicu R5. Kesimpulan: **tetapkan status darurat pencemaran udara dan hentikan semua aktivitas luar ruangan**.

![Kasus 2](screenshot/kasus2.png)

**Kasus 3 (Negatif, tidak menghasilkan kesimpulan)**

- **Fakta awal:** pengguna hanya menjawab `y` pada satu fakta, yaitu `jarak pandang kurang dari 1 km`.
- **Hasil:** tidak ada fakta tentang konsentrasi polutan yang terpenuhi, sehingga R1 dan R2 tidak terpicu dan R3 sampai R5 tidak dapat dijalankan. Program menampilkan **"Kesimpulan: tidak ada"** beserta batas keberlakuan.

![Kasus 3](screenshot/kasus3.png)

## 6. Batas Keberlakuan

Pengetahuan dalam sistem pakar ini berasal dari pedoman ISPU (Permen LHK No. 14 Tahun 2020) dan portal Kualitas Udara BMKG, yang diterjemahkan menjadi aturan IF-THEN. Sistem hanya berlaku untuk keadaan pencemaran udara akibat karhutla, dengan mengevaluasi parameter fisik lingkungan (polutan dan titik panas) serta jarak pandang operasional. Sistem tidak menilai kondisi kesehatan manusia maupun penyebab pencemaran selain karhutla. Hasil keluaran program hanya berupa **saran awal mitigasi** secara komputasional, **bukan keputusan akhir** dan bukan penetapan status tanggap darurat resmi dari instansi berwenang (seperti BNPB atau Pemerintah Daerah). Batas keberlakuan ini juga ditampilkan di program setiap kali kesimpulan dikeluarkan.

## 7. Penggunaan Alat Bantu AI

Saya menggunakan alat bantu AI sebagai rekan diskusi untuk mencari *keyword* literatur pemerintah yang valid (BMKG dan KLHK), menyesuaikan struktur file JSON agar sesuai dengan aturan berantai, dan membantu menemukan kesalahan logika (*debugging*) pada pemisahan fakta murni di algoritma Python.