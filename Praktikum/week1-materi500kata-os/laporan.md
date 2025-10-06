# Laporan Ringkasan Praktikum Week 2
**Nama:** Muhammad Fajri Abdullah  
**NIM:**  250202979
**Kelas:** 1IKRB  
**Topik:** Perbandingan Monolithic Kernel, Microkernel, dan Layered Architecture serta Relevansinya pada Sistem Modern


## Monolithic Kernel

**Konsep utama:**  
Monolithic kernel adalah arsitektur di mana seluruh layanan inti sistem operasi dijalankan di ruang kernel sebagai satu kesatuan besar. Komponen seperti manajemen proses, memori, sistem berkas, dan driver perangkat keras berada dalam level privilese tertinggi dan berinteraksi langsung satu sama lain.
**Kelebihan:**
- Kinerja tinggi karena komunikasi antar-komponen tidak perlu melalui mekanisme pesan.  
- Akses langsung antarbagian sistem membuat proses lebih cepat.
**Kekurangan:**
- Risiko tinggi: jika satu modul mengalami kerusakan, seluruh sistem dapat ikut terpengaruh.  
- Kompleksitas tinggi dalam pemeliharaan dan pengembangan.
**Contoh OS:**  
Linux, FreeBSD, dan OpenBSD. Kernel Linux modern tergolong monolithic, namun mendukung konsep *loadable modules* yang memungkinkan fleksibilitas dalam pengelolaan driver.


## Microkernel

**Konsep utama:**  
Microkernel hanya menyertakan fungsi-fungsi paling dasar seperti manajemen alamat memori, penjadwalan proses, dan komunikasi antarproses (IPC) di dalam ruang kernel. Layanan lainnya seperti sistem berkas dan driver dijalankan di ruang pengguna.
**Kelebihan:**
- Stabilitas dan keamanan lebih tinggi karena layanan terpisah dan terisolasi.  
- Jika satu komponen gagal, kernel tidak langsung terpengaruh.
**Kekurangan:**
- Komunikasi antarproses yang sering dapat menurunkan kinerja.  
- Implementasi lebih kompleks karena harus mengatur pertukaran pesan antar layanan.
**Contoh OS:**  
QNX (banyak digunakan di sistem otomotif dan industri), MINIX 3 (pendidikan dan penelitian), serta keluarga L4 Microkernel yang banyak diterapkan di sistem tertanam dan perangkat IoT.


## Layered Architecture

**Konsep utama:**  
Sistem operasi dibagi menjadi beberapa lapisan berjenjang, di mana setiap lapisan hanya berinteraksi dengan lapisan di bawahnya. Pendekatan ini menekankan modularitas dan keteraturan desain.
**Kelebihan:**
- Mudah dikelola dan dikembangkan karena struktur lapisannya jelas.  
- Memudahkan identifikasi kesalahan pada bagian tertentu.
**Kekurangan:**
- Potensi penurunan kinerja jika terlalu banyak batas antar lapisan.  
- Desain harus hati-hati agar setiap lapisan memiliki fungsi yang jelas.
**Contoh OS:**  
THE System (oleh Dijkstra), serta prinsip berlapis yang diadopsi dalam Windows NT dan macOS melalui struktur kernel hibrida.


## Analisis Relevansi terhadap Sistem Modern

Tidak ada satu model arsitektur yang unggul secara mutlak.  
Monolithic kernel tetap dominan pada sistem desktop dan server karena performanya tinggi serta memiliki ekosistem luas, seperti pada Linux.  
Microkernel menjadi pilihan untuk sistem yang menuntut keandalan dan keamanan tinggi, misalnya sistem otomotif, penerbangan, dan perangkat IoT.  

Layered architecture lebih berperan sebagai prinsip desain yang membantu modularitas dan keteraturan sistem, meskipun jarang digunakan sebagai model tunggal.  

Banyak sistem modern kini menggunakan pendekatan *hybrid kernel*, yang menggabungkan kecepatan monolithic dengan stabilitas microkernel. Contohnya adalah Windows NT dan Apple XNU kernel pada macOS.


## Kesimpulan

Arsitektur monolithic cocok untuk sistem umum dengan kebutuhan kinerja tinggi, microkernel unggul untuk sistem kritis yang membutuhkan keamanan dan reliabilitas, sedangkan layered architecture tetap penting sebagai konsep desain modular.  

Arah perkembangan sistem operasi modern menunjukkan kecenderungan menuju model *hibrida* yang menggabungkan efisiensi, fleksibilitas, dan keamanan secara seimbang.


**Tanggal:** 6-Oktober-2025