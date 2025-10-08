# Laporan Ringkasan Praktikum Week 2
*Nama:* Muhammad Fajri Abdullah  
*NIM:* 250202979
*Kelas:* 1IKRB  
*Topik:* Perbandingan Monolithic Kernel, Microkernel, dan Layered Architecture serta Relevansinya pada Sistem Modern

---

Ada tiga jenis arsitektur sistem operasi yang memiliki cara kerja dan tujuan penggunaan yang berbeda, mereka adalah Monolithic Kernel, Microkernel, dan Layered Architecture. Masing-masing mempunyai beberapa kelebihan dan kekurangan masing-masing yang mempengaruhi bagaimana mereka digunakan dalam perangkat modern. 

## 1.	Monolithic Kernel
Monolithic kernel adalah struktur di mana semua layanan penting sistem operasi berjalan bersama-sama dalam ruang lingkup yang sama yang disebut ruang kernel. Dalam Monolithic Kernel ini ada banyak bagian penting seperti pengelolaan proses, pengaturan memori, sistem file, dan driver perangkat keras. Semua komponen ini bekerja erat dan saling berhubungan langsung tanpa batas pemisah yang jelas.

*Kelebihan Monolithic Kernel :*
- Karena bagian-bagian bisa langsung saling mengakses tanpa harus lewat pesan atau protokol tertentu maka kerja sistem jadi cepat.
- Performa lebih tinggi disebabkan karena proses komunikasi lebih singkat dan efisien.

*Kekurangan Monolithic Kernel:*
- Seluruh sistem terganggu, bahkan crash jika satu bagian mengalami masalah.
- Pemeliharaan dan pengembangan rumit karena banyak fungsi dijalankan sekaligus di kernel.

Contoh sistem operasi yang menggunakan struktur Monolithic seperti Linux, FreeBSD, dan OpenBSD. Kernel Linux misalnya, memang besar tapi bisa fleksibel dikarenakan driver bisa ditambah atau dilepas kapan saja melalui modul yang bisa dimuat.

---

## 2.	Microkernel
Kernel ini ringan dan lebih minimalis daripada monolithic kernel. Microkernel memuat hanya fitur paling dasar di dalam kernel, seperti pengelolaan memori, penjadwalan proses, dan komunikasi antar proses (IPC). Fungsi sistem operasi lain seperti pengelolaan file, driver perangkat dijalankan di luar kernel, biasanya di ruang pengguna. 

*Kelebihan Microkernel:*
- Lebih aman dan stabil, kernel tetap aman dan sistem tidak langsung terganggu jika satu layanan berjalan di ruang pengguna rusak.
- Memudahkan isolasi kesalahan dan menjaga agar masalah tidak menyebar ke bagian lain.

*Kekurangan Microkernel:*
- kinerjanya bisa lebih lambat dibanding Monolithic kernel, karena komunikasi antar komponen lewat mekanisme pesan.
- Pengembangan lebih kompleks karena harus memastikan semua komunikasi antar layanan berjalan lancar tanpa hambatan.

Contoh sistem operasin yang menggunakan Microkernel adalah QNX yang populer di sistem otomotif dan industri, MINIX 3 yang digunakan sebagai sistem pendidikan dan penelitian, serta keluarga L4 yang sering dipakai di sistem tertanam dan perangkat Internet of Things (IoT).

---

## 3.	Layered Architecture
Disini sistem operasi dibagi menjadi beberapa lapisan atau layer yang berurutan. Setiap lapisan hanya berinteraksi dengan lapisan di bawahnya sehingga ada struktur yang jelas dan rapi. Ini memudahkan pengelolaan sistem karena tiap lapisan punya tugas dan fungsi tertentu.

*Kelebihan Layered Architecture:*
- Karena menggunakan modularitas struktur lapisan maka sistem jadi lebih mudah dikelola dan dikembangkan.
- Lebih mudah menemukan letak kesalahannya karena sistem terorganisir secara berlapis.

*Kekurangan Layered Architecture:*
- Proses komunikasi antar lapisan bisa membuat performa menurun karena terlalu banyak lapisan.
- Agar fungsi tiap lapisan tidak tumpang tindih dan bisa berjalan optimal maka memerlukan desain yang cermat.

Contoh sistem operasi yang menggunakan Layered Architecture adalah THE System yang dibuat oleh Dijkstra adalah contoh klasik, juga konsep berlapis ini diaplikasikan dalam sistem modern seperti Windows NT dan macOS yang menggunakan kernel hibrida.

---

## Model mana yang paling relevan untuk sistem modern?
Model kernel yang paling relevan untuk sistem operasi modern adalah hybrid kernel, yang mana menggabungkan antara kelebihan Monolithic kernel dan Microkernel. Model ini mengoptimalkan performa dengan komponen penting berjalan di kernel seperti Monolithic, sekaligus menjaga stabilitas dan keamanan dengan menjalankan layanan lain di ruang pengguna seperti Microkernel.
- Tidak ada jenis arsitektur yang sepenuhnya terbaik untuk semua kebutuhan. Masing-masing punya tempat dan peran berdasarkan tujuan sistemnya.
- Karena performanya bagus dan dukungan ekosistemnya luas maka monolithic kernel masih menjadi favorit di komputer desktop dan server, contohnya Linux.
- Microkernel cocok untuk perangkat yang memerlukan keamanan dan keandalan tinggi, misalnya mobil, pesawat, dan perangkat IoT yang berjalan terus dalam kondisi kritis.
- Meskipun jarang dipakai sebagai model utama sendirian, Layered architecture lebih sebagai prinsip penting untuk membangun sistem yang modular dan terstruktur.
- Banyak sistem modern akhirnya menggunakan model hybrid kernel, yang mencoba menggabungkan kecepatan dan efisiensi Monolithic kernel dengan stabilitas dan keamanan Microkernel. Contohnya adalah Windows NT dan XNU kernel di macOS milik Apple. Dengan cara ini, sistem operasi dapat berjalan dengan baik, aman, dan fleksibel di berbagai perangkat
Arsitektur monolithic cocok untuk sistem general atau umum dengan kebutuhan kinerja tinggi, microkernel unggul untuk sistem kritis yang mana membutuhkan keamanan dan juga reliabilitas, sedangkan layered architecture tetap penting sebagai konsep desain modular. Perkembangan sistem operasi modern menunjukkan kecenderungan menuju model hybrid/hibrida yang menggabungkan antara efisiensi, fleksibilitas, dan keamanan secara seimbang. 

---

*Tanggal Pengerjaan:* 8-Oktober-2025