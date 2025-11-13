
# Laporan Praktikum Minggu 7
Topik: Sinkronisasi Proses dan Masalah Deadlock

---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB
---

## Tujuan
Setelah menyelesaikan tugas ini, diharapkan mahasiswa mampu:
1. Mengidentifikasi empat kondisi penyebab deadlock (*mutual exclusion, hold and wait, no preemption, circular wait*).  
2. Menjelaskan mekanisme sinkronisasi menggunakan *semaphore* atau *monitor*.  
3. Menganalisis dan memberikan solusi untuk kasus deadlock.  
4. Berkolaborasi dalam tim untuk menyusun laporan analisis.  
5. Menyajikan hasil studi kasus secara sistematis.  

---

## Dasar Teori

-  Cooperating Process adalah proses yang dapat memengaruhi atau dipengaruhi oleh proses lain yang dijalankan dalam sistem. Cooperating Process dapat langsung berbagi ruang alamat logis (yaitu, baik kode maupun data) atau hanya diizinkan untuk berbagi data melalui memori bersama atau pertukaran pesan. Namun, akses bersamaan ke data bersama dapat mengakibatkan ketidakkonsistenan data.
-  Penggunaan Semaphore Sistem operasi sering membedakan antara semaphore penghitung dan semaphore biner. Nilai dari semaphore penghitung dapat berkisar dalam domain yang tidak terbatas. Nilai dari semaphore biner hanya dapat berkisar antara 0 dan 1. Dengan demikian, semaphore biner berperilaku mirip dengan kunci mutex. Bahkan, pada sistem yang tidak menyediakan kunci mutex, semaphore biner dapat digunakan sebagai pengganti untuk menyediakan eksklusi mutual.
-  Deadlock, implementasi semaphore dengan waiting queue (antrian tunggu) dapat menyebabkan situasi di mana dua atau lebih proses menunggu tanpa batas waktu untuk suatu kejadian yang hanya dapat disebabkan oleh salah satu dari proses yang sedang menunggu tersebut. Kejadian yang dimaksud adalah eksekusi operasi signal(). Ketika keadaan seperti ini terjadi, proses-proses tersebut dikatakan berada dalam kondisi deadlock (kebuntuan).
-  The Dining-Philosophers Problem, bayangkan ada lima orang filsuf yang menghabiskan hidup mereka dengan berpikir dan makan. Para filsuf itu duduk melingkar di sebuah meja bundar yang dikelilingi oleh lima kursi, masing-masing milik satu filsuf. Di tengah meja terdapat semangkuk nasi, dan di atas meja tersebut terdapat lima sumpit tunggal. Ketika seorang filsuf sedang berpikir, ia tidak berinteraksi dengan rekan-rekannya. Dari waktu ke waktu, seorang filsuf merasa lapar dan berusaha mengambil dua sumpit yang paling dekat dengannya (yaitu sumpit yang berada di antara dirinya dan tetangga di sisi kiri serta kanannya). Seorang filsuf hanya dapat mengambil satu sumpit dalam satu waktu. Jelas bahwa ia tidak dapat mengambil sumpit yang sudah dipegang oleh tetangganya. Ketika seorang filsuf yang lapar berhasil memegang kedua sumpit secara bersamaan, ia mulai makan tanpa melepaskan sumpit tersebut. Setelah selesai makan, ia meletakkan kembali kedua sumpit dan mulai berpikir lagi.

Sumber : Abraham Silberschatz, Peter Baer Galvin, Greg Gagne. Operating System Concepts, 10th Edition, Wiley, 2018.

---

## Langkah Praktikum
1. **Persiapan Tim**
   - Bentuk kelompok beranggotakan 3–4 orang.  
   - Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).  
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. **Eksperimen 3 – Analisis Deadlock**
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ```

---

## Kode / Perintah

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis

**Status Kerangka Tim**
`
- Ketua : Andri Dwi Yuliyanto
- Implementasi : Andri Dwi Yuliyanto
- Analisis : Rafi Nurul Fauzan
- Dokumentasi : Muhammad Fajri Abdullah
`

1. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**

Pseudocode Deadlock Version

```pseudo
while true:
    think()
    pick_left_fork()
    pick_right_fork()
    eat()
    put_left_fork()
    put_right_fork()
```

**Analisis Deadlock:**
Deadlock terjadi saat semua filosofi ambil garpu kiri mereka tapi menunggu garpu kanan yang sedang dipegang filosof lain. Maka semua filosofi stuck saling tunggu garpu satu sama lain, tidak ada yang bisa makan, lalu jadilah kondisi deadlock.

2. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore)**

Modifikasi Pseudocode

```pseudo
semaphore max_dining = 4

while true:
    think()
    wait(max_dining)           # Batasi max filosof yang makan bersamaan
    if id_filosof == N:        # Filosof terakhir mengambil garpu secara terbalik
        pick_right_fork()
        pick_left_fork()
    else:
        pick_left_fork()
        pick_right_fork()
    eat()
    put_left_fork()
    put_right_fork()
    signal(max_dining)
```

**Analisis hasil:**
- Maksimal 4 filosof makan bersamaan, cegah semuanya ambil garpu dan tunggu.
- Filosof terakhir ubah urutan pengambilan garpu, lalu hilangkan circular wait.
- Dengan semaphore, mutual exclusion tetap terjaga.
- Deadlock tidak terjadi karena semua empat kondisi deadlock dicegah.


3. **Eksperimen 3 – Analisis Deadlock dalam Tabel**

| Kondisi Deadlock     | Terjadi di Versi Deadlock | Solusi di Versi Fixed  |
|---|---|---|
| Mutual Exclusion | Ya | Gunakan semaphore untuk mengontrol akses garpu |
| Hold and Wait | Ya | Batasi jumlah filosof yang makan bersamaan (semaphore max_dining) |
| No Preemption | Ya | Filosof melepaskan garpu secara sukarela setelah makan |
| Circular Wait | Ya | Filosof terakhir mengambil garpu secara terbalik |
   

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Sebutkan empat kondisi utama penyebab deadlock.
   **Jawaban:**    
2. Mengapa sinkronisasi diperlukan dalam sistem operasi?\
   **Jawaban:**    
3. Jelaskan perbedaan antara *semaphore* dan *monitor*.
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
