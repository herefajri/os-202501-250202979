
# Laporan Praktikum Minggu 4
Topik: Manajemen Proses dan User di Linux

---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB
---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
> Setelah menyelesaikan tugas ini,diharapkan mahasiswa mampu:

- Menjelaskan konsep proses dan user dalam sistem operasi Linux.
- Menampilkan daftar proses yang sedang berjalan dan statusnya.
- Menggunakan perintah untuk membuat dan mengelola user.
- Menghentikan atau mengontrol proses tertentu menggunakan PID.
- Menjelaskan kaitan antara manajemen user dan keamanan sistem.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

1. Perintah ps dapat digunakan untuk menunjukkan semua proses yang sedang berjalan
pada mesin (bukan hanya proses pada shell saat ini) dengan format :
 - `ps–fae` atau
 - `ps-aux`
  
2. Beberapa versi UNIX mempunyai utilitas sistem yang disebut top yang menyediakan
cara interaktif untuk memonitor aktifitas sistem. Statistik secara detail dengan proses yang
berjalan ditampilkan dan secara terus-menerus di-refresh . Proses
ditampilkan secara terurut dari utilitas CPU. Kunci yang berguna pada top adalah
 - s– set update frequency
 - u– display proses dari satu user
 - k– kill proses (dengan PID)
 - q– qui

3.  Utilitas untuk melakukan pengontrolan proses dapat ditemukan pada sistem UNIX
adalah perintah `killall`. Perintah ini akan menghentikan proses sesuai PID atau job number
proses

 Sumber:
 - Modul Praktikum Sistem Operasi – Universitas Sebelas Maret (UNS),  Proses dan Manajemen Proses (https://spada.uns.ac.id/pluginfile.php/880150/mod_resource/content/1/Modul%206%20-%20Proses%20dan%20Manajemen%20Proses.pdf)
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.

   1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).  
   - Pastikan Anda sudah login sebagai user non-root.  
   - Siapkan folder kerja:
     ```
     praktikum/week4-proses-user/
     ```

   2. **Eksperimen 1 – Identitas User**
   Jalankan perintah berikut:
   ```bash
   whoami
   id
   groups
   ```
   - Jelaskan setiap output dan fungsinya.  
   - Buat user baru (jika memiliki izin sudo):
     ```bash
     sudo adduser praktikan
     sudo passwd praktikan
     ```
   - Uji login ke user baru.

   3. **Eksperimen 2 – Monitoring Proses**
   Jalankan:
   ```bash
   ps aux | head -10
   top -n 1
   ```
   - Jelaskan kolom penting seperti PID, USER, %CPU, %MEM, COMMAND.  
   - Simpan tangkapan layar `top` ke:
     ```
     praktikum/week4-proses-user/screenshots/top.png
     ```

   4. **Eksperimen 3 – Kontrol Proses**
   - Jalankan program latar belakang:
     ```bash
     sleep 1000 &
     ps aux | grep sleep
     ```
   - Catat PID proses `sleep`.  
   - Hentikan proses:
     ```bash
     kill <PID>
     ```
   - Pastikan proses telah berhenti dengan `ps aux | grep sleep`.

   5. **Eksperimen 4 – Analisis Hierarki Proses**
   Jalankan:
   ```bash
   pstree -p | head -20
   ```
   - Amati hierarki proses dan identifikasi proses induk (`init`/`systemd`).  
   - Catat hasilnya dalam laporan.

   6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 4 - Manajemen Proses & User"
   git push origin main
   ```
2. Perintah yang dijalankan.
   ```bash
   whoami
   id
   groups
   ```
  ```bash
  sudo adduser praktikan
  sudo passwd praktikan
  ```
  ```bash
  ps aux | head -10
  top -n 1
  ```
  ```bash
  sleep 1000 &
  ps aux | grep sleep
  ```
  ```bash
  kill <PID>
  ```
  ```bash
  pstree -p | head -20
  ```
3. File dan kode yang dibuat.


4. Commit message yang digunakan.



---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
Tuliskan jawaban di bagian **Quiz** pada laporan:
1. Apa fungsi dari proses `init` atau `systemd` dalam sistem Linux?   
   **Jawaban:**  
2. Apa perbedaan antara `kill` dan `killall`?  
   **Jawaban:**  
3. Mengapa user `root` memiliki hak istimewa di sistem Linux?  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
