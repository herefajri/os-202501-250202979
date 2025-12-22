
# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock

---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB

---

## Tujuan
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.


---

## Dasar Teori
1. Deadlock adalah kondisi di mana proses saling menunggu resource sehingga tidak ada yang dapat melanjutkan eksekusi dan terjadi jika empat kondisi (mutual exclusion, hold and wait, no preemption, circular wait) terpenuhi.
2. Penanganan deadlock mencakup pencegahan, penghindaran, deteksi, dan pemulihan.
3. Deteksi deadlock dilakukan dengan algoritma berbasis wait-for graph untuk menemukan siklus.
4. Simulasi deadlock detection menggunakan dataset proses dan resource untuk menguji apakah sistem berada dalam kondisi deadlock.

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git commit -m "Minggu 11 - Deadlock Detection"
   ```
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
- Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
- Kaitkan hasil dengan teori deadlock (empat kondisi).
- 3. Sajikan hasil analisis dalam tabel dan narasi.

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?
   **Jawaban:**  


2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?
   **Jawaban:**  


3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
   **Jawaban:**  



---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
