
# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)

---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB

---

## Tujuan
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.


---

## Dasar Teori
1. Batas Memori Tegas (Hard Limit): Docker menggunakan parameter '--memory' untuk menetapkan batas maksimal RAM. Jika kontainer melampaui batas ini, sistem akan menghentikan kontainer secara otomatis demi melindungi stabilitas sistem host dari kegagalan fungsi.
2.Pembatasan Kuota CPU: Secara standar, kontainer akan mengambil seluruh tenaga CPU yang tersedia. Dengan flag '--cpus', User dapat mengatur jumlah core CPU yang boleh digunakan, sehingga aplikasi tidak memonopoli prosesor dan sistem tetap responsif.
3. Mekanisme OOM Killer: Docker mengintegrasikan fitur Linux Out-Of-Memory Killer untuk memantau penggunaan sumber daya. Fitur ini berfungsi sebagai jaring pengaman yang mematikan kontainer yang terlalu boros memori sebelum menyebabkan seluruh sistem komputer mengalami crash
4. Otomatisasi Penghapusan Kontainer: Flag '--rm' berfungsi untuk mengelola siklus hidup kontainer secara bersih. Fitur ini memastikan semua sumber daya dan identitas kontainer langsung dihapus saat proses selesai, sehingga mencegah terjadinya konflik nama saat User menjalankan perintah yang sama kembali.

---

## Langkah Praktikum
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```

---

## Kode / Perintah
Potongan kode atau perintah utama:

```bash
 docker build -t week13-resource-limit .
 ```

```bash
docker run --rm week13-resource-limit
```

```bash
docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```

```bash
docker run week13-resource-limit
```

```bash
docker run --cpus="0.5" --memory="256m" week13-resource-limit
```

```bash
docker stats
```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](screenshots/hasil_limit_(docker_stats_awalan).png)

![Screenshot hasil](screenshots/hasil_limit_(docker_run_--rm_week13-resource-limit_stats).png)

![Screenshot hasil](screenshots/hasil_limit_(docker_run_--rm_week13-resource-limit).png)

![Screenshot hasil](screenshots/hasil_limit_(docker_run_week13-resource-limit_stats).png)

![Screenshot hasil](screenshots/hasil_limit_(docker_run_week13-resource-limit).png)

![Screenshot hasil](screenshots/hasil_limit_(docker_run_--rm_--cpus=0.5_--memory=256m_week13-resource-limit_stats).png)

![Screenshot hasil](screenshots/hasil_limit_(docker_run_--rm%20--cpus=0.5_--memory=256m_week13-resource-limit).png)

![Screenshot hasil](screenshots/hasil_limit_(docker_run_--cpus=0.5_--memory=256m_week13-resource-limit_stats).png)

![Screenshot hasil](screenshots/hasil_limit_(docker_run_--cpus=0.5_--memory=256m_week13-resource-limit).png)

---

## Analisis & Tugas

1. Eksperimen Tanpa Limit Resource
   
   Detail Pengujian
   - Perintah: docker run --rm week13-resource-limit
   Data Monitoring (docker stats):    
   - CPU %: Melonjak hingga 70.08%.
   - MEM USAGE: Terpakai sekitar 100.4 MiB.
   - MEM LIMIT: Terbuka lebar di angka 7.702 GiB (mengikuti total kapasitas RAM Host).
   - NET I/O: 1.17kB / 126B.
   - BLOCK I/O: 0B / 201kB.
   Hasil Pengamatan & Analisis
   - Performa CPU: Tanpa adanya batasan (--cpus), kontainer mencoba mengambil sumber daya sebanyak mungkin yang tersedia untuk menyelesaikan proses komputasi. Angka 70.08% menunjukkan beban kerja yang tinggi pada prosesor.
   - Alokasi Memori: Meskipun aplikasi hanya menggunakan sekitar 100 MiB, sistem tetap menyediakan batas maksimal (Limit) sebesar 7.702 GiB. Hal ini berisiko jika aplikasi mengalami memory leak, karena ia dapat menghabiskan seluruh RAM komputer host.
   - Efisiensi Sistem: Penggunaan --rm memastikan bahwa meskipun aplikasi berjalan dengan beban tinggi, tidak ada sisa-sisa kontainer yang membebani media penyimpanan setelah proses "Berjalan... Memori: ~100MB" selesai ditampilkan di layar.

2. Eksperimen Dengan Limit Resource (--cpus="0.5")
   
   Detail Pengujian
   - Perintah: docker run --rm --cpus="0.5" --memory="256m" week13-resource-limitFile 
    pasca-eksekusi.
   Data Monitoring (docker stats)
   - CPU %: Berada di angka 45.48%.
   - MEM USAGE: Terpakai sekitar 100.4 MiB.
   - MEM LIMIT: Terkunci tepat di angka 256 MiB.
   - MEM %: Penggunaan memori adalah 39.23% dari jatah yang diberikan.
   - NET I/O: 1.17kB / 126B.
   - BLOCK I/O: 6.21MB / 201kB.3. 
   Hasil Pengamatan & Analisis
   - Kendali CPU: Penggunaan CPU tertahan di angka 45.48%, yang membuktikan bahwa Docker secara efektif melakukan throttling. Meskipun aplikasi membutuhkan daya lebih (seperti terlihat pada skenario tanpa limit yang mencapai 70%), Docker memaksanya tetap di bawah ambang batas 50% ($0.5$ core).
   - Isolasi Memori: Berbeda dengan sistem tanpa limit yang membuka batas hingga 7.7 GB, di sini sistem hanya menyediakan 256 MiB. Hal ini memastikan bahwa jika terjadi lonjakan penggunaan memori yang tidak wajar, kontainer tidak akan mengganggu stabilitas aplikasi lain di luar Docker.
   - Kebersihan Sistem: Dengan adanya flag --rm, semua jejak penggunaan resource (seperti filesystem layer sementara) langsung dibersihkan setelah teks "Berjalan... Memori: ~100MB" selesai dieksekusi, menjaga kapasitas penyimpanan host tetap optimal.

3. Eksperimen Tanpa Flag --rm

   1. Detail Pengujian
   - Perintah: docker run --cpus="0.5" --memory="256m" week13-resource-limit
   Data Monitoring (docker stats):
   - CPU %: Berada di angka 49.55% (Hampir menyentuh batas maksimal 50%).
   - MEM USAGE: Terpakai 100.3 MiB.
   - MEM LIMIT: Terkunci di 256 MiB.
   - MEM %: Penggunaan memori sebesar 39.19%.
   - NET I/O: 1.17kB / 126B.
   - BLOCK I/O: 0B / 201kB.
   Hasil Pengamatan & Analisis
   - Stabilitas Limitasi: Meskipun angka CPU sedikit lebih tinggi (49.55%) dibandingkan pengujian sebelumnya, Docker tetap berhasil menjaga agar penggunaan tidak melewati angka 50%. Hal ini menunjukkan konsistensi fitur resource control pada Docker Engine.
   - Perilaku Pasca-Eksekusi (Tanpa --rm): Karena flag --rm tidak digunakan, setelah teks "Berjalan... Memori: ~100MB" selesai muncul, kontainer tidak akan hilang dari sistem.
   - Kontainer tersebut akan tetap ada di memori penyimpanan dengan status Exited.
   - Untuk membersihkannya, pengguna harus menjalankan perintah docker rm secara manual.
   - Penggunaan dalam Produksi: Eksperimen ini menunjukkan bahwa meskipun pembatasan resource tetap bekerja tanpa --rm, penggunaan flag tersebut sangat disarankan untuk pengujian berulang agar tidak terjadi penumpukan kontainer yang sudah tidak terpakai (sampah sistem).

   2. Detail Pengujian
   - Perintah: docker run week13-resource-limit
   Data Monitoring (docker stats) Berdasarkan screenshot tersebut, data yang dihasilkan adalah:
   - CPU %: Mencapai 60.01%.
   - MEM USAGE: Terpakai 100.3 MiB.
   - MEM LIMIT: Berada di kapasitas maksimal host, yaitu 7.702 GiB.
   - MEM %: Hanya menggunakan 1.27% dari total limit yang tersedia.
   - NET I/O: 1.17kB / 126B.
   - BLOCK I/O: 0B / 201kB.
   Hasil Pengamatan & Analisis
   - Konsumsi CPU: Dibandingkan dengan pengujian menggunakan limit (yang tertahan di bawah 50%), pada skenario ini CPU melonjak hingga 60.01%. Ini menunjukkan bahwa tanpa batasan, kontainer akan mengambil sumber daya sebanyak yang dibutuhkan atau yang diizinkan oleh sistem saat itu.
   - Resiko Sumber Daya: Dengan MEM LIMIT 7.702 GiB, kontainer memiliki keleluasaan penuh atas RAM. Jika aplikasi mengalami galat (bug) yang menyebabkan konsumsi RAM terus meningkat, hal ini dapat menyebabkan sistem utama (host) mengalami kelambatan atau bahkan freeze.
   - Manajemen Kontainer: Karena dijalankan tanpa --rm, setelah proses selesai, kontainer ini akan menempati ruang penyimpanan sebagai kontainer mati. Jika perintah ini dijalankan berulang kali tanpa pembersihan manual, daftar kontainer di Docker Desktop akan menumpuk dan memakan kuota disk.


---

## Kesimpulan
1. Efektivitas Isolasi Sumber Daya: Docker berhasil membatasi penggunaan CPU dan Memori secara akurat; terbukti pada skenario limit, CPU tertahan di bawah 50% (44-49%) dan Memori terkunci pada 100MB/256MB, sedangkan tanpa limit CPU melonjak hingga 70% dengan akses RAM penuh (7.7GB).
2. Dampak Terhadap Stabilitas Sistem: Penggunaan Resource Limit sangat krusial untuk mencegah sebuah kontainer mendominasi sumber daya komputer host, sehingga mencegah risiko sistem melambat atau crash akibat penggunaan CPU dan Memori yang tidak terkendali oleh satu aplikasi.
3. Efisiensi Manajemen Kontainer: Penggunaan parameter --rm terbukti sangat penting dalam menjaga kebersihan lingkungan kerja karena otomatis menghapus kontainer setelah eksekusi selesai, mencegah penumpukan kontainer berstatus exited yang dapat membebani kapasitas penyimpanan.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori?
   **Jawaban:**
   Pembatasan ini bertujuan untuk menjaga stabilitas sistem dan mencegah terjadinya monopoli sumber daya oleh satu kontainer. Tanpa adanya limit, sebuah kontainer dapat mengonsumsi seluruh kapasitas CPU yang mengakibatkan sistem host menjadi tidak responsif atau freeze. Dengan menerapkan batasan, User memastikan bahwa sisa sumber daya tetap tersedia untuk menjalankan proses sistem lainnya secara lancar.

2. Apa perbedaan VM dan container dalam konteks isolasi resource?
   **Jawaban:**
   Perbedaan utamanya terletak pada tingkat isolasinya: VM (Virtual Machine) membagi sumber daya secara kaku di level perangkat keras, sehingga setiap unit memiliki alokasi yang sudah ditentukan sejak awal. Sebaliknya, kontainer berbagi kernel yang sama dengan sistem host, sehingga isolasinya lebih ringan namun bersifat "terbuka". Oleh karena itu, kontainer memerlukan konfigurasi limit secara manual agar tidak mengambil sumber daya milik kontainer lain atau sistem utama.

3. Apa dampak limit memori terhadap aplikasi yang boros memori?
   **Jawaban:**
   Dampak utamanya adalah penghentian paksa kontainer oleh sistem Docker jika penggunaan memori melampaui batas yang telah ditetapkan. Mekanisme ini disebut sebagai pelindung agar aplikasi yang mengalami kebocoran memori (memory leak) tidak menguras seluruh RAM sistem host. Hal ini memastikan bahwa kegagalan pada satu aplikasi tidak menyebabkan seluruh server atau komputer User mengalami kerusakan data atau mati mendadak (crash).

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
