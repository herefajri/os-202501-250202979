
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
   git add .
   git commit -m "Minggu 10 - Page Replacement FIFO & LRU"
   git push origin main
   ```
---

## Kode / Perintah
FIFO (First-In First-Out)
```bash
import os

def load_reference_string(filename):
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, filename)
    
    try:
        with open(full_path, "r") as f:
            content = f.read().strip()
            content = content.replace(',', ' ')
            return list(map(int, content.split()))
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan di {base_path}")
        return []

def fifo_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0
    page_hits = 0
    pointer = 0
    total_requests = len(pages)

    print(f"=== SIMULASI FIFO PAGE REPLACEMENT ===")
    print(f"Reference String : {pages}")
    print(f"Jumlah Frame     : {frame_count}\n")
    print(f"{'Step':<5} | {'Akses':<6} | {'Status':<7} | {'Frames'}")
    print("-" * 40)

    for i, page in enumerate(pages):
        status = ""
        if page not in frames:
            page_faults += 1
            status = "FAULT"
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % frame_count
        else:
            page_hits += 1
            status = "HIT"

        frame_display = str(frames)
        print(f"{i+1:<5} | {page:<6} | {status:<7} | {frame_display}")

    hit_rate = (page_hits / total_requests) * 100
    fault_rate = (page_faults / total_requests) * 100

    print("-" * 40)
    print(f"HASIL AKHIR:")
    print(f"Total Akses      : {total_requests}")
    print(f"Total Page Hits  : {page_hits}")
    print(f"Total Page Faults: {page_faults}")
    print("-" * 40)

if __name__ == "__main__":
    data = load_reference_string("reference_string.txt")
    
    if data:
        fifo_page_replacement(data, frame_count=3)
```

LRU (Least Recently Used)
```bash
import os

def load_reference_string(filename):
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, filename)
    
    try:
        with open(full_path, "r") as f:
            content = f.read().strip()
            content = content.replace(',', ' ')
            return list(map(int, content.split()))
    except FileNotFoundError:
        print(f"Error: File '{filename}' tidak ditemukan.")
        return []

def lru_page_replacement(pages, frame_count):
    frames = []
    page_faults = 0
    page_hits = 0
    total_requests = len(pages)

    print(f"=== SIMULASI LRU PAGE REPLACEMENT ===")
    print(f"Reference String : {pages}")
    print(f"Jumlah Frame     : {frame_count}\n")
    print(f"{'Step':<5} | {'Akses':<6} | {'Status':<7} | {'Frames (Urutan LRU)'}")
    print("-" * 55)

    for i, page in enumerate(pages):
        status = ""
        if page not in frames:
            page_faults += 1
            status = "FAULT"
            if len(frames) < frame_count:
                frames.append(page)
            else:
                frames.pop(0)
                frames.append(page)
        else:
            page_hits += 1
            status = "HIT"
            frames.remove(page)
            frames.append(page)

        print(f"{i+1:<5} | {page:<6} | {status:<7} | {str(frames)}")

    hit_rate = (page_hits / total_requests) * 100
    fault_rate = (page_faults / total_requests) * 100

    print("-" * 55)
    print(f"HASIL AKHIR (LRU):")
    print(f"Total Page Hits  : {page_hits}")
    print(f"Total Page Faults: {page_faults}")
    print("-" * 55)

if __name__ == "__main__":
    data = load_reference_string("reference_string.txt")
    if data:
        lru_page_replacement(data, frame_count=3)
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
  
    | Step  | Akses  | Status  | Frames |
    |---|---|---|---|
    | 1     | 7      | FAULT   | [7]
    | 2     | 0      | FAULT   | [7, 0]
    | 3     | 1      | FAULT   | [7, 0, 1]
    | 4     | 2      | FAULT   | [2, 0, 1]
    | 5     | 0      | HIT     | [2, 0, 1]
    | 6     | 3      | FAULT   | [2, 3, 1]
    | 7     | 0      | FAULT   | [2, 3, 0]
    | 8     | 4      | FAULT   | [4, 3, 0]
    | 9     | 2      | FAULT   | [4, 2, 0]
    | 10    | 3      | FAULT   | [4, 2, 3]
    | 11    | 0      | FAULT   | [0, 2, 3]
    | 12    | 3      | HIT     | [0, 2, 3]
    | 13    | 2      | HIT     | [0, 2, 3]

----------------------------------------
HASIL AKHIR:
Total Akses      : 13
Total Page Hits  : 3
Total Page Faults: 10

  LRU (Least Recently Used)

    | Step  | Akses  | Status  | Frames (Urutan LRU) |
    |---|---|---|---|
    | 1     | 7      | FAULT   | [7] |
    | 2     | 0      | FAULT   | [7, 0] |
    | 3     | 1      | FAULT   | [7, 0, 1] |
    | 4     | 2      | FAULT   | [0, 1, 2] |
    | 5     | 0      | HIT     | [1, 2, 0] |
    | 6     | 3      | FAULT   | [2, 0, 3] |
    | 7     | 0      | HIT     | [2, 3, 0] |
    | 8     | 4      | FAULT   | [3, 0, 4] |
    | 9     | 2      | FAULT   | [0, 4, 2] |
    | 10    | 3      | FAULT   | [4, 2, 3] |
    | 11    | 0      | FAULT   | [2, 3, 0] |
    | 12    | 3      | HIT     | [2, 0, 3] |
    | 13    | 2      | HIT     | [0, 3, 2] |

-------------------------------------------------------
HASIL AKHIR (LRU):
Total Page Hits  : 4
Total Page Faults: 9

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
