
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
 sudo docker build -t week13-resource-limit .
 ```

```bash
sudo docker run --rm week13-resource-limit
```

```bash
sudo docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```

```bash
sudo docker run --cpus="0.5" --memory="256m" week13-resource-limit
```

```bash
sudo docker stats
```


---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](screenshots/hasil_limit_(tanpa_limit).png)

![Screenshot hasil](screenshots/hasil_limit_(dengan_limit).png)

![Screenshot hasil](screenshots/hasil_limit_(tanpa_rm).png)

---

## Analisis & Tugas

1. Eksperimen Tanpa Limit Resource
Pada tahap ini, User menjalankan kontainer menggunakan perintah dasar: 
```bash
sudo docker run --rm week13-resource-limit
```
   - Beban Kerja: Skrip Python melakukan perhitungan intensif secara terus-menerus tanpa batasan.
   - Respon CPU: Karena tidak ada pembatasan, Docker mengizinkan kontainer menggunakan seluruh kapasitas CPU yang dialokasikan pada VirtualBox.
   - Dampak Sistem: Sistem Lubuntu mengalami freezing atau kemacetan yang cukup parah. Hal ini terjadi karena sistem operasi host tidak memiliki sisa sumber daya untuk memproses antarmuka grafis atau input dari keyboard User.
   - Kesimpulan: Berjalan secara maksimal namun tidak stabil bagi lingkungan kerja sekitarnya.

2. Eksperimen Dengan Limit Resource (--cpus="0.5")
User menjalankan kontainer dengan parameter pembatasan:
```bash
sudo docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
```
   - Beban Kerja: Skrip yang sama tetap berusaha melakukan perhitungan maksimal.
   - Respon CPU: Docker melakukan throttling (pengereman) secara otomatis sehingga penggunaan CPU tertahan di angka 49.86%.
   - Dampak Sistem: Sistem tetap stabil dan responsif. Meskipun User merasakan sedikit keterlambatan (lag ringan) saat mengetik, sistem tidak membeku karena masih tersedia sisa 50% kapasitas CPU untuk proses sistem lainnya.
   - Kesimpulan: Memberikan keseimbangan antara performa aplikasi dan stabilitas sistem host.

3. Eksperimen Tanpa Flag --rm
User menjalankan kontainer tanpa perintah penghapusan otomatis: 
```bash
sudo docker run --cpus="0.5" --memory="256m" week13-resource-limit
```
   - Status Kontainer: Setelah User menghentikan proses dengan Ctrl + C, kontainer berubah status menjadi Exited namun datanya tetap tersimpan di penyimpanan Docker.
   - Konflik Identitas: Saat User mencoba mengulang perintah yang sama, sistem memberikan pesan error "Conflict". Hal ini dikarenakan nama kontainer tes-limit masih terdaftar di sistem sehingga tidak bisa digunakan kembali.
   - Dampak Penyimpanan: Tanpa flag ini, setiap pengulangan perintah oleh User akan menambah tumpukan file kontainer lama yang tidak terpakai (sampah data).
   - Kesimpulan: Berguna untuk keperluan audit atau pengecekan log setelah aplikasi mati, namun memerlukan pembersihan manual oleh User.




---

## Kesimpulan
- Stabilitas Sistem: Penggunaan limitasi resource terbukti menjaga stabilitas sistem host karena penggunaan CPU dapat tertahan di angka 49.86% sehingga sistem tidak mengalami freeze.
- Manajemen Resource: Tanpa pembatasan yang jelas, kontainer akan mengonsumsi seluruh daya CPU secara agresif yang menyebabkan gangguan fungsi pada sistem operasi utama.
- Siklus Hidup Kontainer: Penggunaan flag --rm sangat penting untuk mencegah terjadinya conflict nama saat User menjalankan perintah yang sama secara berulang.

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
