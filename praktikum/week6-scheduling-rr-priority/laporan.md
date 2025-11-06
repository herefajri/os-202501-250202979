
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling

---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB

---

## Tujuan
Diharapkan mahasiswa dapat mempelajari tentang:
- Menghitung waiting time (WT) dan turnaround time (TAT) pada algoritma RR dan Priority.
- Menyusun tabel "hasil perhitungan" dengan benar dan sistematis.
- Membandingkan performa algoritma antara RR dan Priority.
- Menjelaskan pengaruh time quantum dan prioritas terhadap keadilan eksekusi proses.
- Menarik kesimpulan mengenai efisiensi dan keadilan dari kedua algoritma tersebut.

---

## Dasar Teori
Tuliskan ringkasan teori (3–5 poin) yang mendasari percobaan.

Sumber Materi : Abraham Silberschatz, Peter Baer Galvin, Greg Gagne. Operating System Concepts, 10th Edition, Wiley, 2018.

---

## Langkah Praktikum
1. Siapkan Data Proses dengan menggunakan contoh data dibawah ini dan boleh dimodifikasi sesuai kebutuhan:
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. Untuk Eksperimen 1 – tentang Round Robin (RR), ikuti instruksi dibawah ini:
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Tugas : Catat sisa *burst time* tiap putaran.

3. Untuk Eksperimen 2 – tentang Priority Scheduling (Non-Preemptive), ikuti instruksi dibawah ini:
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi) dan lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Tugas : Buat tabel perbandingan hasil RR dan Priority.

4.  Untuk Eksperimen 3 – tentang Analisis Variasi Time Quantum (Opsional), ikuti instruksi dibawah ini:
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Tugas : Buat tabel perbandingan efek *quantum*.

5. Untuk Eksperimen 4 – terkait dengan dokumentasi. Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   dan tambahan, Tugas : Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis



---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling?
   **Jawaban:**

   
2. Apa pengaruh besar/kecilnya *time quantum* terhadap performa sistem?
   **Jawaban:**

    
3. Mengapa algoritma Priority dapat menyebabkan *starvation*?  
   **Jawaban:**
   


---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
