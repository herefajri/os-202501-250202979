
# Laporan Praktikum Minggu 5
Topik: Penjadwalan CPU – FCFS dan SJF

---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB

---

## Tujuan  

Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung waiting time dan turnaround time untuk algoritma FCFS dan SJF.
2. Menyajikan hasil perhitungan dalam tabel yang rapi dan mudah dibaca.
3. Membandingkan performa FCFS dan SJF berdasarkan hasil analisis.
4. Menjelaskan kelebihan dan kekurangan masing-masing algoritma.
5. Menyimpulkan kapan algoritma FCFS atau SJF lebih sesuai digunakan.
   
---

## Dasar Teori

- Penjadwalan FCFS atau First Come, First Served adalah algoritma penjadwalan CPU yang paling sederhana dengan skema proses yang pertama kali meminta CPU akan mendapatkan CPU lebih dulu.
- Implementasi kebijakan FCFS mudah dilakukan dengan antrian FIFO (First In, First Out).
- Penjadwalan SJF atau Short Job First adalah algoritma penjadwalan yang mengaitkan setiap proses dengan lama waktu CPU burst berikutnya yaitu durasi penggunaan CPU berikutnya oleh proses tersebut. Ketika CPU tersedia, CPU akan diberikan kepada proses yang memiliki CPU burst berikutnya paling pendek. Namun, jika dua proses memiliki durasi CPU burst yang sama, maka akanb digunakan penjadwalan FCFS untuk menentukan eksekusinya.


Sumber Materi : Abraham Silberschatz, Peter Baer Galvin, Greg Gagne. Operating System Concepts, 10th Edition, Wiley, 2018.

---

## Langkah Praktikum

1. **Siapkan Data Proses**
   Gunakan tabel proses berikut sebagai contoh (boleh dimodifikasi dengan data baru):
   | Proses | Burst Time | Arrival Time |
   |:--:|:--:|:--:|
   | P1 | 6 | 0 |
   | P2 | 8 | 1 |
   | P3 | 7 | 2 |
   | P4 | 3 | 3 |

2. **Eksperimen 1 – FCFS (First Come First Served)**
   - Urutkan proses berdasarkan *Arrival Time*.  
   - Hitung nilai berikut untuk tiap proses:
     ```
     Waiting Time (WT) = waktu mulai eksekusi - Arrival Time
     Turnaround Time (TAT) = WT + Burst Time
     ```
   - Hitung rata-rata Waiting Time dan Turnaround Time.  
   - Buat Gantt Chart sederhana:  
     ```
     | P1 | P2 | P3 | P4 |
     0    6    14   21   24
     ```

3. **Eksperimen 2 – SJF (Shortest Job First)**
   - Urutkan proses berdasarkan *Burst Time* terpendek (dengan memperhatikan waktu kedatangan).  
   - Lakukan perhitungan WT dan TAT seperti langkah sebelumnya.  
   - Bandingkan hasil FCFS dan SJF pada tabel berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | FCFS | ... | ... | Sederhana dan mudah diterapkan | Tidak efisien untuk proses panjang |
     | SJF | ... | ... | Optimal untuk job pendek | Menyebabkan *starvation* pada job panjang |

4. **Eksperimen 3 – Visualisasi Spreadsheet (Opsional)**
   - Gunakan Excel/Google Sheets untuk membuat perhitungan otomatis:
     - Kolom: Arrival, Burst, Start, Waiting, Turnaround, Finish.
     - Gunakan formula dasar penjumlahan/subtraksi.
   - Screenshot hasil perhitungan dan simpan di:
     ```
     praktikum/week5-scheduling-fcfs-sjf/screenshots/
     ```

5. **Analisis**
   - Bandingkan hasil rata-rata WT dan TAT antara FCFS & SJF.  
   - Jelaskan kondisi kapan SJF lebih unggul dari FCFS dan sebaliknya.  
   - Tambahkan kesimpulan singkat di akhir laporan.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 5 - CPU Scheduling FCFS & SJF"
   git push origin main
   ```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/FCFS&SJF_ORIxMODIF.png)

---

## Analisis
- **Eksperimen 1 – FCFS (First Come First Served)**
	
<img width="593" height="145" alt="image" src="https://github.com/user-attachments/assets/3a475c59-8f54-4e7a-b738-6b80a116bec8" />

```
  | P1 | P2 | P3 | P4 |
  0    6    14   21   24
```
- **Eksperimen 2 – SJF (Shortest Job First)**

<img width="593" height="145" alt="image" src="https://github.com/user-attachments/assets/efdb6595-a27f-4676-b610-52b6cc2c4e8f" />

```
  | P1 | P4 | P3 | P2 |
  0    6    9   16   24
```
- **Tabel hasil FCFS dan SJF**
  
| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| FCFS | 8,75 | 14,75 | Sederhana dan mudah diterapkan. | Tidak efisien untuk proses panjang. |
| SJF | 6,25 | 12,25 | Optimal untuk job pendek. | Menyebabkan *starvation* pada job panjang. |

---

## Tugas
1. Skenario tambahan FCFS dan SJF.

| Proses | Burst Time | Arrival Time |
   |---|---|---|
   | P1 | 6 | 0 |
   | P2 | 5 | 1 |
   | P3 | 9 | 2 |
   | P4 | 4 | 3 |

	- FCFS	
<img width="599" height="145" alt="image" src="https://github.com/user-attachments/assets/4e04548b-86a0-4b72-a4ce-6d136cc63697" />

	- SJF
<img width="599" height="145" alt="image" src="https://github.com/user-attachments/assets/7615afde-88c6-42e9-9907-3ed58909633d" />

2. Sajian hasil perhitungan dalam tabel perbandingan (FCFS vs SJF) dan analisis terhadap kelebihan dan kelemahan tiap algoritma.
| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| FCFS | 7,75 | 13,75 | Sederhana dan mudah diterapkan. | Tidak efisien untuk proses panjang. |
| SJF | 6,25 | 12,25 | Optimal untuk job pendek. | Menyebabkan *starvation* pada job panjang. |

---

## Kesimpulan
Kesimpulan dari praktikum ini.
- Algoritma SJF (Shortest Job First) menghasilkan Waktu Tunggu (Waiting Time) rata-rata dan juga Waktu Penyelesaian (Turnaround Time) rata-rata yang lebih rendah dibandingkan FCFS (First Come First Served).
- FCFS memang lebih sederhana dan mudah diterapkan namun tidak efisien untuk proses dengan burst time panjang, sedangkan SJF lebih optimal untuk proses panjang namun sulit diterapkan karena memerlukan prediksi burst time dan bisa menyebabkan stratvation pada proses panjang.
- FCFS cocok diterapkan/digunakan untuk sistem yang tiidak memerlukan efisiensi tinggi dan prosesnya sederhana, sedangkan SJF lebih cocok untuk sistem proses dengan burst pendek yang dapat di prediksi.

---

## Quiz
1. Apa perbedaan utama antara FCFS dan SJF?
   **Jawaban:**
   - FCFS mengeksekusi atau melayani proses berdasarkan urutan kedatangan, siapa yang datang lebih dulu, dia yang dilayani lebih dulu.
   - SJF mengeksekusi atau melayani berdasarkan durasi proses burst time terpendek terlebih dahulu atau dengan kata lain yang prosesnya paling cepat ia didahulukan.
     
2. Mengapa SJF dapat menghasilkan rata-rata waktu tunggu minimum?
   **Jawaban:**
   Karena SJF menerapkan metode memilih proses burst time terpendek, sehingga proses-proses cepat tidak tertunda oleh proses yang lebih lama dan meminimalkan waktu tunggu/waiting time total karena proses panjang tidak mengahalangi proses pendek yang menjadikan efisiensi waktu tunggu secara keseluruhan meningkat.
   
3. Apa kelemahan SJF jika diterapkan pada sistem interaktif?
   **Jawaban:**
   - dapat menyebabkan starvation atau kondisi di mana proses dengan proses waktu eksekusi/burst time yang panjang tak pernah mendapatkan giliran untuk dilayani/dieksekusi.
   - Proses interaktif memerlukan repon yang cepat dan adil untuk semua proses, sedangkan SJF bisa membuat beberapa proses penting tak pernah dieksekusi secara tepat waktu.
   - SJF memerlukan prediksi burst time yang akurat, yang sulit dilakukan dalam sistem interaktif dikarenakan durasi proses sering tidak diketahui sebelumnya.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
  **Jawaban:**  Memahami SJF yang mana memerlukan waktu dan pengaplikasian Gantt Chart yang membingungkan.
- Bagaimana cara Anda mengatasinya?
  **Jawaban:**  Menonton Youtube.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
