
# Laporan Praktikum Minggu 10
Topik: Manajemen Memori – Page Replacement (FIFO & LRU)

---

## Identitas
- **Nama**  : Muhammad Fajri Abdullah 
- **NIM**   : 250202979
- **Kelas** : 1IKRB
---

## Tujuan
1. Mengimplementasikan algoritma page replacement FIFO dalam program.
2. Mengimplementasikan algoritma page replacement LRU dalam program.
3. Menjalankan simulasi page replacement dengan dataset tertentu.
4. Membandingkan performa FIFO dan LRU berdasarkan jumlah *page fault*.
5. Menyajikan hasil simulasi dalam laporan yang sistematis.


---

## Dasar Teori
- Memori virtual memungkinkan program berjalan seolah-olah memiliki ruang alamat besar. Ketika halaman (page) yang dibutuhkan tidak ada di memori fisik, terjadi page fault sehingga sistem harus memuat halaman dari disk.
- Karena jumlah frame terbatas, sistem operasi harus memilih halaman mana yang diganti saat page fault. Tujuan utama algoritma page replacement adalah meminimalkan jumlah page fault untuk meningkatkan efisiensi sistem.
- Algoritma FIFO (First-In First-Out), halaman yang paling lama berada di memori diganti terlebih dahulu, mudah diimplementasikan dengan struktur queue, namun dapat menimbulkan Belady’s Anomaly (jumlah page fault bisa meningkat meski frame ditambah), sederhana, tetapi tidak selalu efisien.
- Algoritma LRU (Least Recently Used), halaman yang paling jarang digunakan (paling lama tidak diakses) diganti, lebih mendekati algoritma optimal karena mempertimbangkan riwayat akses namun mmbutuhkan pencatatan waktu atau urutan akses sehingga overhead lebih tinggi dibanding FIFO, lebih kompleks, namun biasanya menghasilkan jumlah page fault lebih sedikit dan performa lebih baik.
  
---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan *reference string* berikut sebagai contoh:
   ```
   7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2
   ```
   Jumlah frame memori: **3 frame**.

2. **Implementasi FIFO**

   - Simulasikan penggantian halaman menggunakan algoritma FIFO.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

3. **Implementasi LRU**

   - Simulasikan penggantian halaman menggunakan algoritma LRU.
   - Catat setiap *page hit* dan *page fault*.
   - Hitung total *page fault*.

4. **Eksekusi & Validasi**

   - Jalankan program untuk FIFO dan LRU.
   - Pastikan hasil simulasi logis dan konsisten.
   - Simpan screenshot hasil eksekusi.

5. **Analisis Perbandingan**

   Buat tabel perbandingan seperti berikut:

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | ... | ... |
   | LRU | ... | ... |


   - Jelaskan mengapa jumlah *page fault* bisa berbeda.
   - Analisis algoritma mana yang lebih efisien dan alasannya.

6. **Commit & Push**
  commit
   ```bash
   Minggu 10 - Page Replacement FIFO & LRU
   ```
---

## Kode / Perintah
FIFO (First-In First-Out)
```bash
def fifo_page_replacement(reference_string, frame_count):
    frames = []
    page_faults = 0
    hits = 0
    pointer = 0  

    print("Reference String:", reference_string)
    print("Jumlah Frame:", frame_count)
    print("\nStep | Page | Frame State | Hit/Fault")

    for step, page in enumerate(reference_string, start=1):
        if page in frames:
            hits += 1
            status = "Hit"
        else:
            page_faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % frame_count
            status = "Fault"

        print(f"{step:>4} | {page:>4} | {frames} | {status}")

    print("\nTotal Hits:", hits)
    print("Total Page Faults:", page_faults)


reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_count = 3

fifo_page_replacement(reference_string, frame_count)
```

LRU (Least Recently Used)
```bash
ef lru_page_replacement(reference_string, frame_count):
    frames = []
    page_faults = 0
    hits = 0
    usage_order = {}  

    print("Reference String:", reference_string)
    print("Jumlah Frame:", frame_count)
    print("\nStep | Page | Frame State | Hit/Fault")

    for step, page in enumerate(reference_string, start=1):
        if page in frames:
            hits += 1
            status = "Hit"
        else:
            page_faults += 1
            if len(frames) < frame_count:
                frames.append(page)
            else:
                lru_page = min(usage_order, key=usage_order.get)
                frames[frames.index(lru_page)] = page
                del usage_order[lru_page]
            status = "Fault"

        usage_order[page] = step

        print(f"{step:>4} | {page:>4} | {frames} | {status}")

    print("\nTotal Hits:", hits)
    print("Total Page Faults:", page_faults)

reference_string = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
frame_count = 3

lru_page_replacement(reference_string, frame_count)

```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/hasil_simulasi(FIFO).png)
![Screenshot hasil](screenshots/hasil_simulasi(LRU).png)

---

## Tugas & Analisis

**- Hasil simulasi dalam tabel atau grafik.**
  
  *Reference String: [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]*
  *Jumlah Frame: 3*
  
  FIFO (First-In First-Out)
  | Step | Page | Frame State | Hit/Fault
  |---|---|---|---|
  |   1 |    7 | [7] | Fault |
  |   2 |    0 | [7, 0] | Fault |
  |   3 |    1 | [7, 0, 1] | Fault  |
  |   4 |    2 | [2, 0, 1] | Fault   |   
  |   5 |    0 | [2, 0, 1] | Hit     |   
  |   6 |    3 | [2, 3, 1] | Fault   |   
  |   7 |    0 | [2, 3, 0] | Fault   |   
  |   8 |    4 | [4, 3, 0] | Fault |
  |   9 |    2 | [4, 2, 0] | Fault |
  |  10 |    3 | [4, 2, 3] | Fault |
  |  11 |    0 | [0, 2, 3] | Fault |
  |  12 |    3 | [0, 2, 3] | Hit |
  |  13 |    2 | [0, 2, 3] | Hit |

  - Total Hits: 3
  - Total Page Faults: 10

  LRU (Least Recently Used)
  | Step | Page | Frame State | Hit/Fault |
  |---|---|---|---|
  | 1 |    7 | [7] | Fault |
  | 2 |    0 | [7, 0] | Fault |
  | 3 |    1 | [7, 0, 1] | Fault |
  | 4 |    2 | [2, 0, 1] | Fault |
  | 5 |    0 | [2, 0, 1] | Hit |
  | 6 |    3 | [2, 0, 3] | Fault |
  | 7 |    0 | [2, 0, 3] | Hit |
  | 8 |    4 | [4, 0, 3] | Fault |
  | 9 |    2 | [4, 0, 2] | Fault |
  | 10 |    3 | [4, 3, 2] | Fault |
 | 11 |    0 | [0, 3, 2] | Fault |
 | 12 |    3 | [0, 3, 2] | Hit |
 | 13 |    2 | [0, 3, 2] | Hit |

  - Total Hits: 4
  - Total Page Faults: 9
  
**- Tabel perbandingan :**

   | Algoritma | Jumlah Page Fault | Keterangan |
   |:--|:--:|:--|
   | FIFO | 10 | 3 |
   | LRU | 9 | 4 |

**- Mengapa jumlah *page fault* bisa berbeda?**
  Dikarenakan adanya perbedaan mekanisme:
  - FIFO (First-In, First-Out), Halaman yang paling lama “masuk” ke memori dikeluarkan, tanpa melihat apakah halaman masih sering digunakan atau tidak. Akibatnya, halaman yang masih dibutuhkan bisa saja diganti, sehingga menambah jumlah page fault.
  - LRU (Least Recently Used), menggantikan halaman yang paling jarang digunakan dalam periode terakhir, lebih selaras dengan kebiasaan akses nyata, halaman yang baru dipakai biasanya dipertahankan dan bisa dikatakan bahwa LRU ebih “adaptif” terhadap pola akses, dan biasanya menghasilkan lebih sedikit page fault dibanding FIFO.
  - Faktor-faktor yang dapat membuat page fault dapat berbeda:
    - Urutan akses halaman, kalau program sering mengulang halaman yang baru dipakai, algoritma LRU lebih efisien dan kalau urutan akses mendorong halaman lama keluar, FIFO bisa salah buang halaman yang masih dibutuhkan.
    - Jumlah frame (slot memori), semakin banyak slot, semakin sedikit page fault karena lebih banyak halaman bisa disimpan, namun pada FIFO bisa terjadi Belady’s Anomaly: slot bertambah, page fault malah ikut bertambah.
    - Aturan algoritma, dimana FIFO membuang halaman yang paling lama masuk, tanpa peduli apakah masih dipakai sedangkan LRU membuang halaman yang paling lama tidak dipakai, lebih sesuai dengan pola penggunaan nyata.
      
**- Analisis algoritma mana yang lebih efisien dan alasannya?**
  Algoritma LRU lebih efisien dibanding FIFO, karena lebih hemat biaya akses memori, mengalami anomali, menghasilkan lebih sedikit page fault pada data yang sama, dan lebih cocok digunakan pada sistem nyata dibanding FIFO.
  
---

## Kesimpulan
- Algoritma LRU lebih efisien dibanding FIFO karena menghasilkan jumlah page fault lebih sedikit dan jumlah hit lebih banyak pada data yang sama.
- Perbedaan jumlah page fault terjadi karena aturan penggantian halaman berbeda, FIFO mengganti halaman yang paling lama masuk, sedangkan LRU mengganti halaman yang paling lama tidak dipakai.
- Pemilihan algoritma berpengaruh langsung pada performa sistem operasi, sehingga memahami pola akses halaman dan memilih algoritma yang sesuai sangat penting untuk mengurangi page fault dan meningkatkan efisiensi memori.
  
---

## Quiz
1. Apa perbedaan utama FIFO dan LRU?
   **Jawaban:**
  - FIFO (First-In, First-Out), menggunakan aturan yang berfokus pada halaman yang paling lama masuk ke memori, halaman itu akan diganti terlebih dahulu dengan tanpa memerdulikan status halaman itu , apakah masih sering dipakai atau tidak, sehingga bisa saja membuang halaman yang masih dibutuhkan.
  - LRU (Least Recently Used), menggunakan aturan yang berfokus pada halaman yang paling lama tidak dipakai, halaman yang tidak dipakai tersebut itu akan diganti sehingga ebih adaptif terhadap pola akses nyata, karena halaman yang baru dipakai biasanya akan dipakai lagi.
   
2. Mengapa FIFO dapat menghasilkan *Belady’s Anomaly*?
  **Jawaban:**
  Pada FIFO, halaman yang paling lama masuk akan diganti, tanpa peduli apakah halaman itu masih sering dipakai. Akibatnya dapat terjadi situasi anomali/tak wajar di mana menambah frame (slot memori) malah membuat halaman penting dibuang lebih cepat dan juga page fault bertambah.
     
3. Mengapa LRU umumnya menghasilkan performa lebih baik dibanding FIFO?
   **Jawaban:**
   karena dianggap lebih selaras dengan kebiasaan akses nyata, halaman yang baru dipakai biasanya dipertahankan dan bisa dikatakan bahwa LRU lebih “adaptif” terhadap pola akses, dan biasanya menghasilkan lebih sedikit page fault dibandingkan FIFO.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
