
# Laporan Praktikum Minggu 9
Topik: Simulasi Algoritma Penjadwalan CPU

---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB

---

## Tujuan
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.
4. Menjelaskan hasil simulasi secara tertulis.
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.
   
---

## Dasar Teori
- Penjadwalan CPU adalah mekanisme penting dalam sistem operasi untuk menentukan urutan eksekusi proses pada prosesor.
- Algoritma First-Come, First-Served (FCFS) bekerja dengan prinsip antrian, di mana proses yang datang lebih dahulu akan dieksekusi lebih dahulu, sehingga sederhana namun dapat menimbulkan masalah convoy effect.
- Algoritma Shortest Job First (SJF) memilih proses dengan burst time paling pendek, yang secara teoritis menghasilkan waktu rata-rata tunggu paling optimal, meskipun sulit diimplementasikan karena memerlukan prediksi akurat terhadap burst time. 

---

## Langkah Praktikum
1. **Menyiapkan Dataset**
   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**
   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**
   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**
   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**
   
   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```



---

## Kode 

- Model FSCS

  [Code FCFS](code/(FCFS)_scheduling_simulation.py.txt.txt)
  [Code SJF](code/(SJF)_scheduling_simulation.py.txt.txt)
  
```bash
def fcfs(proses):
    proses.sort(key=lambda x: x['arrival'])

    time = 0
    for p in proses:
        p['start'] = max(time, p['arrival'])
        p['finish'] = p['start'] + p['burst']
        p['turnaround'] = p['finish'] - p['arrival']
        p['waiting'] = p['turnaround'] - p['burst']

        time = p["finish"]

    return proses


proses = [
    {'pid': 'P1', 'arrival': 0, 'burst': 6},
    {'pid': 'P2', 'arrival': 1, 'burst': 8},
    {'pid': 'P3', 'arrival': 2, 'burst': 7},
    {'pid': 'P4', 'arrival': 3, 'burst': 3},
]

result = fcfs(proses)
print('PID | Arrival | Burst | Start | Finish | Waiting | Turnaround')
for p in result:
    print(f'{p['pid']:3} | {p['arrival']:7} | {p['burst']:5} | {p['start']:5} | {p['finish']:10} | {p['waiting']:7} | {p['turnaround']:10}')

```

- Model SJF

```bash
def sjf_non_preemptive(proses):
    proses.sort(key=lambda x: x['arrival'])
    
    time = 0
    selesai = []
    ready_queue = []
    
    while proses or ready_queue:
        while proses and proses[0]['arrival'] <= time:
            ready_queue.append(proses.pop(0))
        
        if ready_queue:
            ready_queue.sort(key=lambda x: x['burst'])
            p = ready_queue.pop(0)
            
            p['start'] = max(time, p['arrival'])
            p['finish'] = p['start'] + p['burst']
            p['turnaround'] = p['finish'] - p['arrival']
            p['waiting'] = p['turnaround'] - p['burst']
            
            time = p['finish']
            selesai.append(p)
        else:
            time = proses[0]['arrival']
    
    return selesai


proses = [
    {'pid': 'P1', 'arrival': 0, 'burst': 6},
    {'pid': 'P2', 'arrival': 1, 'burst': 8},
    {'pid': 'P3', 'arrival': 2, 'burst': 7},
    {'pid': 'P4', 'arrival': 3, 'burst': 3},
]

result = sjf_non_preemptive(proses)
print('PID | Arrival | Burst | Start | Finish | Waiting | Turnaround')
for p in result:
    print(f"{p['pid']:3} | {p['arrival']:7} | {p['burst']:5} | {p['start']:5} | {p['finish']:10} | {p['waiting']:7} | {p['turnaround']:10}")


```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/hasil_simulasi(FCFS).png)
![Screenshot hasil](screenshots/hasil_simulasi(SJF).png)
---

## Tugas & Analisis

FCFS Model Program Python
  | PID | Arrival | Burst | Start | Finish | Waiting | Turnaround |
   |---|---|---|---|---|---|---|
  | P1  |       0 |     6 |     0 |          6 |       0 |          6 |
  | P2  |       1 |     8 |     6 |         14 |       5 |         13 |
  | P3  |       2 |     7 |    14 |         21 |      12 |         19 |
  | P4  |       3 |     3 |    21 |         24 |      18 |         21 |

SJF non-preemptive Model Program Python
   | PID | Arrival | Burst | Start | Finish | Waiting | Turnaround |
   |---|---|---|---|---|---|---|
   | P1  |       0 |     6 |     0 |          6 |       0 |          6 |
   | P4  |       3 |     3 |     6 |          9 |       3 |          6 |
   | P3  |       2 |     7 |     9 |         16 |       7 |         14 |
   | P2  |       1 |     8 |    16 |         24 |      15 |         23 |

----- 

**1. Penjelasan alur program.**
   **Jawaban:**

**FCFS:**
   - Fungsi fcfs(proses) menerima daftar proses berupa dictionary (pid, arrival, burst).
   - Proses diurutkan berdasarkan waktu kedatangan (arrival) menggunakan sort(key=lambda x: x['arrival']).
   - Variabel time digunakan untuk melacak waktu CPU saat ini.
   - Untuk setiap proses p:
      - start: waktu mulai eksekusi, yaitu maksimum antara time (waktu CPU terakhir) dan arrival (waktu kedatangan proses).
      - finish: waktu selesai eksekusi, dihitung dari start + burst.
      - turnaround: total waktu proses berada dalam sistem, yaitu finish - arrival.
      - waiting: waktu tunggu proses di antrian, yaitu turnaround - burst.
   - Setelah proses selesai, time diperbarui ke finish.
   - Setelah semua proses dihitung, hasil dikembalikan dalam bentuk list dictionary.
   - Program mencetak tabel berisi: PID, Arrival, Burst, Start, Finish, Waiting, Turnaround.

**SJF non-preemptive:**
   - Fungsi sjf_non_preemptive(proses) menerima daftar proses berupa dictionary (pid, arrival, burst).
   - Proses diurutkan terlebih dahulu berdasarkan waktu kedatangan (arrival) menggunakan sort(key=lambda x: x['arrival']).
   - Variabel time digunakan untuk melacak waktu CPU saat ini, ready_queue untuk menampung proses yang sudah datang, dan selesai untuk menyimpan proses yang sudah dieksekusi.
   - Selama masih ada proses yang belum selesai, program akan:
      - Memasukkan proses yang sudah datang ke ready_queue.
      - Jika ready_queue tidak kosong, proses diurutkan berdasarkan burst dan dipilih proses dengan burst terkecil.
   - Untuk setiap proses p:
      - start: waktu mulai eksekusi, yaitu maksimum antara time (waktu CPU terakhir) dan arrival (waktu kedatangan proses).
      - finish: waktu selesai eksekusi, dihitung dari start + burst.
      - turnaround: total waktu proses berada dalam sistem, yaitu finish - arrival.
      - waiting: waktu tunggu proses di antrian, yaitu turnaround - burst.
   - Setelah proses selesai, time diperbarui ke finish.
   - Setelah semua proses dihitung, hasil dikembalikan dalam bentuk list dictionary.
   - Program mencetak tabel berisi: PID, Arrival, Burst, Start, Finish, Waiting, Turnaround.
  
**2. Perbandingan hasil simulasi dengan perhitungan manual.**
   **Jawaban:**
  
   FCFS Model Program
    | PID | Arrival | Burst | Start | Finish | Waiting | Turnaround |
   |---|---|---|---|---|---|---|
  | P1  |       0 |     6 |     0 |          6 |       0 |          6 |
  | P2  |       1 |     8 |     6 |         14 |       5 |         13 |
  | P3  |       2 |     7 |    14 |         21 |      12 |         19 |
  | P4  |       3 |     3 |    21 |         24 |      18 |         21 |
  
   FCFS Model Manual Week-5
  
  <img width="593" height="145" alt="image" src="https://github.com/user-attachments/assets/56a4ede5-9142-461c-9150-73cc57f39840" />

   Hasilnya **[Sama]**

  SJF Model Program
   | PID | Arrival | Burst | Start | Finish | Waiting | Turnaround |
   |---|---|---|---|---|---|---|
   | P1  |       0 |     6 |     0 |          6 |       0 |          6 |
   | P4  |       3 |     3 |     6 |          9 |       3 |          6 |
   | P3  |       2 |     7 |     9 |         16 |       7 |         14 |
   | P2  |       1 |     8 |    16 |         24 |      15 |         23 |

  SJF Model Manual Week-5

  <img width="593" height="145" alt="image" src="https://github.com/user-attachments/assets/e5897cf9-d0b0-48f8-8c10-a9463e06a4a0" />

   Hasilnya **[Sama]**

**3. Penjelasan kelebihan dan keterbatasan simulasi.**
   **Jawaban:**
  - Kelebihan Simulasi
     - Lebih cepat: Tidak perlu menghitung satu per satu secara manual.
     - Lebih akurat: Mengurangi risiko salah hitung.
     - Bisa dipakai berulang: Dataset berbeda bisa langsung diuji dengan hasil yang konsisten.
     - Mudah ditampilkan: Hasil bisa langsung dibuat tabel atau grafik.
  - Keterbatasan Simulasi
     - Terbatas pada program: Kalau program hanya mendukung FCFS, algoritma lain harus ditulis lagi.
     - Kurang berguna untuk data kecil: Kalau prosesnya sedikit, manual lebih mudah dipahami.
     - Tidak menunjukkan langkah demi langkah: Simulasi hanya menampilkan hasil akhir, bukan proses berjalan secara nyata.

---

## Kesimpulan
- Simulasi mempermudah perhitungan algoritma penjadwalan seperti FCFS dan SJF, terutama untuk dataset besar, sehingga hasil lebih cepat dan akurat dibandingkan perhitungan manual.
- Hasil simulasi konsisten dengan perhitungan manual pada dataset kecil, sehingga dapat dipercaya sebagai alat bantu analisis.
- Pemahaman konsep tetap penting meskipun simulasi otomatis akarena menggunakan program, perhitungan manual tetap diperlukan agar mahasiswa memahami alur algoritma dasar dan tidak hanya bergantung pada program.

---

## Quiz
1. Mengapa simulasi diperlukan untuk menguji algoritma scheduling?
   **Jawaban:**
   - Menghemat waktu dan tenaga jika dataset proses banyak, perhitungan manual akan sangat rumit dan rawan salah.
   - Memberikan hasil yang konsisten karena program selalu mengikuti aturan algoritma yang sama/yang telah ditentukan, sehingga hasilnya tidak berubah-ubah dan bisa dipercaya.
   - Mahasiswa dapat menguji berbagai skenario dengan mencoba dataset berbeda (misalnya mengubah jumlah proses, waktu kedatangan, burst time) untuk melihat bagaimana algoritma bekerja dalam kondisi yang beragam.

   
2. Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar?
   **Jawaban:**
   - Perhitungan Manual
      - jika proses semakin banyak dan semakin panjang pula langkah perhitungan, maka risiko kesalahan meningkat pula, belum lagi efisiensi waktu yang rendah.
      - Menyusun tabel waiting time dan turnaround time untuk puluhan atau ratusan proses/dataset dapat membingungkan mahasiswa, ini bisa meningkatkan risiko kesalahan perhitungan karena human error.
      - Dan tentu tidak cocok untuk eksperimen dengan banyak variasi dataset.
   - Perhitungan dengan Simulasi
      - Program langsung menghitung semua proses, sangat baik untuk efisiensi waktu.
      - Hasil selalu sesuai dengan algoritma yang diimplementasikan/ ditentukan pengguna, tidak terpengaruh oleh kelelahan atau kesalahan manusia kecuali dalam bagian input.
      - Dataset besar bisa diuji dengan berbagai algoritma (FCFS, SJF, RR, dll.) untuk melihat performa masing-masing.
      - Output bisa langsung ditampilkan dalam bentuk tabel atau Gantt chart.
   
3. Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.
   **Jawaban:**
   FCFS, dikarenakan sistemnnya yang sederhana dengan metode FIFO, tidak perlu membandingkan burst time atau melakukan pemilihan ulang, dan urutan proses berdasarkan arrival, lalu jalankan satu per satu. Program hanya perlu menghitung start, finish, waiting, dan turnaround.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
